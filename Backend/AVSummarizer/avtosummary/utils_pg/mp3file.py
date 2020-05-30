from __future__ import unicode_literals
import youtube_dl
import re

class Mp3File:

    def convertToMp3(self, link):

        loc = link
        loc = loc.split('/')
        video_name = loc[-1]
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': '/Users/adityarohilla/Personal/AVSummarizer/Backend/AVSummarizer/resources/Mp3Files/' + video_name + '.mp3'
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([link])
                return True
            except:
                return False
