import discord
from difflib import SequenceMatcher, get_close_matches

client = discord.Client()

hate = 'reddit'
hate2 = 'chungus'

@client.event
async def on_ready():
    print("Working.")

@client.event
async def on_message(message):

    
    msglower = message.content.lower()
    seq = SequenceMatcher(a=hate, b=msglower)
    seq2 = SequenceMatcher(a=hate2, b=msglower)
    
    print(seq.ratio())
    print(seq2.ratio())
    print(message.author,":", message.content)
    if 'reddit.com' in msglower or 'redd.it' in msglower:
    	print("CLOSE CALL")
    	return
    if seq.ratio() >= 0.7000000:
    	await message.delete()
    	print("REDDIT DETECTED")
    if seq2.ratio() >= 0.7000000:
            await message.delete()
            print("REDDIT DETECTED")


client.run('token-here')
