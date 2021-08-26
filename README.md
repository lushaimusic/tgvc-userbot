# Telegram Voice Chat UserBot

A Telegram UserBot to Play music 🎶 in Voice Chats.

It's recommended to use an USA number.(if your real number is suspended I'm not responsible.use at your own risks) no grauanty no waranty
Use at your own risks..

## Give your 💙

Before clicking on deploy to heroku just click on fork and star just below

<p align="center">
  <a href="https://github.com/LushaiMusic/vc-userbot/fork">
    <img src="https://img.shields.io/github/forks/LushaiMusic/vc-userbot?label=Fork&style=social">
    
  </a>
  <a href="https://github.com/LushaiMusic/vc-userbot">
    <img src="https://img.shields.io/github/stars/LushaiMusic/vc-userbot?style=social">
  </a>
</p>

## How to deploy 

Click the below button to watch the video tutorial on deploying

<a href="https://youtu.be/EYLyV3VHthc"><img src="https://img.shields.io/badge/How%20To%20Deploy-blue.svg?logo=Youtube"></a>
<a href="https://youtu.be/EYLyV3VHthc"><img src="https://img.shields.io/youtube/views/EYLyV3VHthc?style=social">

###  GET STRING SESSION FROM REPL RUN

 [![Run on Repl.it](https://camo.githubusercontent.com/05149b448485553c6f14f6430a45c12dcc79ed3c/68747470733a2f2f7265706c2e69742f62616467652f6769746875622f6a61727669733231303930342f4a6172766973)](https://replit.com/@ZauteKm/generate-pyrogram-session-string#main.py)

## Deploy to Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/Puutraaa/Desah-userbot)

- Enable the worker after deploy the project to Heroku

Change the value of `PLUGIN` variable if you want to try other voice chat
plugins.

## Introduction

**Features**

- Playlist, queue
- Loop one track when there is only one track in the playlist
- Automatically downloads audio for the first two tracks in the playlist to
  ensure smooth playing
- Automatically pin the current playing track
- Show current playing position of the audio

**Plugin**: vc.`player`

Commands only works in groups, userbot account itself and contacts can use any
commands, all members can use common commands after the userbot join the VC

1. Start the userbot, try `!ping`, `!uptime` or `!sysinfo` command to check if
   the bot was running
2. send `!join` to a voice chat enabled group chat from userbot account itself
   or its contacts, be sure to make the userbot account as group admin and give
   it at least the following permissions:
    - Delete messages
    - Manage voice chats (optional)
3. reply to an audio with `/play` to start playing it in the voice chat, every
   member of the group can use common commands such like `/play`, `/current`
   and `!help` now.
4. check `!help` for more commands

**Plugin**: vc.`channel`

Almost same as `player` plugin but commands only works in Saved Messages,
`!join` takes arguments to be able to join group or channel voice chats.

**Plugin**: `ping` and `sysinfo`

Commands only works for userbot account itself and its contacts.

## Requirements

- Python 3.6 or higher
- A
  [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api)
  and a Telegram account
- Choose plugins you need, install dependencies which listed above and run
  `pip install -U -r requirements.txt` to install Python package dependencies
  as well
- [FFmpeg](https://www.ffmpeg.org/)

## Run

Choose one of the two methods and run the userbot with
`python userbot.py`, stop with <kbd>CTRL+c</kbd>. The following example assume
that you were going to use `vc.player` and `ping` plugin, replace
`api_id`, `api_hash` to your own value.

### Method 1: use config.ini

Create a `config.ini` file

```
[pyrogram]
api_id = 1234567
api_hash = 0123456789abcdef0123456789abcdef

[plugins]
root = plugins
include =
    vc.player
    ping
    sysinfo
```

### Method 2: write your own userbot.py

Replace the file content of `userbot.py`

```
from pyrogram import Client, idle

api_id = 1234567
api_hash = "0123456789abcdef0123456789abcdef"

plugins = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping",
        "sysinfo"
    ]
)

app = Client("tgvc", api_id, api_hash, plugins=plugins)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
```

## Notes

- Read module docstrings of [plugins/](plugins) you are going to use at the
  beginning of the file for extra notes

# License

AGPL-3.0-or-later

# Credits :

This Repo Is Just A Custom Fork Of [callsmusic/tgvc-userbot](https://github.com/callsmusic/tgvc-userbot)
