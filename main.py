import discord
import interactions
import os


bot = interactions.Client(token=os.getenv('BOT_DISCORD_HEIMDALL_TOKEN'))


@bot.command(
    name='heimdall-help',
    description='what the hell is anything',
)
async def heimdall(ctx: interactions.CommandContext):
    await ctx.send('fuck you i aint wrote the help yet')


@bot.command(
    name='fuck',
    description='fuck you tony',
    options = [
        interactions.Option(
            name='who',
            description='whomst\'ve fucked em',
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ]
)
async def fuck(ctx: interactions.CommandContext, who: str):
    await ctx.send('nah fuck YOU ' + who)


@bot.command(
    name='achoo',
    description='mothafucka it\'s your mothafucken birthday',
    options = [
        interactions.Option(
            name='role1',
            description='role to assign',
            type=interactions.OptionType.ROLE,
            required=True,
        ),
    ]
)
async def achoo(ctx: interactions.CommandContext, role1: str):
    member = ctx.author
    print(member)
    await ctx.send(f'member: {member.mention}')
    role = discord.utils.get(lambda role: role.name == role1, ctx.guild.roles)
    print(role1)
    await ctx.send(f'role: {role}')
    await user.add_roles(role)


bot.start()
