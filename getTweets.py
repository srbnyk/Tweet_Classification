from TwitterSearch import *
import codecs
import re
import os
import threading
import time
start_time = time.time()

def get_tweets():
    #threading.Timer(900.0, get_tweets).start()
    try:

        # creating a TwitterSearch object with secret tokens
        ts = TwitterSearch(
            consumer_key = 'vp3IyaYPaMKQrOcD109Jm54Pj',
            consumer_secret = 'Gv9g4nuwpIBFTGo00RBO8uDZUd1PpzDOuwF6zOfTXrwZZrE0V3',
            access_token = '198949689-mBj3YNFyPb8mnJ3BlDp0vFT7uk3yyVRAdwHe4PRP',
            access_token_secret = 'dtd2qaU6gzUxIi9pYtDIz5Xqvi8hY6Aih35QwKSLDhUSd'
         )
        # minimum length of tweets to consider for our tweet
        list_length = 4

        # following tags have been shortlisted for classification
        l = ['sport', 'technology', "law", "politics", "education", "fashion", "entertainment", "nature", "health", "travel", "lifestyle"]

        #getting tweet for every tag
        for item in l:
            d = {}
            tso = TwitterSearchOrder()  # creating a TwitterSearchOrder object
            tso.set_keywords([item])    #setting tag as keyword

            tso.set_language('en')  # we want to see English tweets only
            # tso.set_geocode(37.784173, -122.401557, 2000000) #location specific tweets can be filtered (if needed)

            f = codecs.open("Tweets_Old"+"/"+item+"0101.txt", encoding='utf-8', mode='a+')
            for tweet in ts.search_tweets_iterable(tso):
                s = "@"+tweet['user']['screen_name'] + " tweeted: "+tweet['text']
                lines = re.sub(r"(http|https|ftp)://[a-zA-Z0-9\./]+","",s)

                if lines and "RT" not in lines and "@" in lines and "son in law" not in lines and "sister in law" not in lines and "mother in law" not in lines \
                        and "father in law" not in lines and "brother in law" not in lines and "Law of Motion" not in lines and "coupon" \
                        not in lines and "Coupon" not in lines and "SBargainsUK" not in lines and "SuperDeals" not in lines and "mother-in-law" not \
                        in lines and "brother-in-law" not in lines and "son-in-law" not in lines:
                    print ("line: ",lines)
                    list_test = lines.split()
                    # print ("initial split: ", list_test)
                    list_test_aux = []
                    for words in list_test:
                        if "@" in words or "tweeted" in words or "RT" in words:
                            print ("removing word: ", words)
                        else:
                            list_test_aux.append(words)
                    #print ("after removing words: ", list_test_aux)
                    print (len(list_test_aux))
                    if len(list_test_aux) > list_length:
                        s = " ".join(list_test_aux)
                        if s not in d:
                            d[s] = lines



                f.write(lines+"\n")
            f.close()
    except TwitterSearchException as e: # take care of all those ugly errors if there are some
       print(e)
get_tweets()
print("--- %s seconds ---" % (time.time() - start_time))