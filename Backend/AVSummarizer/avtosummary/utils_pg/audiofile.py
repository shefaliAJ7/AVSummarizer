from __future__ import unicode_literals
import youtube_dl
import re
import time
import os

from pydub import AudioSegment

from AVSummarizer.config import Config

upload_folder = Config.UPLOAD_FOLDER

class AudioFile:

    def __init__(self):
        self.complete_file_path = ""
        self.filename = ""

    def convertToAudio(self, link):

        timestamp = time.strftime('%Y%m%d%H%M%S')
        self.filename = 'file_' + timestamp + '.mp3'
        output_file_path = upload_folder + self.filename
        ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': output_file_path
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([link])
                self.complete_file_path = output_file_path
                return self.complete_file_path, self.filename
            except:
                print("Couldn't download video and convert it into mp3")

    def change_media(self, complete_file_path, filename):
        wav_audio = AudioSegment.from_file( complete_file_path )
        os.remove( complete_file_path )
        newfilename = os.path.splitext( filename )[0]
        wav_audio.export( upload_folder + newfilename + ".wav", format="wav" )
        self.filename = newfilename + ".wav"
        self.complete_file_path = upload_folder + self.filename
        return self.complete_file_path, self.filename

