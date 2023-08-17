# Commander

Self-hosted discord bot to control your MCSS instance.

## Installation

Prerequisites:

* Python 3.9
* Discord Bot Token

.ENV file

Dont forget to change rename .env.example to .env and change it's contents:

```env
BOT_TOKEN=replace with bot token
BOT_OWNER=unused for now
BOT_GUILD=your discord server id
MCSS_KEY=mcss api key, check mcss docs for info
MCSS_API=http://yourapiurl.local:25560
```
Installing required packages:
```bash
  pip install -r requirements.txt
```

## Run Locally

Easy!

```bash
  python3 ./commander.py
```
Alternatively:
```bash
  py ./commander.py
```

## Usage
The bot makes use of discord slash commands, these are the currently implemented commands:
```
/server start (server name)
/server stop (server name)
```
## Notes

Currently only the bot owner can execute commands, regardless of the BOT_OWNER value in the .ENV file