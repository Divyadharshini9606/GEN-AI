# -*- coding: utf-8 -*-
"""que_to_ans.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_No_VwXKuCcGNKTvyN2rKJ2WJYmSqAqF
"""

import pandas as pd
from transformers import pipeline

df = pd.read_csv("/content/drive/MyDrive/eiffel_dataset.csv")
context = df.loc[0, "context"]

print("\n Eiffel Tower Context Loaded Successfully!\n")

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

user_question = input(" Ask a question based on the Eiffel Tower context:\n> ")

result = qa_pipeline(question=user_question, context=context)

print("\n Answer:", result["answer"])