import discord 
import os
from discord.ext import commands
from discord.ext.tasks import loop
from discord import Streaming
from discord.utils import get
from discord import Forbidden
from discord.ext.commands import Cog
from discord.ext.commands import command
from dotenv import load_dotenv
load_dotenv()
token = os.environ['DISCORD_TOKEN']

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix=',', intents=intents)

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
       
"""@client.event 
async def on_member_join(member):
  role = get(member.guild.roles, id=839338894997979176)
  await member.add_roles(role)
"""
#this should be the right code (implement it on monday or when I have free time)
"""@client.event
async def on_member_update(prev, cur):
    role = discord.utils.get(cur.guild.roles, name="Developer")
    games = ["visual studio code", "pycharm", "webstorm", "phpstorm"]
    # make sure game titles are lowercase

    if cur.activity and cur.activity.name.lower() in games:
            await cur.add_roles(957687177536483388)"""

client.run(token)
