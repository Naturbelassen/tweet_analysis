import tweepy
import sys
import keyToken
from nltk import word_tokenize
from nltk.corpus import stopwords

#Validate access rights
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    """
    on_status gets the statuses/tweets without extra information
    write results into a file
    on_error ensures no lock out
    """
    def on_status(self, status):
        try:
            print(status.text)
            saveFile = open('twiDB.txt', 'a', encoding='utf-8')
            saveFile.write(status.text)
            saveFile.write('\n')
            saveFile.close()
            return True
        except Exception as e:
            print(e)
    def on_error(self, status_code):
        if status_code == 420:
            return False
            print (status)

class tweetPreProccess(status.text)
    """
    Setting stop_words to include english words like the, a, an, in
    Tokenize the collected tweet for further analysis
    Compare tokenized tweet eith the collection of stop_words, if the result is negative add it to cleanTweet
    """
    stop_words = set(stopwords.words('english')
    word_tokens = word_tokenize(example_sent) 
    cleanTweet = []
                     
    for w in word_tokens
        if w not in stop_words
            cleanTweet.append(w)
    return cleanTweet
            
                     

    print(cleanTweet)

    

# Only tweets that contain 'python' will be collected
# is_async enabled means using another thread when disconnect
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['python'], is_async=True)

