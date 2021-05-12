import tweepy
import random

CONSUMER_KEY ='XXXX'
CONSUMER_SECRET = 'XXXX'   
ACCESS_KEY = 'XXXX'    
ACCESS_SECRET = 'XXXX'

num = random.randint(0,32627)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
api.update_status('Random Number: ' + str(num))

print('The random number generated is: ' + str(num))