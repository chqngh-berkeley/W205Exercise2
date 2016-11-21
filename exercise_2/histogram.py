import psycopg2
import sys, getopt

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")

def main(argv):
    params = argv[0].split(',')
    k1 = int(params[0])
    k2 = int(params[1])
    cur = conn.cursor()
    cur.execute('SELECT word, count from Tweetwordcount \
        WHERE count >= %d AND count < %d', (k1, k2))
    records = cur.fetchall()
    for rec in records:
        print "%s : %d" % (rec[0], rec[1]), '\n'

if __name__ == "__main__":
    main(sys.argv[1:])
