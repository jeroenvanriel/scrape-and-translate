#wget https://setup.johnsnowlabs.com/nlu/colab.sh -O - | bash
rm twitter_data_multi_lang.csv
wget http://ckl-it.de/wp-content/uploads/2021/02/twitter_data_multi_lang.csv
python train.py