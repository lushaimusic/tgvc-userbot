from os import environ

# import logging
from pyrogram import Client, idle

API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
SESSION_NAME = environ["SESSION_NAME"]

PLUGINS = dict(
    root="plugins",
    include=[
        "vc." + environ["PLUGIN"],
        "ping",
        "sysinfo"
    ]
)

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=PLUGINS)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
