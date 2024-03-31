import discord
from discord.ext import commands
import dismusic
import os
import tokens as constants

API_KEY = constants.TOKEN

bot = commands.Bot(command_prefix="/")


def main():
    bot.run(API_KEY)