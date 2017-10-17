Libraries:

matplotlib https://matplotlib.org/

tweepy http://www.tweepy.org/

textblob https://textblob.readthedocs.io/en/dev/

mpl_toolkits.basemap https://matplotlib.org/basemap/index.html

The program reads the last 200 english language tweets returned for the query "donald trump." It's only the last 200 because I was rate limited by the Twitter API, oops. These tweets are filtered by the user's state using the user's location field. For each state, a score is assigned. Positive tweets add to the score, negative tweets subtract from it. States with a net positive scores are colored blue on the map, and net negative states are colored red. States with a net score of '0' or states which did not produce any tweets are colored white.

.png samples of the program's output have been included.
