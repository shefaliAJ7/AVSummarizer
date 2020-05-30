from transformers import pipeline, AutoModelForTokenClassification, AutoTokenizer
import torch

class Summarization:

    def summarize(self, text, min, max):
        summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
        summary = summarizer(text, min_length=min, max_length=max)
        return summary
