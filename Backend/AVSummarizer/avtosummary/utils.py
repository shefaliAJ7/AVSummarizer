import boto
import re
from AVSummarizer.config import Config
from AVSummarizer.avtosummary.utils_pg.mp3file import Mp3File
from AVSummarizer.avtosummary.utils_pg.transcribe import Transcribe
from AVSummarizer.avtosummary.utils_pg.summarization import Summarization

class AVSummary_Utils:

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
        else:
            return False
    def isMp3FileValid(self, mp3file):
        return True

    def isTextValid(self, text):
        pass

    def isSummaryValid(self, summary):
        pass

    def av_to_mp3(self, avlink):
        toMp3 = Mp3File()
        if toMp3.convertToMp3(avlink):
            loc = avlink.split('/')
            video_name = loc[-1]
            return video_name
        else:
            return ''


    def mp3_to_text(self, mp3_file_path):
        pass
        transcribe = Transcribe()
        transcribe.save_mp3_in_s3(mp3_file_path)
        return transcribe.transcribe_mp3()

    def text_to_summary(self, text):
        pass

"""
import os
import boto3
import time
import requests

from datetime import date
from botocore.exceptions import NoCredentialsError
from botocore.client import Config as ConfigAWS
from werkzeug.utils_pg import secure_filename

aws_access_key_id = "AKIAVR2JSCFVAVI34XFX"
aws_access_secret_key = "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"
aws_bucket_name = "avsummarizer"
uploadFolder = os.path.abspath(os.path.dirname(__file__)) \
    +'/resources/FileUploads/'

class UploadedFile:

    filename = ''
    s3link = ''

    def upload_file_in_server(self, file):
        if not os.path.isdir(uploadFolder):
            os.mkdir(uploadFolder)
        self.filename = secure_filename(file.filename)
        destination = "/".join([uploadFolder, self.filename])
        file.save(destination)
        return destination

    def store_file_in_s3(self, complete_file_path):
        folder_name = date.today()
        s3 = boto3.resource(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_access_secret_key,
            config=ConfigAWS(signature_version='s3v4')
        )
        try:
            s3.Bucket(aws_bucket_name).upload_file(complete_file_path, '%s/%s' % (folder_name, self.filename))
            s3Link = "s3://" + aws_bucket_name + "/" + str(folder_name) + "/" + self.filename
            self.s3link = s3Link
        except FileNotFoundError:
            print("Error: The file was not found")
        except NoCredentialsError:
            print("Error: Credentials not available")


class Transcribe:

    filename = ""
    s3link = ""
    converted_text = ""
    text_stats = []

    def aws_voice_to_text(self):
        transcribe = boto3.client(
            'transcribe',
            region_name="us-west-2",
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_access_secret_key
        )

        JOB_NAME = self.filename
        try:
            transcribe.delete_transcription_job(TranscriptionJobName=JOB_NAME)
        except:
            print("Job is not available")

        transcribe.start_transcription_job(
            TranscriptionJobName=JOB_NAME,
            Media={'MediaFileUri': self.s3link},
            MediaFormat='mp3',
            LanguageCode='en-US'
        )
        while True:
            status = transcribe.get_transcription_job(TranscriptionJobName=JOB_NAME)
            if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
                break
            time.sleep(5)

        text_uri = status.get("TranscriptionJob").get("Transcript").get("TranscriptFileUri")

        # Retrieve the text
        audio_text = requests.get(url=text_uri)
        data = audio_text.json()

        # Voice to text -> can display in frontend
        self.text_stats = data['results']['items']
        self.converted_text = data['results']['transcripts'][0]['transcript']

        # delete the job
        transcribe.delete_transcription_job(TranscriptionJobName=JOB_NAME)
"""
