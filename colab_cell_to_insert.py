# assumes dutch.csv and english.csv have been uploaded to 
# top-level dir of this instance, and all cells up to 3.1 (not including)
# have been run.
dutch_path = '/content/dutch.csv'
english_path = '/content/english.csv'
dutch_out_path = '/content/dutch_preds.csv'
english_out_path = '/content/english_preds.csv'

dutch_df = pd.read_csv(dutch_path)
english_df = pd.read_csv(english_path)

dutch_preds = fitted_pipe.predict(dutch_df)
english_preds = fitted_pipe.predict(english_df)

# this is where you could save only a slice of the dataframe, e.g. to not include the sentence embedding...
dutch_preds.to_csv(dutch_out_path)
english_preds.to_csv(english_out_path)

from google.colab import files
files.download(dutch_out_path)
files.download(english_out_path)