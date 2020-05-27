import os
from flask import Flask, request, jsonify, Blueprint

from utils import AVSummary_Utils

avtosummary = Blueprint('avtosummary',__name__)

@avtosummary.route('/api/summarize', methods=['GET'])
def get_summarization_of_avlink():
    try:
        avlink = request.json['avlink']
        utils = AVSummary_Utils()

        if utils.isAVLinkValid(avlink):
            mp3 = utils.avlink_to_mp3(avlink)

            if utils.isMP3FileValid(mp3):
                text = utils.mp3_to_text(mp3)

                if utils.isTextValid(text):
                    summary = utils.text_to_summary(text)

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
            message = {
                "text": "",
                "summary": "",
                "message": "Mp3File could not be generated"
            }
            return jsonify(message), 500
        message = {
            "text": "",
            "summary": "",
            "message": "AVLink given is not valid or broken"
        }
        return jsonify(message), 400
    except:
        message = {
            "message": "Internal Server Error, something went wrong"
        }
        return jsonify( message), 500

"""
@app.route('/upload_file', methods=['POST'])
def upload_file_in_s3():
    try:
        if 'file' not in request.files:
            message = {
                "message": "file value not found in the request"
            }
            return jsonify(message), 400
        file = request.files['file']
        if file:
            uf = UploadedFile()
            file_complete_path = uf.upload_file_in_server(file)
            uf.store_file_in_s3(file_complete_path)
            os.remove(file_complete_path)
            message = {
                "filename": uf.filename,
                "s3link": uf.s3link
            }
            return jsonify(message), 200
        else:
            message = {
                "message": "File not found"
            }
            return jsonify(message), 404
    except:
        message = {
            "message": "Internal Server Error, something went wrong"
        }
        return jsonify(message), 500


@app.route('/get_text', methods = ['POST'])
def get_text():
    try:
        filename = request.json['filename']
        s3link = request.json['s3link']

        transcribe = Transcribe()

        transcribe.filename = filename
        transcribe.s3link = s3link

        if len(filename) > 0 and len(s3link) > 0:
            transcribe.aws_voice_to_text()
            message = {
                "text": transcribe.converted_text,
                "stats": transcribe.text_stats
            }
            return jsonify(message), 200
        else:
            message = {
                "message": "File not found in our records"
            }
            return jsonify(message), 404
    except:
        message = {
            "message": "Internal Server Error, something went wrong"
        }
        return jsonify(message), 500
"""
