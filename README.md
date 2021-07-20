# WebPhotographer

A Telegram bot that is able to take screenshots of webpages remotely and send it to its users.

## How to set up

In order to run the bot you will need a [Telegram](https://core.telegram.org/api) API key.

rename the file from `example.env` to `.env` and put the key in the file.

```env
TELEGRAM_KEY=<KEY_API>
```

install packages and run:

### NixOS Users

```
$ nix develop

$ python main.py
```

### Non-NixOS Users

```
$ pip install -r requirements.txt

$ python main.py
```