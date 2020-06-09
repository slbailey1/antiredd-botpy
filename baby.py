import discord
client = discord.Client()


list1 = ['baby!','hes baby',"I'm Baby!",'baby','<:ImBaby:711344078167605329>', "I'm baby!", 'im baby', "I'm baby", "im baby!", '<:baby:718526936552439899>'] 
list2 = ['we are baby', '<@&718234473753477150>']

@client.event
async def on_ready():
    print("Working.")
    activity = discord.Game(name="baby!")
    await client.change_presence(status=discord.Status.dnd, activity=activity)

@client.event
async def on_message(message):

    
    msglower = message.content.lower()
    channel = client.get_channel(683509801984196826)
    
    
    print(message.author,":", msglower)
    
    
    if msglower in list1:
        await channel.send("I'm baby!<:ImBaby:711344078167605329>", tts=True)
        return
    elif msglower in list2:
        await channel.send("We are baby.<:ImBaby:711344078167605329>", tts=True)
        return
               
            

 
client.run('NzA5MTQxNjE0MjY5OTU2MTQ3.Xrmpmg.7Y7Msd3_K-Vyd8TBCzKhhMjMvdo')
