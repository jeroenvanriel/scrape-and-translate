# We could use the unofficial Google translate api, but then
# we might have a chance of getting our ip address banned.
#
# from googletrans import Translator
# translator = Translator()
# print(translator.translate('what is this').text)
# print(translator.translate('veritas lux mea', src='la').text)

import time
from transformers import MarianMTModel, MarianTokenizer

def clock():
    global start
    now = time.time()
    print(f'elapsed={now - start}\n')
    start = now

file_name_dutch = './data processing/tweets_dutch_sietze.txt'
file_name_english = './data processing/tweets_english_sietze.txt'
verbose = False

print("Translating tweets in " + file_name_dutch)
start = time.time()
if verbose:
    print('loading/initializing model')

model_name = "Helsinki-NLP/opus-mt-nl-en"
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

if verbose:
    clock()

def translate(dutch):
    inputs = tokenizer(dutch, return_tensors='pt', padding=True)
    translated = model.generate(**inputs)
    return [tokenizer.decode(t, skip_special_tokens=True) for t in translated]

num_lines = sum(1 for line in open(file_name_dutch))

with open(file_name_dutch, 'r') as d:
    with open(file_name_english, 'w') as e:
        if verbose:
            print('start translating')
        max_n = 10000
        for id, tweet in zip(range(max_n), d.readlines()):
            translation = translate(tweet)[0]
            if verbose:
                print(tweet, end='')
                print(' -> ')
                print(translation)
                clock()
            else:
                print("\r    Tweets translated: " + str(id + 1) + "/" + str(min(max_n, num_lines)), end="")
            print(translation, file=e)

print()
print("Done. Saved in " + file_name_english)
