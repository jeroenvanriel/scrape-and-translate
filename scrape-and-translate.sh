rm tweets.txt

snscrape -n 10 -f '{content}' twitter-search iets > tweets.txt

python translate.py

