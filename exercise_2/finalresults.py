import psycopg2
import sys, getopt

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

def main(argv):
    if len(argv) == 0:
        cur = conn.cursor()
        cur.execute('SELECT * from Tweetwordcount order by word asc')
        records = cur.fetchall()
        for rec in records:
           print rec
    else:
        cur.execute("SELECT word, count from Tweetwordcount where word =%s", (argv[0]))
        record = cur.fetchOne()
        print "Total number of occurences of \"%s\" : %d" % (record[0], record[1])
    conn.commit()
    conn.close

if __name__ == "__main__":
    main(sys.argv[1:])
