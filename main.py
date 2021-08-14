from threading import Thread
from flask import Flask, jsonify
import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.context import SlashContext, ComponentContext
from variable import TOKEN
import error_handler
import app

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(intents=intents, command_prefix='imd/')
slash = SlashCommand(bot, sync_commands=True)
extensions = ['cogs.vote']

@slash.slash(name='ping')
async def _ping(ctx:SlashContext):
    await ctx.send(f'Pong! ({bot.latency*1000}ms)', hidden=True)

if __name__ == '__main__':
    error_handler.setup(bot)
    server = Thread(target=app.run)
    server.start()

    for ext in extensions:
        bot.load_extension(ext)

    bot.run(TOKEN)