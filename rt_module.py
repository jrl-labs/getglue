"""
http://developer.rottentomatoes.com/docs
"""

import requests
import yaml
import json


def main():

    with open('../conf/oauth.yml', 'r') as f:
        # credentials will be a dictionary with the key and secret
        credentials = yaml.safe_load(f)

    key = credentials['rt']['key']

    movies = query_moviename('terminator', key)

    movieid = movies[0]['id']

    movieid_2_reviews_onepage(movieid, key)


def query_moviename(moviename, key):
    """
    Queries API by moviename and returns one page of results as a list.
    """
    formattedname = moviename.replace('_', '+')
    formattedname = formattedname.replace(' ', '+')

    url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json'

    params = {'apikey': key, 'page_limit': 50, 'q': moviename}

    r = requests.get(url, params=params)
    #result = json.loads(r.text)
    result = r.json
    allmovies = result['movies']

    return allmovies


def movieid_2_reviews_onepage(movieid, key):
    """
    """
    url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/'\
        + str(movieid) \
        + '/reviews.json'

    params = {'apikey': key, 'page_limit': 50, 'review_type': 'all'}

    r = requests.get(url, params=params)

    reviews = r.json['reviews']

    return reviews



if __name__ == '__main__':
    main()
