
import discord
client = discord.Client()

from iteration import *

@client.event
async def on_ready():
    print("Working.")

@client.event
async def on_message(message):
    msglower = message.content.lower()
    print(message.author,":", message.content)
    if 'reddit.com' in msglower or 'redd.it' in msglower:
    	print("CLOSE CALL")
    elif msglower or message.content() in list:
    	await message.delete()
    	print("REDDIT DETECTED")
    	

client.run('Token here')
