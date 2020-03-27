import pandas as pd
import numpy as np
import nltk
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer
from textblob import TextBlob

tweets_df = pd.read_csv('data/concatenate/combined_csv.csv')

tweets_df = tweets_df.replace('RT([^:]*):', '', regex = True)        # remove retweet mentions
tweets_df = tweets_df.replace('https(.*)', '', regex = True)        # remove links
tweets_df = tweets_df.replace('@[A-Za-z0-9]+', '', regex = True)        # remove @user mentions
tweets_df = tweets_df.replace('//(.*)', '', regex = True)
tweets_df = tweets_df.replace(r'[^\w]', ' ', regex = True)
tweets_df = tweets_df.replace('[a-zA-Z]*â€¦[a-zA-Z]*', '', regex = True)        # remove all non-letter/number chars

tweets_df = tweets_df.apply(lambda x: x.str.lower() if x.dtype == "object" else x)      # lower case every word

tweets_df['tweets'] = tweets_df['tweets'].astype(str)

# tokenize
def identify_tokens(row):
    tweets = row['tweets']
    tokens = nltk.word_tokenize(tweets)
    token_words = [w for w in tokens if w.isalpha()]
    return token_words

tweets_df['token'] = tweets_df.apply(identify_tokens, axis=1)

# stemming
stemming = LancasterStemmer()
def stem_list(row):
    my_list = row['token']
    stemmed_list = [stemming.stem(word) for word in my_list]
    return (stemmed_list)

tweets_df['stemmed_words'] = tweets_df.apply(stem_list, axis=1)

# remove stop words
stops = set(stopwords.words('english'))
def remove_stops(row):
    my_list = row['token']
    meaningful_words = [w for w in my_list if not w in stops]
    return (meaningful_words)

tweets_df['meaningful'] = tweets_df.apply(remove_stops, axis=1)

tweets_df['meaningful'] = tweets_df['meaningful'].astype(str)

def spelling_correction(tweets):
    try:
        return TextBlob(tweets).correct()
    except UnicodeDecodeError:
        return None

tweets_df['checked spelling'] = tweets_df['meaningful'].apply(lambda x: spelling_correction(x))

def get_sentiment(tweets):
    try:
        return TextBlob(tweets).sentiment
    except:
        return None

tweets_df['sent'] = tweets_df['tweets'].apply(get_sentiment)

tweets_df['sent'][0][0]
tweets_df['polarity'] = tweets_df['sent'].apply(lambda x: x[0])
tweets_df['subjectivity'] = tweets_df['sent'].apply(lambda x: x[1])




tweets_df.to_csv('data/new_combined.csv', index = False)

