The working Storm application is in the tweetwordcount folder.

Assuming the EC2 instance has the following configurations:

AMI Name: UCB MIDS W205 EX2-FULL
AMI ID: ami-d4dd4ec3

Already Installed:
Apache Storm, streamparse

Instructions:

Create the tcount database:
psql -U postgres
CREATE DATABASE tcount


run the following in the terminal:
bash script.sh

Press Enter if prompted to run as root(LEIN_ROOT)

Should see something similar to twitterStream.png

To Query for results, please look in the reportscripts folder.
