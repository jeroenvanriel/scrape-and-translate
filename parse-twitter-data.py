import json
import snscrape.modules.twitter as sntwitter

max_tweets = 100

output_file = "tweets_dutch.txt"

def scrapeByKeyword(query):
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(keyword).get_items()):
        if i % 10 == 0:
            print("\r tweets scraped for keyword '" + keyword + "': " + str(i) + "/" + str(max_tweets) + "       ", end = "")
        if i >= max_tweets:
            break
        tweets_list.append(tweet.content)


# Creating list to append tweet data to
tweets_list = []
# temporary. TODO load from file.
keywords = ["hond", "kat", "meneer"]

for keyword in keywords:
    scrapeByKeyword(keyword)
    print()

print()
print("Beginning writing Dutch tweets to file...") 

with open(output_file, 'w') as f:
    for tweet in tweets_list:
        f.write(tweet.replace('\n', '') + '\n')

print("Done.")
print()