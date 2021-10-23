file_name_dutch = './tweets_dutch.txt'
file_name_english = './tweets_english.txt'
file_name_labels = './labels.txt'
file_name_dutch_csv = './dutch.csv'
file_name_english_csv = './english.csv'

with open(file_name_dutch, 'r') as di:                          # dutch input
    with open(file_name_english, 'r') as ei:                    # english input
        with open(file_name_labels, 'r') as l:                  # labels
            with open(file_name_dutch_csv, 'w') as do:          # dutch output
                with open(file_name_english_csv, 'w') as eo:    # english output
                    # write column headers to output files
                    print("id,text,y", file=do)
                    print("id,text,y", file=eo)
                    i = 0
                    # write tweets along with their labels to output files
                    for dutch_tweet, english_tweet, label in zip(di.readlines(), ei.readlines(), l.readlines()):
                        # removes line ending, drops commas and quotes, as these mess with csv encoding...
                        dt = dutch_tweet.rstrip('\n').replace('"', '').replace(',', '')
                        et = english_tweet.rstrip('\n').replace('"', '').replace(',', '')
                        print(str(i) + ',' + dt + ',' + label.rstrip('\n'), file=do)
                        print(str(i) + ',' + et + ',' + label.rstrip('\n'), file=eo)
                        i += 1

import pandas as pd

print("Verifying csv formatting...")

dutch_df = pd.read_csv(file_name_dutch_csv)
eng_df = pd.read_csv(file_name_english_csv)

print("Done.")