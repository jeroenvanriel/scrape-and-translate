# taken from:
# https://github.com/JohnSnowLabs/nlu/blob/master/examples/colab/Training/multi_lingual/binary_text_classification/NLU_multi_lingual_training_sentiment_classifier_demo_twitter.ipynb

import nlu
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

print("Downloading ")
trainable_pipe = nlu.load('xx.embed_sentence.labse train.sentiment')
# We need to train longer and user smaller LR for NON-USE based sentence embeddings usually
# We could tune the hyperparameters further with hyperparameter tuning methods like gridsearch
# Also longer training gives more accuracy
trainable_pipe['sentiment_dl'].setMaxEpochs(60)  
trainable_pipe['sentiment_dl'].setLr(0.005)
print("Now training...")
fitted_pipe = trainable_pipe.fit(train_df)
# predict with the trainable pipeline on dataset and get predictions
preds = fitted_pipe.predict(train_df,output_level='document')

#sentence detector that is part of the pipe generates sone NaNs. lets drop them first
preds.dropna(inplace=True)
from sklearn.metrics import classification_report
print(classification_report(preds['y'], preds['trained_sentiment']))

print(preds)