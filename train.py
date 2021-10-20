# taken from:
# https://github.com/JohnSnowLabs/nlu/blob/master/examples/colab/Training/multi_lingual/binary_text_classification/NLU_multi_lingual_training_sentiment_classifier_demo_twitter.ipynb

import pandas as pd
train_path = "./twitter_data_multi_lang.csv"

train_df = pd.read_csv(train_path)
train_df.test_sentences = train_df.test_sentences.astype(str)
# the text data to use for classification should be in a column named 'text'
# the label column must have name 'y' name be of type str
train_df= train_df[["text","y"]]
from sklearn.model_selection import train_test_split
train_df, test_df = train_test_split(train_df, test_size=0.2)

print("Loaded training data:")
print(train_df)