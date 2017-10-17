#Authors: Alexis Franciosi, Kevin Quintero, Derek Jones, Herman Curiel
import matplotlib.pyplot as plt
import tweepy
import re
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from tweepy import Stream
from tweepy import OAuthHandler
from textblob import TextBlob

consumer_key = 'SOD8Yt81vTAg3XsycLLFq9eVs'
consumer_secret = 'cSf1bcaiP4NPBKx7czDug7n62fWsOtoTd8C2n93GOdNJy8X5fk'
access_token = '90118692-l362TjvCXCw0EPCIEtPtNNiDZp6hmgn1KnFC7Zgzp'
access_token_secret = 'IZzL3Ch84Dh2nj9vZYj7q4Ko61YaTivOuakcyBuB1JT8D'

print("Working...")

#authenticate to twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# create the map
map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

# load the shapefile, use the name 'states'
map.readshapefile('st99_d00', name='states', drawbounds=True)

#gets state_names from the shapefile for shape object lookup
state_names = []
for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME'])

states = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 
               'Colorado', 'Connecticut', 'Delaware', 'District of Columbia',
               'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 
               'Iowa', 'Kansas', 'Kentucky', 'Louisiana', 'Maine', 'Maryland', 
               'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi', 'Missouri', 
               'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 
               'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 
               'Oklahoma', 'Oregon', 'Pennsylvania', 'Rhode Island', 'South Carolina', 
               'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont', 'Virginia', 
               'Washington', 'West Virginia', 'Wisconsin', 'Wyoming']

#issue twitter query through API
public_tweets = tweepy.Cursor(api.search,
                              q = 'Donald Trump',
                              count = 100, 
                              lang = ('en')).items(200)
