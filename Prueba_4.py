import tweepy
from textblob import TextBlob
import pandas as pd

# Step 1 - Authenticate
consumer_key = '6GA9Cq6EcMazscYbtfwZ0fKjz'
consumer_secret = '9jKmzEpyCCcrPaTu6NHSV03nNo03pUplfLiN6VFskes9hJOxkX'
access_token = '1072612111568777223-jeK0cG4sXJy8mNEm1QhGUK4Hhrb8UU'
access_token_secret = '9lFGtCgrc5PDosyq3g3Cyimwtowg7xzIgVWnLlD4oQ5Y1'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment
#You can decide the sentiment polarity threshold yourself

df = pd.DataFrame(columns=['Text','Sentiment_level'])
i = 0

for tweet in public_tweets:
    print(tweet.text)
    print(type(tweet.text))
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print(type(analysis.sentiment.polarity))
    print("")

    df.loc[i] = [tweet.text , round(analysis.sentiment.polarity,2)]
    i += 1

print(df)

df.to_csv('Datos.csv')
