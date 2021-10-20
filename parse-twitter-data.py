import json
import snscrape.modules.twitter as sntwitter

max_tweets = 100

output_file = "tweets_dutch.txt"

# function to scrape tweets by keyword
def scrapeByKeyword(keyword):
    # Using TwitterSearchScraper to scrape data and append tweets to list
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(keyword).get_items()):
        # print progress to CLI
        if i % 10 == 0:
            print("\r tweets scraped for keyword '" + keyword + "': " + str(i) + "/" + str(max_tweets) + "       ", end = "")
        if i >= max_tweets:
            break
        tweets_list.append(tweet.content)


# Creating list to append tweet data to
tweets_list = []
# temporary. TODO load from file.
keywords = ["hond", "kat", "meneer"]

# Perform the scrape, keyword by keyword. TODO get from file.
for keyword in keywords:
    scrapeByKeyword(keyword)
    print()

# write contents of all scraped tweets to the output file.
print("Beginning writing Dutch tweets to file...") 
with open(output_file, 'w') as f:
    for tweet in tweets_list:
        # replace newlines with spaces
        f.write(tweet.replace('\n', ' ') + '\n')

print("Done.")
print()
