import torch
import json
from transformers import pipeline


class Summarization:

    def __init__(self):
        self.summary = "-1"
        # self.model = LongformerForMaskedLM.from_pretrained("longformer-base-4096")
        # self.tokenizer = LongformerTokenizer.from_pretrained("longformer-base-4096")

        self.device = torch.device('cpu')

    def summarize(self, text, min, max):
        print('Text', text)
        print('Min and Max',min, max)
        try:
            preprocess_text = text.strip().replace("\n","")
            # t5_prepared_Text = "summarize: "+preprocess_text
            #
            # tokenized_text = self.tokenizer.encode(t5_prepared_Text, return_tensors="pt", truncation_strategy='longest_first', max_length=4096).to(self.device)
            # summary_ids = self.model.generate(tokenized_text,
            #                              num_beams=4,
            #                              no_repeat_ngram_size=2,
            #                              min_length=int(min),
            #                              max_length=int(max),
            #                              early_stopping=True)
            #
            # output = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            text = text[:1024]
            summarizer = pipeline(task="summarization")
            if int(max) < int(min):
                min, max = max, min
            summary = summarizer(text, max_length=int(max), min_length=int(min))
            print("Summary", summary[0]['summary_text'])
            return summary[0]['summary_text']
        except:
            return "Some Internal Error Happened"

    def improve(self, summary):
        indi_parts = summary.split('.')
        indi_parts.pop()
        summary = '. '.join(indi_parts)
        self.summary = summary + "."
        return self.summary


