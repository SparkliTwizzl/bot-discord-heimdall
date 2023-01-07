import interactions
import os


class bot_heimdall:

    bot = interactions.Client(token=os.getenv("BOT_DISCORD_HEIMDALL_TOKEN")) # any machine without token saved as environment variable cant run the bot


    # basic message-based command
    # @bot.command(
    #     name="heimdall-message-command",
    #     description="description",
    # )
    # async def heimdall_message_command(ctx: interactions.CommandContext):
    #     await ctx.send("message command invoked")


    # context menu command (right click menu)
    # @bot.command(
    #     type=interactions.ApplicationCommandType.USER,
    #     name="heimdall-context-menu-command"
    # )
    # async def heimdall_context_menu_command(ctx):
    #     await ctx.send(f"context menu command invoked on user {ctx.target.user.username}")


    # SelectMenu component command
    @bot.command(
        type=interactions.SelectMenu,
        name="heimdall-select-menu-command"
    )
    async def heimdall_select_menu_command(ctx):
        menuOption0 = interactions.SelectOption(
            label="option 0",
            custom_id="option0"
        )
        menuOption1 = interactions.SelectOption(
            label="option 1",
            custom_id="option1"
        )
        menu = interactions.SelectMenu(
            components=[menuOption0, menuOption1]
        )
        await ctx.send("SelectMenu command invoked", components=menu)


    bot.start()
