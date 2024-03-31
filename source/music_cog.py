import configparser

import discord
from discord.ext import commands
from youtube_dl import YoutubeDL

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.isplaying = False;
        self.ispaused = False;

        self.music_queue = [];
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': True}
        self.ffmpeg_options = {'before_options': '-reconnect 1 -reconnect_streamed 1'}

        self.vc = None

    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception as e:
                return False
        return {'source': info['formats'[0]['url']], 'title': info['title']}
    def play_next_song(self):
        if len(self.music_queue) > 0:
            self.isplaying = True

            m_url = self.music_queue[0][0]['source']

            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.ffmpeg_options), after=lambda e: self.play_next_song())
        else:
            self.isplaying = False