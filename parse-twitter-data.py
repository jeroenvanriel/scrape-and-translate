import json
import snscrape.modules.twitter as sntwitter

max_tweets = 100

output_file = "tweets_dutch.txt"
keywords_file = "keywords.txt"

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

# Perform the scrape, keyword by keyword.
with open(keywords_file, 'r') as f:
    for keyword in f.readlines():
        scrapeByKeyword(keyword.rstrip("\n"))
        print()

# write contents of all scraped tweets to the output file.
print("Beginning writing Dutch tweets to file...") 
with open(output_file, 'w') as f:
    for tweet in tweets_list:
        # replace newlines with spaces
        f.write(tweet.replace('\n', ' ') + '\n')

print("Done.")
print()
