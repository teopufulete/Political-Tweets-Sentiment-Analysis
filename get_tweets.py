import tweepy
import csv
import panda as pd
import os
import json

access_token = "ENTER YOUR ACCESS TOKEN"
access_token_secret = "ENTER YOUR ACCESS TOKEN SECRET"
consumer_key = "ENTER YOUR API KEY"
consumer_secret = "ENTER YOUR API SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

general_2020election_tweets = "...data/2020election_data.csv"
trump_tweets = "...data/trump_data.csv"
warren_tweets = "...data/warren_data.csv"

COLS = ['id', 'created_at','original_text','clean_text', 'sentiment', 'favorite_count', 'retweet_count', 'possibly_sensitive', 'hashtags',
'user_mentions', 'place']

emoji_pattern = re.compile("["
         u"\U0001F600-\U0001F64F"  # emoticons
         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
         u"\U0001F680-\U0001F6FF"  # transport & map symbols
         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
         u"\U00002702-\U000027B0"
         u"\U000024C2-\U0001F251"
         "]+", flags=re.UNICODE)

def write_tweets(keyword, file):
    
    if os.path.exists(file):
        df = pd.read_csv(file, header=0)
    else:
        df = pd.DataFrame(columns=COLS)
    
    for page in tweepy.Cursor(api.search, q=keyword,
                              count=200, include_rts=False, lang="en", since="2017-04-03").items()
    
    for status in page:
        new_entry = []
        status = status._json
        
      
    

