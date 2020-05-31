from transformers import pipeline

class Summarization:

    def __init__(self):
        self.summary = "-1"

    def summarize(self, text, min, max):
        summarizer = pipeline("summarization", model="t5-base", tokenizer="t5-base", framework="tf")
        summary = summarizer(text, min_length=min, max_length=max)
        return summary

    def improve(self, summary):
        indi_parts = summary.split('.')
        indi_parts.pop()
        summary = '.'.join(indi_parts)
        self.summary = summary
        return self.summary
