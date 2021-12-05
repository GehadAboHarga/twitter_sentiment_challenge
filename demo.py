import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
# install twitter api then navigate to tokens and paste your twitter account tokens here
consumer_key= 'CONSUMER_KEY_HERE'
consumer_secret= 'CONSUMER_SECRET_HERE'

access_token='ACCESS_TOKEN_HERE'
access_token_secret='ACCESS_TOKEN_SECRET_HERE'

# use tokens to login to twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# create twiiter api object
api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
# search public tweets for certain word
public_tweets = api.search('we_support_abotreka')

polarity_arr = []

for tweet in public_tweets:
    print(tweet.text)
    #Step 4 Perform Sentiment Analysis on Tweets
    # create textblob object from every tweet text 
    analysis = TextBlob(tweet.text)
    # print polarity of each tweet (+ve or -ve)
    polarity_arr.append(int(analysis.sentiment.polarity))
    print(analysis.sentiment.polarity)
    print("")
    # print subjectivity of each tweet (The subjectivity is a float within the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.)
    print(analysis.sentiment.subjectivity)
    print("")
    
abs_polarity =  [abs(ele) for ele in polarity_arr]
avg_polarity = polarity_arr.sum() / polarity_arr.len()
abs_avg_polarity = abs_polarity.sum() / abs_polarity.len()
print("average polarity is " + avg_polarity "and absolute average polarity is" + abs_avg_polarity)
# average polarity gives us an impression whether most people is +ve or -ve about the text
# absolute average polarity gives us an impression how much people are polar regarding their opinions in the matter
