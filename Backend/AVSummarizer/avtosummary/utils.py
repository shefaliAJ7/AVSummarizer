import boto
import re
import os
from AVSummarizer.avtosummary.utils_pg.transcript import Transcript
from AVSummarizer.avtosummary.utils_pg.summarization import Summarization

class AVSummary_Utils:

    def __init__(self):

        self.toText = Transcript()
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



    def isTextValid(self, text):
        if text != "-1":
            return True
        return False

    def isSummaryValid(self, summary):
        if summary != "-1":
            return True
        return False

    def av_to_text(self, avlink):
        text = self.toText.getTranscript(avlink)
        return text



    def text_to_summary(self, text, max, min):
        summary = self.toSummary.summarize(text, min, max)
        return self.toSummary.improve(summary)
