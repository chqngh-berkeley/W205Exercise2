import matplotlib.pyplot as plt
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

cur.execute('SELECT * from Tweetwordcount order by count desc limit 20')
records = cur.fetchall()
cur.commit()
cur.close()

plt.title("Top 20 Words")
plt.xlabel("Words")
plt.ylabel("Count")
plt.hist(records)
