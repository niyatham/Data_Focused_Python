from tweepy import OAuthHandler
import tweepy
import pandas as pd


class pharma_tweets:
    def get_tweets_cancer(search_term):
              
        
        access_token = '2564230999-Xr7WkHMWSYD6TqBmONqxl3HWwYxGzIgNeFBuwj8'
        access_token_secret = 'TZFNcnrxxG4yet1xlPUZRzLEnerxWIy2aiOicpnDAZ7ed'
        consumer_key = 'gYamveU0bPP7hz7KNd4vBK80a'
        consumer_secret = 'KEumqW4NmAovqQUqBI7PpidbfWnrGvZ72CFSlqm7EREwz2iGGP'
        
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        
        api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
        
        tweets = []
        
        for tweet in tweepy.Cursor(api.search, q=search_term, count=1000, since='2021-01-01').items(50000):
        
        	try: 
        		data = [tweet.created_at, tweet.text, tweet.user._json['screen_name'], tweet.entities['urls']]
        		data = tuple(data)
        		tweets.append(data)
        
        	except tweepy.TweepError as e:
        		print(e.reason)
        		continue
        
        	except StopIteration:
        		break
        
        df = pd.DataFrame(tweets, columns = ['created_at','tweet_text', 'screen_name', 'urls'])
        return df



