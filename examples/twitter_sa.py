from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

#consumer key, consumer secret, access token, access secret.
ckey="FG1OfbjQM8y21ziSPY7rJiWjY"
csecret="Uckz4SHgvYoZ7LURWl1Ms62ScCzB4ZO63t8YEw0cnbya0RV2E4"
atoken="2557170452-GWx0paToPFAsUVYqJ6iPK8bjDYD6j29Jk8oRMaZ"
asecret="JN9CL1Y1t6grzsISgVbJJkthDdt6EgYBiXGjiwDQoE5kg"

# from twitterapistuff import *

class listener(StreamListener):

	def on_data(self, data):

		all_data = json.loads(data)

		tweet = all_data["text"]
		sentiment_value, confidence = s.sentiment(tweet)
		print(tweet, sentiment_value, confidence)

		if confidence*100 >= 80:
			output = open("twitter-out.txt","a")
			output.write(sentiment_value)
			output.write('\n')
			output.close()

		return True

	def on_error(self, status):
		print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])