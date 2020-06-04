import boto
import re
import os
from AVSummarizer.config import Config
from AVSummarizer.avtosummary.utils_pg.audiofile import AudioFile
from AVSummarizer.avtosummary.utils_pg.transcribe import Transcribe
from AVSummarizer.avtosummary.utils_pg.summarization import Summarization

class AVSummary_Utils:

    def __init__(self):
        self.toAudio = AudioFile()
        self.toText = Transcribe()
        self.toSummary = Summarization()

    def isAVLinkValid(self, avlink):
        regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        if re.match(regex, avlink) is not None:
            return True

        return False

    def isAudioFileValid(self, audio_file):
        if os.path.exists(audio_file):
            return True
        return False

    def isTextValid(self, text):
        if text != "-1":
            return True
        return False

    def isSummaryValid(self, summary):
        if summary != "-1":
            return True
        return False

    def av_to_audio(self, avlink):
        self.toAudio.convertToAudio(avlink)
        return self.toAudio.change_media()

    def audio_to_text(self, audio_file_path, audio_filename):
        self.toText.filename = audio_filename
        self.toText.save_audio_in_s3(audio_file_path)
        text = self.toText.transcribe_audio()
        os.remove( audio_file_path )
        return text

    def text_to_summary(self, text):
        self.toSummary.summarize(text, 5, 100)
        return self.toSummary.improve()
