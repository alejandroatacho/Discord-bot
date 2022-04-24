# Libraries
import discord
import os
import urllib.request
import requests
import random
from discord.ext import commands
from discord.ext.tasks import loop
#from twitch import get_notifications
from discord import Streaming
from discord.utils import get
from discord import Forbidden
from discord.ext.commands import Cog
from discord.ext.commands import command
from dotenv import load_dotenv
load_dotenv() 

# Variables
client = discord.Client()
modes_Dict = {'osu': 0, 'taiko': 1, 'ctb': 2, 'mania': 3}
modes = ["osu", "taiko", "ctb", "mania"]
token = os.environ['DISCORD_TOKEN']
#__________________
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('Hello there (>\'w\')>!')

    if message.content.startswith('-mozu beru'):
        await message.channel.send('Mozukudazo loves girls with long blackhair!')

    if message.content.startswith('-mozu roll'):
        randomNum = random.randint(0, 100)
        await message.channel.send("You rolled " + str(randomNum) + "!")
    # using -mozu rs <username>
    if message.content.startswith('-mozu rs'):
        splitted = message.content.split(" ")
        if(splitted[3]):
            mode = modes_Dict[splitted[3]]
        else:
            mode = 0
        readerurl = requests.get(
            "https://osu.ppy.sh/api/get_user?k=a61bebd49e28899f983df7e528940f630665d28b&u={}&m={}".format(splitted[2], mode))
        print(readerurl.json())
        await message.channel.send(readerurl.json())

client.run(token)