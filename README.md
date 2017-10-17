Libraries:
matplotlib https://matplotlib.org/
tweepy http://www.tweepy.org/
textblob https://textblob.readthedocs.io/en/dev/
mpl_toolkits.basemap https://matplotlib.org/basemap/index.html

The program reads the last 200 english language tweets returned for the query "donald trump".
These tweets are filtered by the user's state using the user's location field.
For each state, a score is assigned. Scores are added to and subtracted from when Tweets are read.
with positive or negative sentiment. +1 for positive and -1 for negative.
States with positive scores are colored blue on the map, and negative states are colored red.
States with a net score of '0' or states which did not produce any tweets are colored white.
