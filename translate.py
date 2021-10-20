# We could use the unofficial Google translate api, but then
# we might have a chance of getting our ip address banned.
#
# from googletrans import Translator
# translator = Translator()
# print(translator.translate('what is this').text)
# print(translator.translate('veritas lux mea', src='la').text)

import time
def clock():
    global start
    now = time.time()
    print(f'elapsed={now - start}\n')
    start = now


from transformers import MarianMTModel, MarianTokenizer

start = time.time()
print('loading/initializing model')

model_name = "Helsinki-NLP/opus-mt-nl-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

clock()

def translate(dutch):
    inputs = tokenizer(dutch, return_tensors='pt', padding=True)
    translated = model.generate(**inputs)
    return [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

import pandas as pd

file_name_dutch = './tweets_dutch.txt'
file_name_english = './tweets_english.txt'

with open(file_name_dutch, 'r') as d:
    with open(file_name_english, 'w') as e:
        print('start translating')
        max_n = 10000
        for id, tweet in zip(range(max_n), d.readlines()):
            print(tweet, end='')
            print(' -> ')
            translation = translate(tweet)[0]
            print(translation)
            print(translation, file=e)

            clock()

