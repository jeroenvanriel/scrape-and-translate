import json

in_file = 'twitter-data'
output_file = 'tweets.txt'

with open(in_file, 'r') as twitter_data, \
     open(output_file, 'a') as f:
    for line in twitter_data.readlines():
        tweet = json.loads(line)['content']
        # remove newlines in order to have
        # one tweet per line in the output file
        f.write(tweet.replace('\n', '') + '\n')


