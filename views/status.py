# Libraries
import discord
import os
import urllib.request
import requests
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
token = os.environ['DISCORD_TOKEN']
client = discord.Client()

#__________________
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#welcome message

@client.event
async def on_member_join(member):
    guild = client.get_guild(837894069929508894) # YOUR INTEGER GUILD ID HERE
    welcome_channel = guild.get_channel(837894069929508897) # YOUR INTEGER CHANNEL ID HERE
    advice_channel = guild.get_channel(847874263205675028)
    role = guild.get_role(839338894997979176) # YOUR INTEGER ROLE ID HERE FOR THE ROLE YOU WANT TO GIVE
    await member.add_roles(role)
    await welcome_channel.send(f'Welcome to the {guild.name}, {member.mention} <a:YayyyyRainbow:856384905705553951>, check <#{847874263205675028}> to add your own specific roles! :heart:') #\:emoji-name: <-- in discord chat
    await member.send(f'We are glad to have you in the {guild.name} , {member.name} !  :partying_face:')
#__________________________________________________________________________

#Discord Status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='Osu!', url='https://www.twitch.tv/mozukudazo'))

    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    #print("{0.user} is now online!".format(client))
    return
#___________________________________________________________________________

client.run(token)
# lets the bot run based on the token


