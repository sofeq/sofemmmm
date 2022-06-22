## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1ApWapzMBuyHYurdGV0_VQEtAV2TdfblfV1nsiZ_5WqGmXw_D7UFJzN7zL0Vk-XYGLOMhGQmBLGiUNKqoT2s6IkoBy_4tstFwIQ092ZBJc9rmPiyReRrVeh7bFHo9QomMHeKSmz7UmehqKxiiz1d8YIErJA55Mc6LM7zryGZvo0yd6BbWmAOWXuwCSbZJGym6uAoq8MRVnkURtbSqUr00cHuDVYXNj2-a2UFE8tyshFdcpn__Qh81-w_BPxqDAlKbefwGFXAfHpC3n4Wo90Js0sZwrMWyceOBTk-zt_BsN1fE9LenYIDE_Ff26SN7319nVrPD1nZ1aUNbZafYTXACk2H4_DA7dGQ=")
BOT_TOKEN = getenv("BOT_TOKEN", "5583750786:AAFmZcJjU9yDjFib2VvT1kQouRpWmtx-y10")
BOT_NAME = getenv("BOT_NAME", "song")
API_ID = int(getenv("API_ID", "8186557"))
API_HASH = getenv("API_HASH", "efd77b34c69c164ce158037ff5a0d117")
OWNER_NAME = getenv("OWNER_NAME", "sofe")
OWNER_USERNAME = getenv("OWNER_USERNAME", "no_nn")
ALIVE_NAME = getenv("ALIVE_NAME", "sof")
BOT_USERNAME = getenv("BOT_USERNAME", "musicf7sbot")
OWNER_ID = getenv("OWNER_ID", "1686444936")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "no_nn")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "bc_cb")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "bc_cb")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1686444936").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
