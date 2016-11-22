#ssh -i "UCB W205 HW2.pem" root@ec2-54-165-130-188.compute-1.amazonaws.com


# install the necessary python libraries
pip install psycopg2;
pip install tweepy;

rm -rf EX2Tweetwordcount;

sparse quickstart EX2Tweetwordcount;

# remove and copy the necessary files for the storm application
rm EX2Tweetwordcount/src/spouts/words.py;
rm EX2Tweetwordcount/src/bolts/wordcount.py;
rm EX2Tweetwordcount/topologies/wordcount.clj;
rm EX2Tweetwordcount/virtualenvs/wordcount.txt;

cp sparsefiles/tweets.py EX2Tweetwordcount/src/spouts/;
cp sparsefiles/wordcount.py EX2Tweetwordcount/src/bolts/;
cp sparsefiles/parse.py EX2Tweetwordcount/src/bolts/;
cp sparsefiles/tweetwordcount.txt EX2Tweetwordcount/virtualenvs/;
cp sparsefiles/tweetwordcount.clj EX2Tweetwordcount/topologies/;
cp -R EX2Tweetwordcount ~/;
# create the db
python create_tcount.py;

# start sparse
cd ~/EX2Tweetwordcount;
sparse run;
