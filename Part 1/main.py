import discord
from discord.ext import commands, tasks
import os

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
	print('Bot is Online')

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


#Create a .env file and write TOKEN={YOUR TOKEN HERE}
client.run(os.getenv('TOKEN'))