import interactions
import os


bot = interactions.Client(token=os.getenv("BOT_DISCORD_HEIMDALL_TOKEN")) # any machine without token saved as environment variable cant run the bot


# basic message-based command
# @bot.command(
#     name="heimdall-message-command",
#     description="description",
# )
# async def heimdall_help(ctx: interactions.CommandContext):
#     await ctx.send("response")

# context menu command (right click menu)
# @bot.command(
#     type=interactions.ApplicationCommandType.USER,
#     name="heimdall-context-menu-command"
# )
# async def test(ctx):
#     await ctx.send(f"context menu command invoked on user {ctx.target.user.username}")


bot.start()
