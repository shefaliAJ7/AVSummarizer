import os
import boto3
import time
import requests

from datetime import date
from botocore.exceptions import NoCredentialsError
from botocore.client import Config as ConfigAWS
from werkzeug.utils import secure_filename

from AVSummarizer.avtosummary.config import Config

class Transcribe:

    filename = ""
    s3link = ""
    converted_text = ""
    text_stats = []

    def store_file_in_s3(self, complete_file_path):
        folder_name = date.today()
        s3 = boto3.resource(
            's3',
            aws_access_key_id=Config.ACCESS_KEY_ID,
            aws_secret_access_key=Config.ACCESS_SECRET_KEY,
            config=ConfigAWS( signature_version='s3v4' )
        )
        try:
            s3.Bucket( Config.BUCKET_NAME ).upload_file( complete_file_path, '%s/%s' % (folder_name, self.filename) )
            s3Link = "s3://" + Config.BUCKET_NAME + "/" + str( folder_name ) + "/" + self.filename
            self.s3link = s3Link
        except FileNotFoundError:
            print( "Error: The file was not found" )
        except NoCredentialsError:
            print( "Error: Credentials not available" )


    def aws_voice_to_text(self):
        transcribe = boto3.client(
            'transcribe',
            region_name="us-west-2",
            aws_access_key_id=Config.ACCESS_KEY_ID,
            aws_secret_access_key=Config.ACCESS_SECRET_KEY
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
