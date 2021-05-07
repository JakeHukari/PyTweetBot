import tweepy
import random

CONSUMER_KEY ="hzGQU7JazJT19Y79d2DrfnTJV"
CONSUMER_SECRET = "lAQlNXoaxyEequZHnitroGSyjOSlAxB6pc76qlIHyLMn1MTJTF"   
ACCESS_KEY = "1161775799596388352-f1e26ZYaJiL5XX7mX31l3t3VIggMPq"    
ACCESS_SECRET = "ii8UUZ6wuUOgKd5NfMccvDDmzRO4sf41J53f3xq2eGiaH"

num = random.randint(0,100)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

api = tweepy.API(auth)
api.update_status('Random Number' + str(num))