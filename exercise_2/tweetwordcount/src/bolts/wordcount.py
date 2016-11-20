from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2
conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")


cur = conn.cursor()

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()


    def process(self, tup):
        word = tup.values[0]
        
        #Update
        #Assuming you are passing the tuple (uWord, uCount) as an argument
        cur.execute("UPDATE Tweetwordcount SET count=count+1 WHERE word=%s", word)
        conn.commit()

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
