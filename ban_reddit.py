import discord
client = discord.Client()

@client.event
async def on_ready():
    print('Working.')

@client.event
async def on_message(message):
    msglower = message.content.lower()
    print(message.author,':', message.content)
    if 'reddit.com' in msglower or 'redd.it' in msglower:
    	return
    elif 'reddit' in msglower or 'chungus' in msglower:
    	await message.delete()
    	print('REDDIT DETECTED')

client.run('token')
