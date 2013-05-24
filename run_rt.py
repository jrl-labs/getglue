import rt_module
import requests
import yaml
import json


###############################################################################
# Load my API credentials into a dictionary
###############################################################################
with open('conf/auth.yml', 'r') as f:
    credentials = yaml.safe_load(f)

key = credentials['rt']['key']

###############################################################################
# Cut and paste from an RT example
###############################################################################

# Three example urls
url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json'
url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/770672122/reviews.json?apikey=' + key
url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json?apikey=' + key + '&q=terminator&page_limit=1'

# Get back the requests object
r = requests.get(url)

# Extract a dictionary from the json
movies = r.json


###############################################################################
# Use the module!
###############################################################################

movies = rt_module.query_moviename('terminator', key)

movieid = movies['movies'][0]['id']

# reviews is a list of dictionaries.  
# Each of these will be loaded by R into the row of a table.
reviews = rt_module.movieid_2_reviews_onepage(movieid, key)

# Dump json to file
with open('reviews.json', 'w') as f:
    json.dump(reviews, f)
