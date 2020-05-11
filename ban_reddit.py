import discord
from difflib import SequenceMatcher, get_close_matches
client = discord.Client()

hate = 'reddit'
hate2 = 'chungus'

@client.event
async def on_ready():
    print("Working.")
    activity = discord.Game(name='I HATE REDDIT >:(')
    await client.change_presence(status=discord.Status.dnd, activity=activity)

@client.event
async def on_message(message):

    
    msglower = message.content.lower()
    seq = SequenceMatcher(a=hate, b=msglower)
    seq2 = SequenceMatcher(a=hate2, b=msglower)
    
    print('Reddit ratio :', seq.ratio())
    print('Chungus ratio :', seq2.ratio())
    print(message.author,":", message.content)
    if 'reddit.com' in msglower or 'redd.it' in msglower:
    	print("CLOSE CALL")
    	return
    elif seq.ratio() >= 0.7000000: # reddit
    	await message.delete()
    	print("REDDIT DETECTED")
    elif seq2.ratio() >= 0.7000000: # chungus
            await message.delete()
            print("CHUNGUS DETECTED")


client.run('TOKEN')
