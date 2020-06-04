import os
import sys
from flask import Flask, request, jsonify, Blueprint

from AVSummarizer.avtosummary.utils import AVSummary_Utils

avtosummary = Blueprint('avtosummary',__name__)

@avtosummary.route('/api/summarize', methods=['POST'])
def get_summarization_of_avlink():

    avlink = request.json['avlink']
    max = request.json['max']
    min = request.json['min']
    utils = AVSummary_Utils()
    print(avlink)
    if utils.isAVLinkValid(avlink):
        text = utils.av_to_text(avlink)

        if utils.isTextValid(text):
            summary = utils.text_to_summary(text, max, min)
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
        else:
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
            "message": "Link is invalid"
        }
        return jsonify(message), 500