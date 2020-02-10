import tweepy
import csv
import os
import json
import re
import pandas as pd


access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

general_2020election_tweets = "data/2020election_data.csv"
trump_tweets = "data/trump_data.csv"
warren_tweets = "data/warren_data.csv"

COLS = ['id', 'created_at','favorite_count', 'retweet_count', 'hashtags', 'place']

def write_tweets(keyword, file):
    
    # if os.path.exists(file):
    #     df = pd.read_csv(file, header=0)
    # else:
    # df = pd.DataFrame(columns = COLS)
    all_entries = []
    for page in tweepy.Cursor(api.search, q=keyword,count=3, include_rts=False).pages(3):
        for status in page:
            new_entry = None
            status = status._json

            if status['lang'] != 'en':
                continue
            

            # if status['created_at'] in df['created_at'].values:
            #     i = df.loc[df['created_at'] == status['created_at']].index[0]
            #     if status['favorite_count'] != df.at[i, 'favorite_count'] or \
            #         status['retweet_count'] != df.at[i, 'retweet_count']:
            #          df.at[i, 'favorite_count'] = status['favorite_count']
            #          df.at[i, 'retweet_count'] = status['retweet_count']
            #     continue
 
            new_entry = [status['id'], status['created_at'],
                        status['source'], status['text'], 
                        status['favorite_count'], status['retweet_count']]
            # print(new_entry[3])

            all_entries.append(new_entry)
    # print(all_entries)
    # csvFile = open(file, 'a' ,encoding='utf-8')
    # df.to_csv(csvFile, mode='a', columns=COLS, index=False, encoding="utf-8")
    with open(file, 'a' ,encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(COLS)
        print(all_entries)
        writer.writerows(all_entries)


trump_keywords = '#trump OR #donaldtrump'
election_keywords = '#2020election'
write_tweets(trump_keywords, trump_tweets)
write_tweets(election_keywords, general_2020election_tweets )
