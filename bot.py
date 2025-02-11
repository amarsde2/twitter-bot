import tweepy 
import time 


'''

Used tweepy library to automate like and follow and retweet 

'''



# your consumer key and secret key to access twitter app 

mercent_key = "consumer key"
mercent_secret = "consumer secret key"
access_token = "access token key"
access_token_secret = "access token secret key"


# configuration for query , like, follow and sleep time

query = "#targethashtag"
should_like = True 
should_follow = True 
delay = 400

auth = tweepy.OAuthHandler(mercent_key, mercent_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search , q  = query).items():
    try:
        print(f"Tweet By: {tweet.user.screen_name}")
        tweet.retweet()


        # like tweet 
        if should_like:
            tweet.favorite()

        # follow twitter account if not following
        if should_follow:
            if not tweet.user.following:
               tweet.user.follow()


        time.sleep(delay)
        
    except tweepy.TweepEror as e:
   
        print(e.reason)
   
    except StopIteration:
        break