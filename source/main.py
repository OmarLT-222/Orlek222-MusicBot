##-----IMPORTS AND DEFINITIONS-----##

import discord
from discord.ext import commands
import tokens as constants

from helper_cog import HelperCog
from music_cog import music_cog

API_KEY = constants.TOKEN

print("Starting Bot...")
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

bot.remove_command('help')
bot.add_cog(music_cog(bot))
bot.add_cog(HelperCog(bot))

bot.run(API_KEY)