pos_tweets = []
neg_tweets = []
tweets = []
num_tweets = 0
for tweet in public_tweets:
    new_tweet  = {}
    #remove special characters from tweet text
    formatted_tweet = (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.text).split()))
    new_tweet['text'] = formatted_tweet
    #get sentiment
    analysis = TextBlob(formatted_tweet)
    if analysis.sentiment.polarity > 0:
        new_tweet['sentiment'] = 'positive'
    elif analysis.sentiment.polarity == 0:
        new_tweet['sentiment'] = 'neutral'
    else:
        new_tweet['sentiment'] = 'negative'
    #get location info
    if tweet.user.location:
        #remove special characters from location text
        formatted_loc = (' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet.user.location).split()))
        if (" AL" in formatted_loc.upper()) or ("ALABAMA" in formatted_loc.upper()) or (formatted_loc.upper == "AL"):
            new_tweet['state'] = 'Alabama'
        elif (" AK" in formatted_loc.upper()) or ("ALASKA" in formatted_loc.upper()) or (formatted_loc.upper == "AK"):
            new_tweet['state'] = 'Alaska'
        elif (" AZ" in formatted_loc.upper()) or ("ARIZONA" in formatted_loc.upper()) or (formatted_loc.upper == "AZ"):
            new_tweet['state'] = 'Arizona'
        elif (" AR" in formatted_loc.upper()) or ("ARKANSAS" in formatted_loc.upper()) or (formatted_loc.upper == "AR"):
            new_tweet['state'] = 'Arkansas'
        elif (" CA" in formatted_loc.upper()) or ("CALIFORNIA" in formatted_loc.upper()) or (formatted_loc.upper == "CA"):
            new_tweet['state'] = 'California'
        elif (" CO" in formatted_loc.upper()) or ("COLORADO" in formatted_loc.upper()) or (formatted_loc.upper == "CO"):
            new_tweet['state'] = 'Colorado'
        elif (" CT" in formatted_loc.upper()) or ("CONNECTICUT" in formatted_loc.upper()) or (formatted_loc.upper == "CT"):
            new_tweet['state'] = 'Connecticut'
        elif (" DA" in formatted_loc.upper()) or ("DELAWARE" in formatted_loc.upper()) or (formatted_loc.upper == "DA"):
            new_tweet['state'] = 'Delaware'
        elif (" FL" in formatted_loc.upper()) or ("FLORIDA" in formatted_loc.upper()) or (formatted_loc.upper == "FL"):
            new_tweet['state'] = 'Florida'
        elif (" GA" in formatted_loc.upper()) or ("GEORGIA" in formatted_loc.upper()) or (formatted_loc.upper == "GA"):
            new_tweet['state'] = 'Georgia'
        elif (" HI" in formatted_loc.upper()) or ("HAWAII" in formatted_loc.upper()) or (formatted_loc.upper == "HI"):
            new_tweet['state'] = 'Hawaii'
        elif (" ID" in formatted_loc.upper()) or ("IDAHO" in formatted_loc.upper()) or (formatted_loc.upper == "ID"):
            new_tweet['state'] = 'Idaho'
        elif (" IL" in formatted_loc.upper()) or ("ILLINOIS" in formatted_loc.upper()) or (formatted_loc.upper == "IL"):
            new_tweet['state'] = 'Illinois'
        elif (" IN" in formatted_loc.upper()) or ("INDIANA" in formatted_loc.upper()) or (formatted_loc.upper == "IN"):
            new_tweet['state'] = 'Indiana'
        elif (" IA" in formatted_loc.upper()) or ("IOWA" in formatted_loc.upper()) or (formatted_loc.upper == "IA"):
            new_tweet['state'] = 'Iowa'
        elif (" KS" in formatted_loc.upper()) or ("KANSAS" in formatted_loc.upper()) or (formatted_loc.upper == "KS"):
            new_tweet['state'] = 'Kansas'
        elif (" KY" in formatted_loc.upper()) or ("KENTUCKY" in formatted_loc.upper()) or (formatted_loc.upper == "KY"):
            new_tweet['state'] = 'Kentucky'
        elif (" LA" in formatted_loc.upper()) or ("LOUISIANA" in formatted_loc.upper()):
            new_tweet['state'] = 'Louisiana'
        elif (" ME" in formatted_loc.upper()) or ("MAINE" in formatted_loc.upper()) or (formatted_loc.upper == "ME"):
            new_tweet['state'] = 'Maine'
        elif (" MD" in formatted_loc.upper()) or ("MARYLAND" in formatted_loc.upper()) or (formatted_loc.upper == "MD"):
            new_tweet['state'] = 'Maryland'
        elif (" MA" in formatted_loc.upper()) or ("MASSACHUSETTS" in formatted_loc.upper()) or (formatted_loc.upper == "MA"):
            new_tweet['state'] = 'Massachusetts'
        elif (" MI" in formatted_loc.upper()) or ("MICHIGAN" in formatted_loc.upper()) or (formatted_loc.upper == "MI"):
            new_tweet['state'] = 'Michigan'
        elif (" MN" in formatted_loc.upper()) or ("MINNESOTA" in formatted_loc.upper()) or (formatted_loc.upper == "MN"):
            new_tweet['state'] = 'Minnesota'
        elif (" MS" in formatted_loc.upper()) or ("MISSISSIPPI" in formatted_loc.upper()) or (formatted_loc.upper == "MS"):
            new_tweet['state'] = 'Mississippi'
        elif (" MO" in formatted_loc.upper()) or ("MISSOURI" in formatted_loc.upper()) or (formatted_loc.upper == "MO"):
            new_tweet['state'] = 'Missouri'
        elif (" MT" in formatted_loc.upper()) or ("MONTANA" in formatted_loc.upper()) or (formatted_loc.upper == "MT"):
            new_tweet['state'] = 'Montana'
        elif (" NE" in formatted_loc.upper()) or ("NEBRASKA" in formatted_loc.upper()) or (formatted_loc.upper == "NE"):
            new_tweet['state'] = 'Nebraska'
        elif (" NV" in formatted_loc.upper()) or ("NEVADA" in formatted_loc.upper()) or (formatted_loc.upper == "NV"):
            new_tweet['state'] = 'Nevada'
        elif (" NH" in formatted_loc.upper()) or ("NEW HAMPSHIRE" in formatted_loc.upper()) or (formatted_loc.upper == "NH"):
            new_tweet['state'] = 'New Hampshire'
        elif (" NJ" in formatted_loc.upper()) or ("JERSEY" in formatted_loc.upper()) or (formatted_loc.upper == "NJ"):
            new_tweet['state'] = 'New Jersey'
        elif (" NM" in formatted_loc.upper()) or ("NEW MEXICO" in formatted_loc.upper()) or (formatted_loc.upper == "NM"):
            new_tweet['state'] = 'New Mexico'
        elif (" NY" in formatted_loc.upper()) or ("NEW YORK" in formatted_loc.upper()) or (formatted_loc.upper == "NY"):
            new_tweet['state'] = 'New York'
        elif (" NC" in formatted_loc.upper()) or ("NORTH CAROLINA" in formatted_loc.upper()) or (formatted_loc.upper == "NC"):
            new_tweet['state'] = 'North Carolina'
        elif (" ND" in formatted_loc.upper()) or ("NORTH DAKOTA" in formatted_loc.upper()) or (formatted_loc.upper == "ND"):
            new_tweet['state'] = 'North Dakota'
        elif (" OH" in formatted_loc.upper()) or ("OHIO" in formatted_loc.upper()) or (formatted_loc.upper == "OH"):
            new_tweet['state'] = 'Ohio'
        elif (" OK" in formatted_loc.upper()) or ("OKLAHOMA" in formatted_loc.upper()) or (formatted_loc.upper == "OK"):
            new_tweet['state'] = 'Oklahoma'
        elif (" OR" in formatted_loc.upper()) or ("OREGON" in formatted_loc.upper()) or (formatted_loc.upper == "OR"):
            new_tweet['state'] = 'Oregon'
        elif (" PA" in formatted_loc.upper()) or ("PENNSYLVANIA" in formatted_loc.upper()) or (formatted_loc.upper == "PA"):
            new_tweet['state'] = 'Pennsylvania'
        elif (" RI" in formatted_loc.upper()) or ("RHODE" in formatted_loc.upper()) or (formatted_loc.upper == "RI"):
            new_tweet['state'] = 'Rhode Island'
        elif (" SC" in formatted_loc.upper()) or ("SOUTH CAROLINA" in formatted_loc.upper()) or (formatted_loc.upper == "SC"):
            new_tweet['state'] = 'South Carolina'
        elif (" SD" in formatted_loc.upper()) or ("SOUTH DAKOTA" in formatted_loc.upper()) or (formatted_loc.upper == "SD"):
            new_tweet['state'] = 'South Dakota'
        elif (" TN" in formatted_loc.upper()) or ("TENNESSEE" in formatted_loc.upper()) or (formatted_loc.upper == "TN"):
            new_tweet['state'] = 'Tennessee'
        elif (" TX" in formatted_loc.upper()) or ("TEXAS" in formatted_loc.upper()) or (formatted_loc.upper == "TX"):
            new_tweet['state'] = 'Texas'
        elif (" UT" in formatted_loc.upper()) or ("UTAH" in formatted_loc.upper()):
            new_tweet['state'] = 'Utah'
        elif (" VT" in formatted_loc.upper()) or ("VERMONT" in formatted_loc.upper())  or (formatted_loc.upper == "VT"):
            new_tweet['state'] = 'Vermont'
        elif ((" VA" in formatted_loc.upper()) or ("VIRGINIA" in formatted_loc.upper())  or (formatted_loc.upper == "WV") and "WEST" not in formatted_loc.upper()):
            new_tweet['state'] = 'Virginia'
        elif (" WA" in formatted_loc.upper()) or ("WASHINGTON" in formatted_loc.upper()) or (formatted_loc.upper == "WA"):
            new_tweet['state'] = 'Washington'
        elif (" WV" in formatted_loc.upper()) or ("WEST VIRGINIA" in formatted_loc.upper()) or (formatted_loc.upper == "WV"):
            new_tweet['state'] = 'West Virginia'
        elif (" WI" in formatted_loc.upper()) or ("WISCONSIN" in formatted_loc.upper()) or (formatted_loc.upper == "WI"):
            new_tweet['state'] = 'Wisconsin'
        elif (" WY" in formatted_loc.upper()) or ("WYOMING" in formatted_loc.upper()) or (formatted_loc.upper == "WY"):
            new_tweet['state'] = 'Wyoming'
        else:
            #location set but no matching state found
            new_tweet['state'] = 'none'
    else:
        #no location set
        new_tweet['state'] = 'none'

    #append to the tweets list
    if tweet.retweet_count > 0:
        if new_tweet not in tweets:
            tweets.append(new_tweet)
            #append to pos/neg list
            if new_tweet['sentiment'] == 'positive':
                pos_tweets.append(new_tweet)
            elif new_tweet['sentiment'] == 'negative':
                neg_tweets.append(new_tweet)
            num_tweets += 1
    else:
        tweets.append(new_tweet)
        #append to pos/neg list
        if new_tweet['sentiment'] == 'positive':
            pos_tweets.append(new_tweet)
        elif new_tweet['sentiment'] == 'negative':
            neg_tweets.append(new_tweet)
        num_tweets += 1
    
#associate states with their scores
state_scores = []
for state in states:
    score = 0
    score_dict = {}
    for tweet in tweets:
        if tweet['state'] == state:
            if tweet['sentiment'] == 'positive':
                score += 1
            elif tweet['sentiment'] == 'negative':
                score -= 1
    score_dict['state'] = state
    score_dict['score'] = score
    state_scores.append(score_dict)

#percentages
print("Positive tweets percentage: {} %".format(100*len(pos_tweets)/num_tweets))
print("Negative tweets percentage: {} %".format(100*len(neg_tweets)/num_tweets))

#print 5 pos/neg tweets
print("\n\n5 Positive tweets:")
for tweet in pos_tweets[:5]:
    print(tweet['text'])
print("\n\n5 Negative tweets:")
for tweet in neg_tweets[:5]:
    print(tweet['text'])

#color the map for each state
for state_score in state_scores:
    if state_score['score'] > 0:
        # get current axes instance
        ax = plt.gca() 

        #get state and draw the filled polygon
        seg = map.states[state_names.index(state_score['state'])]
        poly = Polygon(seg, facecolor='blue',edgecolor='blue')
        ax.add_patch(poly)
    elif state_score['score'] < 0:
        # get current axes instance
        ax = plt.gca() 

        #get state and draw the filled polygon
        seg = map.states[state_names.index(state_score['state'])]
        poly = Polygon(seg, facecolor='red',edgecolor='red')
        ax.add_patch(poly)
plt.show()
