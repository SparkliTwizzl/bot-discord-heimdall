##import discord
##import os
##from discord.ext import commands
##
##
##prefix = ['%']
##client = discord.Client()
##bot = commands.Bot(prefix)
##
##changePrefixCommand = 'prefix'
##
##
##def IsMessageStaticCommand(message, command):
##    return message.content == prefix + command
##
##
##def IsMessageDynamicCommand(message, command):
##    command = prefix + command
##    if len(message.content) > len(command):
##        return message.content.startswith(command + ' ')
##    else:
##        return message.content.startswith(command)
##
##def GetCommandArgumentList(message, command):
##    return message.content[len(prefix + command + ' '):]
##
##
##@client.event
##async def on_ready():
##    print('logged in as {0.user}'.format(client))
##
##@client.event
##async def on_message(message):
##    if message.author == client.user:
##        return
##
##    if message.content == '/heimdall-prefix':
##        await message.channel.send('prefix is set to ' + prefix)
##
####    if IsMessageCommand(message, changePrefixCommand):
####        await message.channel.send(message.content[len(prefix + changePrefixCommand + ' '):])
####        messagePrefix = message.content[len(prefix)+len(changePrefixCommand):]
####        await message.channel.send('changed command prefix to \"'+prefix+'\"')
##
##    if IsMessageDynamicCommand(message, changePrefixCommand):
##        prefix = GetCommandArgumentList(message, changePrefixCommand)
##        await message.channel.send('changed command prefix to ' + prefix)
##
##    if IsMessageStaticCommand(message, 'oi cunt'):
##        await message.channel.send('nah fuck you leave me alone')
##
##
##client.run(os.getenv('BOT_DISCORD_HEIMDALL_TOKEN'))




import interactions
import os


prefix = '%'
bot = interactions.Client(token=os.getenv('BOT_DISCORD_HEIMDALL_TOKEN'))


@bot.command(
    name='heimdall-prefix',
    description='remind me what Heimdall\'s command prefix is set to',
)
async def test_command(ctx: interactions.CommandContext):
    await ctx.send('prefix is set to ' + prefix)

bot.start()
