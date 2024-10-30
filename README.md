# Demo: Exploiting Leaked Timestamps From Google Chrome Extensions

## Description
This demo showcases how Chromium extensions are unintentionally exposing an exploit that can be used for advanced browser fingerprinting.

The demo demonstrates how any website can easily obtain a uniqnue visitor identifier using the last modified timestamps of extension files.

The demo works only on Google Chrome Desktop mode and does not work on Incognito.

[Read our article](https://fingerprint.com/blog/exploiting-leaked-timestamps-google-chrome-extensions) for more information.

## Quick start
Make sure you have Python isntalled. If you do not have it installed, you can install it from the offical Python [website](https://www.python.org/downloads/).

Install the requirements:
```bash
python3 -m pip install -r requirements.txt
```

Run the server:
```bash
python3 main.py
```

The demo should now be available at `http://localhost:5000`