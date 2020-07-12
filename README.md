# <img src="https://cdn.iconscout.com/icon/free/png-512/discord-3-569463.png" alt="discord icon" width="32"/> SHR1MP Bot
This is a discord bot for the Shr1mp server with the intent of supporting all of its users needs. The Bot will be hosted on heroku upon release.

## Functionality
- Start/Stop Factorio server

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
- TOKEN - a "key" used to control a Discord Bot. Acquire it from *discordapp.com/developers/applications/{APPLICATION_ID}/bots*.
- INSTANCE_ID - used to find our factorio server. Acquire it from [console.aws.amazon.com](https://eu-central-1.console.aws.amazon.com/ec2/v2/home?region=eu-central-1#Instances:sort=desc:instanceId)

#### AWS configuration
- Download AWS CLI
    - [Windows](https://awscli.amazonaws.com/AWSCLIV2.msi)
    - [MacOS](https://awscli.amazonaws.com/AWSCLIV2.pkg)
    - [Linux](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html#cliv2-linux-install)
- Create new access key
    - enter the [IAM Users page for admin](https://console.aws.amazon.com/iam/home?nc2=h_m_sc#/users/admin?section=security_credentials)
    - Create access key and store the information given
- Run the following command
```bash
$ aws configure
```
AWS Access Key ID: `from the step above`  
AWS Secret Access Key: `from the step above`  
Default region name: eu-central-1  
Default output format: json

## How to run
<!-- todo: Write tutorial how to run it but also how to deploy changes -->
To push all the dependencies to the requirements.txt
```bash
$ pip freeze > requirements.txt
```
