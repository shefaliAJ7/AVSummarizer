import os
import boto3
import time
import requests

from datetime import date
from botocore.exceptions import NoCredentialsError
from botocore.client import Config as ConfigAWS
from werkzeug.utils import secure_filename

from AVSummarizer.config import Config

aws_access_key_id = Config.ACCESS_KEY_ID
aws_access_secret_key = Config.ACCESS_SECRET_KEY
aws_bucket_name = Config.BUCKET_NAME

class Transcribe:

    def __init__(self):
        self.filename = ""
        self.s3link = ""
        self.converted_text = "-1"
        self.text_stats = []

    def save_audio_in_s3(self, complete_file_path):
        s3 = boto3.resource(
            's3',
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_access_secret_key,
            config=ConfigAWS( signature_version='s3v4' )
        )
        try:
            s3.Bucket( aws_bucket_name ).upload_file( complete_file_path, '%s' % (self.filename) )
            s3Link = "s3://" + aws_bucket_name + "/" + self.filename
            print(s3Link)
            return s3Link
        except FileNotFoundError:
            print( "Error: The file was not found" )
            return ""
        except NoCredentialsError:
            print( "Error: Credentials not available" )
            return ""

    def transcribe_audio(self, s3link):
        self.s3link = s3link

        print(self.s3link)

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
            MediaFormat='wav',
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

        # delete the file in s3
        if len(self.converted_text) > 0:
            s3 = boto3.resource(
                's3',
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_access_secret_key,
                config=ConfigAWS( signature_version='s3v4' )
            )
            s3.Object(aws_bucket_name, self.filename).delete()


        print(self.converted_text)
        return self.converted_text
