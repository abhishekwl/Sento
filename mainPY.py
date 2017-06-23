###############################
# 	@codeauthor: Abhishek M
# 	Reach out to me @github/warlock1437
# 	Email me at nateriver210@gmail.com
#	STOP TRYING TO VIEW MY SOURCE
#	If you are seeing this, I want you to know that doing this just started a keylogger on your device.
#################################

import tweepy, json
from textblob import TextBlob

consumer_key = 'lUKONw2hbO07tl6uCnZJqxosI'
consumer_secret = 'dQzwDUsCplYMxvsO9yN5Dq7rfvP5K9V76UWSXueSYK3XL1ecGJ'
access_token = '2711844384-5YFSLJbKACyv4i29HlVWsOiWJTrX64hSzmBypJp'
access_token_secret = 'vhNXORp6vHa1g2CIIkviDDA0OT9wqxQc4AiuGqFGMbQLG'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

query = raw_input('Enter query\n---> ')
limit = input('Enter number of tweets to be returned\n---> ')

for tweet in tweepy.Cursor(api.search,q=query).items(limit=limit):
	tweetContent = str(tweet.text.encode('utf8'))
	wiki = TextBlob(tweetContent.decode('utf8'))
	tweetSentimentPolarity = float(wiki.sentiment.polarity)
	tweetSentimentSubjectivity = float(wiki.sentiment.subjectivity)
	if tweetSentimentPolarity==0.0:
		tweetSentimentPolarity = 'Neutral'
	elif tweetSentimentPolarity>0.0:
		tweetSentimentPolarity = 'Positive'
	else:
		tweetSentimentPolarity = 'Negative'
	if tweetSentimentSubjectivity==0.5:
		tweetSentimentSubjectivity = 'Neutral Opinion'
	elif tweetSentimentSubjectivity>0.5:
		tweetSentimentSubjectivity = 'Subjective Tweet'
	else:
		tweetSentimentSubjectivity = 'Objective Tweet'
	print '\n[+] '+tweetContent
	print 'Emotion : '+tweetSentimentPolarity+'\t'+tweetSentimentSubjectivity
