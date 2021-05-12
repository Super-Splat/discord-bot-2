import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('deez'):
      
        await message.channel.send('deez <@393214572942852099>')
    

client.run('ODQxNzg3Nzk4NjkyNTYwODk2.YJr1-g.xR21jFM7Jfx-2zXVps4YdGgAtkM')