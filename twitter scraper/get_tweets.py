import tweepy
import csv
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

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

general_2020election_tweets = "data/general_2020election_data.csv"
trump_tweets = "data/trump_data.csv"
warren_tweets = "data/warren_data.csv"
bernie_tweets = "data/bernie_data.csv"
biden_tweets = "data/biden_data.csv"
buttigieg_tweets = "data/buttigieg_data.csv"
bloomberg_tweets = "data/bloomberg_data.csv"
gabbard_tweets = "data/gabbard_data.csv"
klobuchar_tweets = "data/klobuchar_data.csv"
steyer_tweets = "data/steyer_data.csv"


COLS = ['id', 'created_at', 'favorite_count', 'tweet', 'place']


def write_tweets(keyword, file):
    # if os.path.exists(file):
    #     df = pd.read_csv(file, header=0)
    # else:
    # df = pd.DataFrame(columns = COLS)
    all_entries = []
    for page in tweepy.Cursor(api.search, q=keyword, count=50, include_rts=False).pages(200):
        for status in page:
            new_entry = None
            status = status._json

            if status['lang'] != 'en':
                continue

            new_entry = [status['id'], status['created_at'],
                         status['text'], status['favorite_count'], status['retweet_count']]
            # print(new_entry[3])

            all_entries.append(new_entry)
    # print(all_entries)
    # csvFile = open(file, 'a' ,encoding='utf-8')
    # df.to_csv(csvFile, mode='a', columns=COLS, index=False, encoding="utf-8")
    with open(file, 'a', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(COLS)
        print(all_entries)
        writer.writerows(all_entries)


trump_keywords = ['#Trump2020', 'DonaldTrump', 'Trump']
election_keywords = '#2020election'
warren_keywords = ['#ElizabethWarren', '#Warren', 'Warren2020']
bernie_keywords = ['#BernieSanders', '#Bernie2020', '#FeelTheBern']
biden_keywords = ['#Biden', '#JoeBiden', '#Biden2020']
buttigieg_keywords = ['#PeteButtigieg', 'PeteForAmerica', 'Pete2020']
bloomberg_keywords = ['#Bloomberg2020', '#MichaelBloomberg']
gabbard_keywords = ['#Tulsi', '#Tulsi2020', '#TulsiGabbard']
klobuchar_keywords = ['#Klobuchar', '#Kim2020', '#KimKlobuchar']
steyer_keywords = ['#Steyer', '#Steyer2020', '#TomSteyer']


write_tweets(trump_keywords, trump_tweets)
write_tweets(election_keywords, general_2020election_tweets)
write_tweets(warren_keywords, warren_tweets)
write_tweets(bernie_keywords, bernie_tweets)
write_tweets(biden_keywords, biden_tweets)
write_tweets(buttigieg_keywords, buttigieg_tweets)
write_tweets(bloomberg_keywords, bloomberg_tweets)
write_tweets(gabbard_keywords, gabbard_tweets)
