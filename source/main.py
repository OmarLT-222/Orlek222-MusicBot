##-----IMPORTS AND DEFINITIONS-----##
import asyncio

import discord
from discord.ext import commands
import tokens as constants

from helper_cog import HelperCog
from music_cog import music_cog

API_KEY = constants.TOKEN

async def setup():
    print("Setting up bot...")
    bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

    bot.remove_command('help')
    await bot.add_cog(music_cog(bot))
    await bot.add_cog(HelperCog(bot))

    return bot

if __name__ == "__main__":
    bot = asyncio.run(setup())
    print("Starting bot...")
    bot.run(API_KEY)



