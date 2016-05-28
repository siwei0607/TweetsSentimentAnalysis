from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import csv, sys, datetime, json, time
import threading
    
def streamProc():
    threading.Timer(14400.0, streamProc).start()
    
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    #consumer key, consumer secret, access token, access secret.
    ckey=str("")
    csecret=str("")
    atoken = str("")
    asecret = str("")
    
    now=datetime.datetime.now()
    day=int(now.day)
    month=int(now.month)
    year=int(now.year)
    hour=int(now.hour)
    minute=int(now.minute)
    
    
    #You will need to fix this path
    outfile = '/Users/weisi/Desktop/tweets/Election_%i-%i-%i.%i.%i.csv' %(now.year, now.month, now.day, now.hour, now.minute)
    
    class listener(StreamListener):
    
        def on_data(self, data):
            try:
                f=csv.writer(open(outfile,"a"), delimiter="~")
                a = json.loads(str(data))
                row = []
                row.append(a["created_at"])
                row.append(a["user"]['id'])
                row.append(a["id"])
                row.append(a["text"])
                print row
                f.writerow(row)
                
            except Exception, e:
                print >>sys.stderr,'Encountered Exception:', e
                pass
    
        def on_error(self, status):
            print status
        
        def on_timeout(self):
            print >>sys.stderr, 'Time out....'
            return True
        
    auth = OAuthHandler(ckey, csecret)
    auth.set_access_token(atoken, asecret)
    
    twitterStream = Stream(auth, listener())
    twitterStream.filter(track=["keywords"])


def main():
    streamProc()

if __name__ == "__main__":
    main()
