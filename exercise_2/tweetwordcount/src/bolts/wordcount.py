from __future__ import absolute_import, print_function, unicode_literals

from collections import Counter
from streamparse.bolt import Bolt

import psycopg2
conn = psycopg2.connect(database="Tcount", user="postgres", password="pass", host="localhost", port="5432")


cur = conn.cursor()
cur.execute('''CREATE TABLE Tweetwordcount
       (word TEXT PRIMARY KEY     NOT NULL,
       count INT     NOT NULL);''')
conn.commit()
conn.close()

class WordCounter(Bolt):

    def initialize(self, conf, ctx):
        self.counts = Counter()


    def process(self, tup):
        word = tup.values[0]

        cur = conn.cursor()

        #Insert
        cur.execute("INSERT INTO Tweetwordcount (word,count) \
              VALUES ('test', 1)");
        conn.commit()

        #Update
        #Assuming you are passing the tuple (uWord, uCount) as an argument
        cur.execute("UPDATE Tweetwordcount SET count=%s WHERE word=%s", (uWord, uCount))
        conn.commit()

        #Select
        cur.execute("SELECT word, count from Tweetwordcount")
        records = cur.fetchall()
        for rec in records:
           print "word = ", rec[0]
           print "count = ", rec[1], "\n"
        conn.commit()

        conn.close()

        # Increment the local count
        self.counts[word] += 1
        self.emit([word, self.counts[word]])

        # Log the count - just to see the topology running
        self.log('%s: %d' % (word, self.counts[word]))
