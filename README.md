# Data Generation

## Default workflow
To scrape Dutch tweets and automatically translate them:
1. `pip install -r requirements.txt` to install dependencies,
1. `./scrape-and-translate.sh` to scrape and immediately translate Dutch tweets to English.

## Advanced workflow
Because we wanted to manually drop nonsensical tweets in between these steps, we had a different workflow to create data. This way, we could subdivide the manual work among all five authors.

Our workflow:
1. `pip install -r requirements.txt` to install dependencies,
1. `python parse-twitter-data.py` to scrape tweets,
1. split up result (`tweets_dutch.txt`) into 5 subsets, one for each author,
1. all authors dropped their nonsensical tweets manually,
1. all authors labelled their tweets,
1. all authors translated their tweets using `python translate.py` (edited to include paths to personal Dutch and English files)
1. recombine authors' Dutch, English and label files into:
    - `/data processing/combined/tweets_dutch.txt`
    - `/data processing/combined/tweets_english.txt`
    - `/data processing/combined/labels.txt`
1. ran `python "/data processing/combined/txts_to_csvs.py"`

The resulting files (`dutch.csv` and `english.csv`) are loaded by our Colab notebook.

# Training and Validation
For the steps we have taken in order to train our model and analyse its performance, please have a look at our [Colab notebook](https://colab.research.google.com/drive/18EwDscTv0y-NTEqcRvKoXZ6fkim52eUg?usp=sharing).
