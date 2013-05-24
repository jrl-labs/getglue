"""
Very very simple module to demonstrate working with an API.
We'll use the rotten tomatoes API since it is very simple.

http://developer.rottentomatoes.com
"""

import requests
import yaml



def query_moviename(moviename, key, page_limit=50):
    """
    Queries API by moviename and returns results as a list.

    Parameters
    ----------
    moviename : String
        We will search for movies of this name.  We replace underscores and
        blank spaces with a '+' in order to try and comply with URL formatting
    key : String
        API key
    page_limit : Integer
        Limit on the number of pages to return
    """
    formattedname = moviename.replace('_', '+')
    formattedname = formattedname.replace(' ', '+')

    url = 'http://api.rottentomatoes.com/api/public/v1.0/movies.json'

    params = {'apikey': key, 'page_limit': page_limit, 'q': moviename}

    r = requests.get(url, params=params)

    movies = r.json

    return movies


def movieid_2_reviews(movieid, key, page_limit=50):
    """
    Gets reviews corresponding to movieid.

    Parameters
    ----------
    movieid : String
        The rottentomatoes id of the movie
    key : String
        API key
    page_limit : Integer
        Limit on the number of pages to return
    """
    url = 'http://api.rottentomatoes.com/api/public/v1.0/movies/'\
        + str(movieid) \
        + '/reviews.json'

    params = {'apikey': key, 'page_limit': page_limit, 'review_type': 'all'}

    r = requests.get(url, params=params)

    reviews = r.json

    return reviews
