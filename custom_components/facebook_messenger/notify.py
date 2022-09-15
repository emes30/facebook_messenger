"""Facebook platform for notify component."""
from http import HTTPStatus
import json
import logging

import requests
import voluptuous as vol

import os

from homeassistant.components.notify import (
    ATTR_DATA,
    ATTR_TARGET,
    PLATFORM_SCHEMA,
    BaseNotificationService,
)
from homeassistant.const import CONTENT_TYPE_JSON
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

CONF_PAGE_ACCESS_TOKEN = "page_access_token"
CONF_TARGETS = "targets"
CONF_NAME = "name"
CONF_SID = "sid"
BASE_URL = "https://graph.facebook.com/v2.6/me/messages"
KEY_MEDIA = "media"
KEY_MEDIA_TYPE = "media_type"


TARGET_SCHEMA = vol.Schema(
    {vol.Required(CONF_SID): cv.string, vol.Required(CONF_NAME): cv.string}
)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_PAGE_ACCESS_TOKEN): cv.string,
        vol.Optional(CONF_TARGETS): vol.All(cv.ensure_list, [TARGET_SCHEMA]),
    }
)


def get_service(hass, config, discovery_info=None):
    """Get the Facebook notification service."""
    return FacebookNotificationService(
        config[CONF_PAGE_ACCESS_TOKEN], config[CONF_TARGETS]
    )


class FacebookNotificationService(BaseNotificationService):
    """Implementation of a notification service for the Facebook service."""

    def __init__(self, access_token, targets):
        """Initialize the service."""
        self.page_access_token = access_token
        self.targets_map = {}
        if targets:
            self.make_targets_map(targets)

    def make_targets_map(self, targets):
        for item in targets:
            self.targets_map[item[CONF_NAME]] = item[CONF_SID]

    def send_message(self, message="", **kwargs):
        """Send some message."""
        payload = {"access_token": self.page_access_token}
        targets = kwargs.get(ATTR_TARGET)
        data = kwargs.get(ATTR_DATA)

        body_message = {"text": message}

        media = None
        media_type = "image/jpeg"

        if data is not None:
            body_message.update(data)
            # Only one of text or attachment can be specified
            if "attachment" in body_message:
                body_message.pop("text")
            if KEY_MEDIA in body_message:
                media = body_message[KEY_MEDIA]
                if not os.path.exists(media):
                    _LOGGER.error(f"File not found. [{ media }]")
                    media = None

        if not targets:
            _LOGGER.error("At least 1 target is required")
            return

        for target in targets:
            # check target map
            if target in self.targets_map:
                target = self.targets_map[target]

            # If the target starts with a "+", it's a phone number,
            # otherwise it's a user id.
            if target.startswith("+"):
                recipient = {"phone_number": target}
            else:
                recipient = {"id": target}

            body = {
                "recipient": recipient,
                "message": body_message,
                "messaging_type": "MESSAGE_TAG",
                "tag": "ACCOUNT_UPDATE",
            }
            resp = requests.post(
                BASE_URL,
                data=json.dumps(body),
                params=payload,
                headers={"Content-Type": CONTENT_TYPE_JSON},
                timeout=10,
            )
            if resp.status_code != HTTPStatus.OK:
                log_error(resp)


def log_error(response):
    """Log error message."""
    obj = response.json()
    error_message = obj["error"]["message"]
    error_code = obj["error"]["code"]

    _LOGGER.error(
        "Error %s : %s (Code %s)", response.status_code, error_message, error_code
    )
