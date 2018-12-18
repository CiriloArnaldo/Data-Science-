import re # This module provides regular expression matching operations similar to those found in Perl.
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import pandas as pd


class TwitterClient(object):
    """
    Generic Twitter Class for Sentiment Analysis
    """
    def __init__(self):
        '''
        Class Constructor or Initialization Method
        '''
        consumer_key = '6GA9Cq6EcMazscYbtfwZ0fKjz'
        consumer_secret = '9jKmzEpyCCcrPaTu6NHSV03nNo03pUplfLiN6VFskes9hJOxkX'
        access_token = '1072612111568777223-jeK0cG4sXJy8mNEm1QhGUK4Hhrb8UU'
        access_token_secret = '9lFGtCgrc5PDosyq3g3Cyimwtowg7xzIgVWnLlD4oQ5Y1'

        # Attempt Authentication
        try:
            # Creat OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # Set access token and consumer_secret
            self.auth.set_access_token(access_token, access_token_secret)
            # Create tweepy API object to fetch Tweets
            self.api = tweepy.API(self.auth)

            print('well Authenticated')
        except:
            print('Error: Authentication Failed')

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing using
        simplex regex statements.
        '''
        return ' '.join(re.sub(" (@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", tweet).split() )

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed
        using textblob's sentiment method
        '''
        #Create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main funtion to bring tweets and parse them
        '''
        # Empty list to store parse tweets
        tweets=[]
        try:
            # Call twitter api to fetch Tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # Parsing tweets one by one
            for tweet in fetched_tweets:
                # Empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # Saving text of Tweet
                parsed_tweet['text'] = tweet.text
                #Saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)
                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error: "+str(e))

#api = TwitterClient()

def main():
    # creating object of TwitterClient Class
    print("Hola")
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets(query = 'Trump', count = 200)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(tweets)))

    # picking negative tweets from tweets
    ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(tweets)))

    # percentage of neutral tweets
    neutweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
    print("Neutral tweets percentage: {} % ".format(100*len(neutweets)/len(tweets)))



    # printing first 5 positive tweets
    print("\n\nPositive tweets:")
    for tweet in ptweets[:10]:
        print(tweet['text'])

    # printing first 5 negative tweets
    print("\n\nNegative tweets:")
    for tweet in ntweets[:10]:
        print(tweet['text'])

    # printing first 5 neutral tweets
    print("\n\nNeutral tweets:")
    for tweet in neutweets[:10]:
        print(tweet['text'])

    # Texto de Prueba
    print(type(neutweets[0]['text']))
    print(len(ptweets))
    # Guardando la data en un archivo CSV
    df = pd.DataFrame(columns=['Text', 'Sentiment'])
    for i in range(len(ptweets)):
        df.loc[i]= [ptweets[i]['text'], ptweets[i]['sentiment']]
    print(df)

    saveData(ptweets,ntweets,neutweets)

def saveData(ptweets,ntweets,neutweets):

    print("Estoy guardando")


# run directly or run from import ?
if __name__ == "__main__": # Is this file being run directly by Python or is it being imported ?
    # This file is being run directly by Python
    #Calling main function
    main()
