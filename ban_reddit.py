# DOWN WITH REDDIT
# a simple discord bot
# that filters everything to do
# w i t h  r e d d i t 

import discord
client = discord.Client()

list = [
'reddit', 'chungus', 'redddit', 'readit', 'rediit', 'chunguus', 'chhungus', 'chunggus', 'chungggus', 'reddi t','r e d d i t', 'chungūs', 'red dit', 'red it', 'red dirt', 'roadit', 'redd it'] 

@client.event
async def on_ready():
    print('Working.')

@client.event
async def on_message(message):
    msglower = message.content.lower()
    print(message.author,':', message.content)
    if 'reddit.com' in msglower or 'redd.it' in msglower:
    	print('CLOSE CALL')
    elif msglower in list:
    	await message.delete()
    	print('REDDIT DETECTED')
    	

client.run('token-here')
