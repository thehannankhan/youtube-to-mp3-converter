#!/bin/env python
# Requires: youtube_dl module & ffmpeg
# Usage: python youtube2mp3.py <URL>, ...
# Example: python youtube2mp3.py https://www.youtube.com/watch?v=xuCO7-DLCaA&ab_channel=LR1
import youtube_dl
import sys

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


if __name__ == "__main__":
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        filenames = sys.argv[1:]
        ydl.download(filenames)