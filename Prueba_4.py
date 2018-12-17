import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'gaotNxAHDnrHvTgVVjlddzbgp'
consumer_secret= 'QauM5qAMOyZ8326XzuRcNbbdjHZrJRIGKbiIqzZ6QwdenJisjJ'

access_token='1072612111568777223-K5OdWKvBczN15nDhSUTdmPw51IwNMo'
access_token_secret='RX6aC2o8nalqTCNy0IvbuaBJDJ9PiS1vZrkzcsJ4NVejE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)

    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
