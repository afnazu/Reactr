import tweepy
from textblob import TextBlob
import sys
import csv

#check length of argument(topic)
if len(sys.argv) >= 2:
    topic = sys.argv[1]
else:
    print("Default topic is gender.")
    topic = "Gender"


#pass security info to variables
consumer_key='nkVupdTOywYP06ZPjcqy5QPh5'
consumer_secret='Zja0QNkNUXzgRuqEPlTo0Oi6NJN6wUvih937cXUluzCxplnYuF'

access_token='285958794-dboeXjTVKcRq7uZNBioRuUTCQKg5qV5tqzXZIpbo'
access_token_secret='qClIA2g8URNeiN2jLwoAT6nQj5iEox5yFP95npkYvNKRq'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#retrieve Tweets
public_tweets = api.search('Gender')

with open('sentiments.csv', 'w', newline='\n') as f:
    filewriter = csv.DictWriter(f, fieldnames=['Tweet', 'Sentiment'])
    filewriter.writeheader()
    for tweet in public_tweets:
        text = tweet.text
        cleantext = ' '.join([word for word in text.split(' ')
                              if len(word) > 0 and word[0] != '@'
                              and word[0] == '.' and word[0] != '#'
                              and 'http' not in word and word != 'RT'])
        analysis = TextBlob(cleantext)

        sentiment = analysis.sentiment.polarity
        if sentiment >= 0:
            polarity = 'Positive'
        else:
            polarity = 'Negative'

        filewriter.writerow({'Tweet':text, 'Sentiment':polarity})
    
