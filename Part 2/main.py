import discord
from discord.ext import commands, tasks
import os

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
	print('Bot is Online')

@client.event
async def on_message(message):
  	if author == client.user:
		pass
	if message.content.startswith('hello'):
		await message.channel.send('Hello There!')

@client.event
async def on_message_delete(message):
	author = message.author
	content = message.content
	channel = message.channel
	if author == client.user:
		pass
	else:
		await channel.send(f'{author}: {content}')

@client.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


#Create a .env file and write TOKEN={YOUR TOKEN HERE}
client.run(os.getenv('TOKEN'))
