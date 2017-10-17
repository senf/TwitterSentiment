libraries used:
matplotlib https://matplotlib.org/
tweepy http://www.tweepy.org/
textblob https://textblob.readthedocs.io/en/dev/
mpl_toolkits.basemap https://matplotlib.org/basemap/index.html

The program reads the last 200 english language tweets returned for the query "donald trump"
These tweets are filtered by the user's state using the user's location field
For each state, a score is assigned. Each time a negative tweet comes from that state, score -=1
Likewise, score += 1 for that state when someone in that state tweets with a positive sentiment
States with positive scores are colored blue on the map, and negative states are colored red
States with a net score of '0' or states which did not produce any tweets are colored white
The Basemap library is used to render the US map and color in the states.
