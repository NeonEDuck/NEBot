from discord.ext import commands
from discord_slash.context import SlashContext, ComponentContext
import traceback

def setup(bot :commands.Bot) -> None:
    
    @bot.event
    async def on_slash_command_error(ctx :SlashContext, ex :Exception) -> None:
        if ex.args and ex.args[0] in ('vote', 'permission'):
            await ctx.send(content=ex.args[1], hidden=True)
        else:
            traceback.print_tb(ex.__traceback__)
            print(ex)

    @bot.event
    async def on_component_callback_error(ctx :ComponentContext, ex :Exception) -> None:
        if ex.args and ex.args[0] in ('vote', 'permission'):
            await ctx.send(content=ex.args[1], hidden=True)
        else:
            traceback.print_tb(ex.__traceback__)
            print(ex)