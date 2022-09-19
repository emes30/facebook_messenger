[![Validate](https://github.com/emes30/facebook_messenger/workflows/Validate/badge.svg)](https://github.com/emes30/facebook_messenger/actions?query=workflow:"Validate")
[![GitHub release](https://img.shields.io/github/release/emes30/facebook_messenger?include_prereleases=&sort=semver&color=blue)](https://github.com/emes30/facebook_messenger/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![buymeacoffee](https://img.shields.io/badge/BuyMeACoffee-Donate-blue.svg)](https://www.buymeacoffee.com/emes30)

# Facebook Messenger for Home Assistant

This is an upgrade for <a href="https://www.home-assistant.io" target="_blank">Home Assistant</a> Facebook integration. It allows you to send notification to Messenger with images.

----

### Contents

 * [Functionality](#functionality)
 * [Installation](#installation)
 * [Configuration](#configuration)
 * [Installation and Configuration Summary](#installation-and-configuration-summary)
 * [Usage](#usage)
 * [License](#license)

----

### Functionality

This integration is based on Facebook integration currently available in Home Assistant.
It's possible to send text-based and image notifications. You can also assign names to your
SIDs and use it as notification target.

----

### Installation

HACS is not available yet. You must use manual method.
Copy the `facebook_messenger` folder into the `config\custom_components` folder of your Home Assistant instance, and restart.

----

### Configuration

This integration exposes itself as a <a href="https://www.home-assistant.io/integrations/notify/" target="_blank">notifications integration</a>, and can be configured by adding this snippet in your `configuration.yaml` file:

```yaml
notify:
  name: messenger
  platform: facebook_messenger
  page_access_token: <YOUR FACEBOOK TOKEN>
  targets:
    - sid: <YOUR SID>
      name: mike
```

Replace `<YOUR FACEBOOK TOKEN>` with your facebook token, use secrets.yaml for better protection.

`targets` attribute is optional. If you declared it, you can use human readable names instead of digits as your notification's target.

Restart Home Assistant to load your configuration.

----

### Installation and Configuration Summary

Quick summary to get things working:

- Install **facebook_messenger** integration
- Reboot Home Assistant
- Create a `notify` entity, use your facebook page token
- Reboot Home Assistant
- Start adding the new entity to your automations & scripts :)

----

### Usage

#### Text notification

```yaml
  action:
    - service: notify.messenger
      data:
        target: mike
        message: "Hello from Home Assistant."
```

#### Image notification

```yaml
  action:
    - service: notify.messenger
      data:
        target: mike
        data:
          media: "<path to image file on server>"
          media_type: "image/jpeg"
```

It is important to specify correct `media_type`. It is validated by Facebook and message will be rejected when `media_type` doesn't match actual media file type. `image/jpeg` is default value.

You can also test it in Developer Tools, under Services tab.

----

### License

This software is released under the <a href="https://opensource.org/licenses/MIT" target="_blank">MIT license</a>.
