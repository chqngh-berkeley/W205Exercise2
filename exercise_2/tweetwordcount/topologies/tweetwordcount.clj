(ns tweetwordcount
  (:use     [streamparse.specs])
  (:gen-class))

(defn tweetwordcount [options]
   [
    ;; spout configuration
    {"Tweets" (python-spout-spec
          options
          "spouts.tweets.Tweets"
          ["tweet"]
          :p 1
          )
    }
    ;; bolt configuration
    {"ParseTweet" (python-bolt-spec
          options
          {"Tweets" :shuffle}
          "bolts.parse.ParseTweet"
          ["word"]
          :p 2
          )
     "CountBolt" (python-bolt-spec
          options
          {"ParseTweet" ["word"]}
          "bolts.wordcount.WordCounter"
          ["word" "count"]
          :p 2
          )
    }
  ]
)
