# import time
# import os
# import pandas

# while True:
#     if os.path.exists("files/temps_today.csv"):
#         data = pandas.read_csv("files/temps_today.csv")
#         print(data.mean()["st1"])

#     else:
#         print("File does not exist.")
#     #time.sleep(10)

import json
import difflib
from difflib import get_close_matches


def word_def(word):
    data = json.load(open("teaching/data.json"))
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        return "Did you mean %s instead?" %get_close_matches(word, data.keys())[0]
    else:
        return "We didn't find word. Please double check it."

print(word_def(input("Enter the word: ")))
