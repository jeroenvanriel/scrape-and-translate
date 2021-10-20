rm tweets_dutch.txt
rm tweets_english.txt

snscrape -n 10 -f '{content}' twitter-search iets > tweets_dutch.txt

python translate.py

