import torch
import json
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config


class Summarization:

    def __init__(self):
        self.summary = "-1"
        self.model = T5ForConditionalGeneration.from_pretrained('t5-small')
        self.tokenizer = T5Tokenizer.from_pretrained('t5-small')
        self.device = torch.device('cpu')

    def summarize(self, text, min, max):
        try:
            preprocess_text = text.strip().replace("\n","")
            t5_prepared_Text = "summarize: "+preprocess_text
            tokenized_text = self.tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(self.device)
            summary_ids = self.model.generate(tokenized_text,
                                         num_beams=4,
                                         no_repeat_ngram_size=2,
                                         min_length=min,
                                         max_length=max,
                                         early_stopping=True)

            output = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            self.summary = output
        except:
            self.summary = "-1"

    def improve(self):
        if self.summary == "-1":
            return self.summary
        indi_parts = self.summary.split('.')
        indi_parts.pop()
        summary = '. '.join(indi_parts)
        self.summary = summary + "."
        return self.summary


