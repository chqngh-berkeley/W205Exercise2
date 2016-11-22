import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute('SELECT * from Tweetwordcount order by count desc limit 20')
records = cur.fetchall()

for rec in records:
    print "%s : %s" % (rec[0], rec[1]), '\n'

cur.commit()
cur.close()
