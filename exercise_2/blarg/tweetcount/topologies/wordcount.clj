(ns  tweetcount
(:use [streamparse.specs]) 
  (:gen-class))

(defn tweetcount [options] [
    ;; spout configuration
    {"Sentences" (python-spout-spec
      options "spouts.sentences.Sentences" 
      ["word"]
    )}
    ;; bolt configuration 1 
    {
    "ParseTweet" (python-bolt-spec
      options
      {"Sentences" :shuffle}
      "bolts.parse.ParseTweet"
      ["word"]
      :p 2
    )
    ;; bolt configuration 2
    "TweetCounter" (python-bolt-spec
      options
      {"ParseTweet" :shuffle}
      "bolts.tweetcounter.TweetCounter"
      ["word" "count"]
      :p 2
    )
  } ]
  )


