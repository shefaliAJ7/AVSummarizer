import os
import sys
from flask import Flask, request, jsonify, Blueprint

from AVSummarizer.avtosummary.utils import AVSummary_Utils

avtosummary = Blueprint('avtosummary',__name__)

@avtosummary.route('/api/summarize', methods=['POST'])
def get_summarization_of_avlink():
    try:
        avlink = request.json['avlink']
        utils = AVSummary_Utils()
        print(avlink)
        if utils.isAVLinkValid(avlink):
            audio_file_path, audio_filename = utils.av_to_audio(avlink)

            if utils.isAudioFileValid(audio_file_path):
                text = utils.audio_to_text(audio_file_path, audio_filename)

                if utils.isTextValid(text):
                    summary = utils.text_to_summary(text)
                    print('summary', summary)
                    if utils.isSummaryValid(summary):
                        message = {
                            "text": text,
                            "summary": summary,
                            "message": "No error"
                        }
                        return jsonify(message), 200
                    message = {
                        "text": text,
                        "summary": "",
                        "message": "Summary could not be generated"
                    }
                    return jsonify(message), 500
                message = {
                    "text": "",
                    "summary": "",
                    "message": "Text and Summary could not be generated"
                }
                return jsonify(message), 500
            else:
                message = {
                    "text": "",
                    "summary": "",
                    "message": "AudioFile could not be generated"
                }
                return jsonify(message), 500
        message = {
            "text": "",
            "summary": "",
            "message": "Link Broken"
        }
        return jsonify(message), 400
    except:
        message = {
            "message": "Internal Server Error, something went wrong"
        }
        return jsonify(message), 500