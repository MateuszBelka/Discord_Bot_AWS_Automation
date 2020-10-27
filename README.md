# <img src="https://cdn.iconscout.com/icon/free/png-512/discord-3-569463.png" alt="discord icon" width="32"/> SHR1MP Bot
This is a discord bot for the Shr1mp server with the intent of supporting all of its users needs. The Bot will be hosted on heroku upon release.

## Functionality
- Start/Stop Factorio AWS server
- Start/Stop Minecraft AWS server
- Start/Stop Terraria AWS server
- Automatically update server hardware depending on user needs
- Automate customization of offline server's configuration to minimize costs
- Generate random meme from selected subreddits


## Requirements
#### Python 3.6.x 
(3.8 may cause ssl issues. For [solution](https://github.com/Rapptz/discord.py/issues/4159) download [this PEM](https://beans-took-my-kids.reeee.ee/38qB2n.png) from [here](https://crt.sh/?id=2835394))
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
- INSTANCE_ID_FACTORIO - used to find our factorio server. Acquire it from [console.aws.amazon.com](https://eu-central-1.console.aws.amazon.com/ec2/v2/home?region=eu-central-1#Instances:sort=desc:instanceId)
- INSTANCE_ID_MINECRAFT - used to find our minecraft server. Acquire it from [console.aws.amazon.com](https://eu-central-1.console.aws.amazon.com/ec2/v2/home?region=eu-central-1#Instances:sort=desc:instanceId)
- INSTANCE_ID_TERRARIA - used to find our terraria server. Acquire it from [console.aws.amazon.com](https://eu-central-1.console.aws.amazon.com/ec2/v2/home?region=eu-central-1#Instances:sort=desc:instanceId)
- T2SMALL_INSTANCE_CHANNELS - discord channels in which server commands are supposed to change the instance type to t2.small
- REDDIT_APP_ID
- REDDIT_APP_SECRET
- REDDIT_ENABLED_MEME_SUBREDDITS

### AWS configuration
#### Through AWS CLI
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

#### Through additional environments variables (recommended on heroku)
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY
- AWS_DEFAULT_REGION
- output

## How to deploy
In order for host to have access to all libraries in use. Run this command.
```bash
$ pip freeze > requirements.txt
```

Deployments to heroku are made automatically when new commits are pushed to master branch.
