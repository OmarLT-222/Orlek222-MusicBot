import discord
from discord.ext import commands

class HelperCog(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.help_message = """
```
General commands:
/help - Displays all available commands
/p or /play - Finds the song on youtube and plays it.
/q or /queue - Displays the first 5 elements of the queue
/skip or /s - Skips the current song
/clear or /c - Clears the queue
/leave or /l - Disconnects the bot from the voice channel
/pause - Pauses the current song
/resume - Resumes the current song
```
"""

        self.text_channel_text = []
    @commands.Cog.listener()
    async def on_ready(self):
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                self.text_channel_text.append(channel)

        await self.send_to_all(self.help_message)

    async def send_to_all(self, msg):
        for text_channel in self.text_channel_text:
            await text_channel.send(msg)

    @commands.command(name = "help", help = "Displays all available commands")
    async def help(self, ctx):
        await ctx.send(self.help_message)