import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('NTM2NjY4NDY3NzY0Mzk2MDU3.GffIMu.BdYYY2k13L0D1y-_R9pdeZVyszg1t0St-iCbqY')
