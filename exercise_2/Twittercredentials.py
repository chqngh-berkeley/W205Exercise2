import tweepy

consumer_key = "OxVI9q0hlNaUqIUYu3bRO8Deg";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "PQXfZrMryy5YibmEQ5idYXSCtCHqItajBkRvFwKZvYwLPOSWEL";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "800157203529224192-JFJddvlp7WfpssUJM7d1wNbDjddUcBK";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "ngw4itsO90ZrVSiI5b2rApWiMuvIGaCbr67LGB5m4prDV";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
