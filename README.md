# <img src="https://cdn.iconscout.com/icon/free/png-512/discord-3-569463.png" alt="discord icon" width="32"/> Discord Bot
This is a discord bot for the Shr1mp server with the intent of supporting all of its users needs. The Bot will be hosted on AWS upon release.

## Functionality
- Start/Stop Factorio server `in progress`
## Requirements
#### Python 3.6.x (latest version)
- [Windows](https://www.python.org/downloads/windows/)
- [MacOS](https://www.python.org/downloads/mac-osx/)
- [Linux](https://www.python.org/downloads/source/)
- [Other](https://www.python.org/download/other/)

#### Install dependencies
```bash
$ pip install -r requirements.txt
```

#### Environment variables:
Create `.env` file in the root directory and assign values of the following variables:
- token - a "key" used to control a Discord Bot. Acquire it from *discordapp.com/developers/applications/{APPLICATION_ID}/bots*.

## How to run
<!-- todo: Write tutorial how to run it but also how to deploy changes -->
To push all the dependencies to the requirements.txt
```bash
$ pip freeze > requirements.txt
```
## Recommended IDE
[PyCharm](https://www.jetbrains.com/pycharm/)
