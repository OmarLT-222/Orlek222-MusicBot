import discord
from discord.ext import commands
import yt_dlp

class music_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.isplaying = False
        self.ispaused = False

        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': True}
        self.ffmpeg_options = dict(options='-vn')

        self.vc = None

    def search_yt(self, item):
        with yt_dlp.YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception as e:
                return False
        return {'source': info["url"], 'title': info['title']}

    def play_next_song(self):
        if len(self.music_queue) > 0:
            self.isplaying = True

            m_url = self.music_queue[0][0]['source']

            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.ffmpeg_options), after=lambda e: self.play_next_song())
        else:
            self.isplaying = False

    async def play_song(self, ctx):
        if len(self.music_queue) > 0:
            self.isplaying = True
            m_url = self.music_queue[0][0]['source']

            if self.vc == None or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()

                if self.vc == None:
                    await ctx.send("Could not connect to voice channel")
                    return
            else:
                await self.vc.move_to(self.music_queue[0][1])
            self.music_queue.pop(0)
            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.ffmpeg_options), after=lambda e: self.play_next_song())
        else:
            self.isplaying = False

    @commands.command(name="play", aliases = ["p"], help = "Plays a song")
    async def play(self, ctx, *args):
        query = " ".join(args)
        voice_channel = ctx.author.voice.channel
        if voice_channel == None:
            await ctx.send("Connect to a voice channel")
        elif self.ispaused:
            self.vc.resume()
        else:
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("Could not download the song, try a different keyword")
            else:
                await ctx.send("Song added to queue")
                self.music_queue.append([song, voice_channel])

                if not self.isplaying:
                    await self.play_song(ctx)

    @commands.command(name="pause", help = "Pauses the current song")
    async def pause(self, ctx, *args):
        if self.isplaying:
            self.isplaying = False
            self.ispaused = True
            self.vc.pause()
        elif self.ispaused:
            self.isplaying = True
            self.ispaused = False
            self.vc.resume()

    @commands.command(name="resume", aliases =["r"], help="Resumes the current song")
    async def pause(self, ctx, *args):
        if self.ispaused:
            self.isplaying = True
            self.ispaused = False
            self.vc.resume()

    @commands.command(name="skip", aliases =["s"], help="Skips the current song")
    async def skip(self, ctx, *args):
        if self.vc != None and self.vc:
            self.vc.stop()
            await self.play_song(ctx)

    @commands.command(name="queue", aliases=["q"], help="Shows the 5 first elements in queue")
    async def queue(self, ctx, *args):
        queue = ""
        for i in range(0, len(self.music_queue)):
            if i>5: break
            queue += self.music_queue[i][0]['title'] + '\n'
        if queue != "": await ctx.send(queue)
        else: await ctx.send("No songs in queue")

    @commands.command(name="clear", aliases=["c"], help="Clears the queue")
    async def clear(self, ctx, *args):
        if self.vc != None and self.isplaying:
            self.vc.stop()
        self.music_queue.clear()
        await ctx.send("Queue cleared")

    @commands.command(name="leave", aliases=["l"], help="Kick the bot from the voice channel")
    async def leave(self, ctx, *args):
        self.isplaying = False
        self.ispaused = False
        await self.vc.disconnect()
