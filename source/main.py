##-----IMPORTS AND DEFINITIONS-----##

import discord
from discord.ext import commands
import tokens as constants

from helper_cog import HelperCog
from music_cog import music_cog

API_KEY = constants.TOKEN


def main():
    bot = commands.Bot(command_prefix="/")

    bot.remove_command('help')
    bot.add_cog(music_cog(bot))
    bot.add_cog(HelperCog(bot))

    bot.run(API_KEY)


main()
