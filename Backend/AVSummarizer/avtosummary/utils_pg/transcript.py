from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urljoin,urlparse,parse_qs

class Transcript:

    def __init__(self):
        self.text = "-1"

    def getTranscript(self, link):
        try:
            url_data = urlparse(link)
            query = parse_qs(url_data.query)
            video = query["v"][0]
            transcript_list = YouTubeTranscriptApi.list_transcripts(video)
            transcript = transcript_list.find_transcript(['en'])
            ts = transcript.fetch()
            text = ""
            for t in ts:
                text += t['text']
            self.text = text
        except:
            self.text = "-1"
        return self.text


