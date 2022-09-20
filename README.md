[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=emes30&repository=facebook_messenger&category=integration)
\
[![Validate](https://github.com/emes30/facebook_messenger/workflows/Validate/badge.svg)](https://github.com/emes30/facebook_messenger/actions?query=workflow:"Validate")
[![GitHub release](https://img.shields.io/github/release/emes30/facebook_messenger?include_prereleases=&sort=semver&color=blue)](https://github.com/emes30/facebook_messenger/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration)
[![buymeacoffee](https://img.shields.io/badge/BuyMeACoffee-Donate-blue.svg)](https://www.buymeacoffee.com/emes30)

# Facebook Messenger for Home Assistant

This is an upgrade for <a href="https://www.home-assistant.io" target="_blank">Home Assistant</a> Facebook integration. It allows you to send notification to Messenger with images.

----

### Contents

 * [Functionality](#functionality)
 * [Installation](#installation)
 * [Configuration](#configuration)
 * [How to obtain your Facebook token](#how-to-obtain-your-facebook-token)
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

HACS is the preferred installation method. Click [here](https://my.home-assistant.io/redirect/hacs_repository/?owner=emes30&repository=facebook_messenger&category=integration), you'll be
redirected to your Home Assistant instance. If link doesn't work, you can find Facebook Messenger
in HACS integrations repository list.\
Manual method. Copy the `facebook_messenger` folder into the `config\custom_components` folder of your Home Assistant instance, and restart.

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

---

### How to obtain your Facebook token

To use this integration you must register as Facebook developer and create application that will be
sending notifications on your behalf. First login to your Facebook account and click [here](https://developers.facebook.com/async/registration) to start registration process. It requires few steps, you must confirm your phone and email address, choose occupation (use developer :wink:).\
When you've done with registration process, add [new application](https://developers.facebook.com/apps/create/).

1. Choose app type Business
2. Choose Display name, enter your email and click Create App. You'll have to enter password again.
3. On the next page **Add products to your app** find Messenger tile and click Set up.
4. Find **Access Tokens** section and click **Create new Page**, new tab will open, keep this one open, you return here in steps 7 and 10
5. Provide Name and Category, you may choose whatever you like, but Name must be unique.
6. Click next until you reach Ready page, you don't have to provide any additional information
7. Return to **Access Tokens** tab, and this time click **Add or remove Page**, new window opens
8. Confirm that it's really you, check Page you've just created, and click Next
9. Ignore warning and click Ready!, your page is connected with Facebook
10. Return to **Access Tokens** tab again, now click **Generate token**, check I understand,
11. Success :muscle: finally you have your token, copy and save it


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
