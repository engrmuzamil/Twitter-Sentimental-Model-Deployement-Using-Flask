# import Required Lib
from textblob import TextBlob
import re
# Function to check sentiment of Tweet
def check_sentiment(tweet):
    tweet =  re.sub("'", ' ', tweet)
    tweet =  re.sub("#", ' ', tweet)
    tweet = TextBlob(tweet)
    result = tweet.sentiment.polarity
    if result < 0:
        return 'Negative Tweet'
    elif result == 0:
        return 'Netural Tweet'
    else:
        return 'Positve Tweet'

