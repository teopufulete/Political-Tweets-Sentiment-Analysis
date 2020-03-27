# Political-Tweets-Sentiment-Analysis

Aiming to predict the 2020 US presidential election results using sentiment analysis

*Architecture choices:
  *Bidirectional LSTM - to determine polarity of a tweet
  *Bayesian inference - to analyze LSTM output and make predictions

*Techonoloes used:
  *Data collection:
    *Tweepy - twitter API for data scraping
  
  *Data preprocessing:
    *Pandas - handling large amounts of data
    *Regex - general noise removal
    *NLTK -  tokenization, stemming, lemmatization, stopword removal
    *Glob - merging multiple csvs into one
  
  *Data analysis:
    *Numpy - handling high-dimensional mathematical operations
    *sklearn - feature extraction and word embedding
    *Keras - testing different architectures, picked Bidirectional LSTM after comparing accuracy of different models
