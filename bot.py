# Libraries
import discord
import random
import time
import datetime
import os
import json
import urllib.request
import requests
#from
from discord.ext import commands
from discord.ext.tasks import loop
from discord import Streaming
from discord.utils import get
from discord import Forbidden
from discord.ext.commands import Cog
from discord.ext.commands import command
from dotenv import load_dotenv
load_dotenv()
#Views
from views.status import *
from views.react import *
from views.react import on_message
from views.role import *
from views.twitch import *
from views.twitch import get_notifications

# Variables
client = discord.Client()
modes_Dict = {'osu': 0, 'taiko': 1, 'ctb': 2, 'mania': 3}
modes = ["osu", "taiko", "ctb", "mania"]
token = os.environ['DISCORD_TOKEN']
#__________________
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
#__________________

@client.event
async def on_member_update(prev, cur):
    role = discord.utils.get(cur.guild.roles, name="Developer")
    games = ["visual studio code", "pycharm", "webstorm", "phpstorm"]
    
    for member in client.get_all_members():
      if member.game == games[member]:
        if cur.activity and cur.activity.name.lower() in games:
            await cur.add_roles(957687177536483388)
        
      else:
        return
       

#twitch stuff
"""@client.event
async def on_member_update(before, after):
    if not before.activity.type == after.activity.type:
        return
    role = get(after.guild.roles, id=955902434440523796)
    channel = get(after.guild.channels, id=842083343100149801)
    if isinstance(after.activity, Streaming):
        await after.add_roles(role)
        await channel.send(f"{before.mention} is streaming on {activity.platform}: {activity.name}.\nJoin here: {activity.url}") #
    elif isinstance(before.activity, Streaming):
        await after.remove_roles(role)
        await channel.send(f'{after.mention} is no longer streaming!')
    else:
        return
# ______________
bot = commands.Bot(command_prefix="-mozu ")
@bot.command()
async def ping(ctx):
    await ctx.send("pong")
@loop(seconds=90)
async def check_twitch_online_streamers():
    channel = bot.get_channel(842083343100149801)
    if not channel:
        return
    notifications = get_notifications()
    for notification in notifications:
        await channel.send("streamer {} ist jetzt online: {}".format(notification["user_login"], notification))
with open("config.json") as config_file:
    config = json.load(config_file)
if __name__ == "__main__":
    check_twitch_online_streamers.start()
    bot.run(config[token])
"""
# lets the bot run based on the token


client.run(token)
