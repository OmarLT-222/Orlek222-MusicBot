# Orlek222's Music bot
Since a lot of discord music bots are being blocked by youtube nowadays I've decided to write up a quick project that will allow anyone to host their own discord bot. This bot includes the following commands:

/help - Displays all available commands
/p or /play - Finds the song on youtube and plays it.
/q or /queue - Displays the first 5 elements of the queue
/skip or /s - Skips the current song
/clear or /c - Clears the queue
/leave or /l - Disconnects the bot from the voice channel
/pause - Pauses the current song
/resume - Resumes the current song

# Installation
First, you'll need to clone the repo: `git@github.com:OmarLT-222/Orlek222-MusicBot.git`

Then run `pip install -r requirements.txt` to install all of the python dependencies.\

Please note that you will also need to have [ffmpeg](https://ffmpeg.org/download.html) installed and make sure that the path to the bin folder is in your environment variables.

# Running your bot
The simplest way is to execute it like any Python app, just by using `python3 source/main.py`

# Token
Remember that you need to have your token setup in your environment variables, or in another file from which you will be able to import it, which is my case.

# TODO

- [ ] Implement a spotify reproduction functionality

# CREDITS
I made this bot following [this tutorial](https://youtu.be/dRHUW_KnHLs?si=iHYcrUwNcjUkjDF8). I changed some things, as the FFMPEG options so it\
wouldn't have any trouble on playing the songs, and I also used the `yt-dlp` library as `youtube_dl` is deprecated.