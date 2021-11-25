


# CODE IN DESCRIPTION












import discord
from discord.ext import commands
from discord import Intents

PREFIX = '?'

intents = Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

bot.remove_command('help')

@bot.event
async def on_ready():
	print('Connected')
	
@bot.command(pass_context=True)
async def hello(ctx):
	await ctx.send('Hi!')
	
TOKEN = open('token.txt', 'r').readline() #Token in https://discord.com/developers/applications but create a application, and in Bot add bot, then go to OAuth2, URL Generator, and select: bot (up), administrator (down) or other, and copy. And join on your invite link, add him, and go to Token, and cope the token, your token paste in token.txt. In Termux send: cd /storage/emulated/0/ your way. And: pkg install python (y if will be question), pip install python, python bot.py for start.

bot.run(TOKEN)