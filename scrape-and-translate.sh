rm tweets_dutch.txt
rm tweets_english.txt

# scrape tweets and save them to tweets_dutch.txt
python parse-twitter-data.py

# translate tweets in tweets_dutch.txt and save them in tweets_english.txt
python translate.py

