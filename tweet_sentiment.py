import tweepy
import sys
import keyToken

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            print(status.text)
            saveFile = open('twiDB.csv', 'a', encoding='utf-8')
            saveFile.write(status.text)
            saveFile.write('\n')
            saveFile.close()
            return True
        except Exception as e:
            print(e)
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_error disconnects the stream
            return False
            print (status)


myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['python'], is_async=True)

