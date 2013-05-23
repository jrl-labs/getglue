import requests
import yaml
from requests_oauthlib import OAuth1
from unidecode import unidecode

# Store your tokens in a "yaml" file.  This file should look like:
# key: YOUR-KEY-HERE
# secret: YOUR-SECRET-HERE

with open('../conf/oauth.yml', 'r') as f:
    # credentials will be a dictionary with the key and secret
    credentials = yaml.safe_load(f)
key = unidecode(credentials['getglue']['key'])
secret = unidecode(credentials['getglue']['secret'])
auth = OAuth1(key, secret)

url = 'http://api.getglue.com/v2/user/profile?userId=getglue'
url = 'http://api.getglue.com/v2/user/profile?userId=langmore'
url = 'http://api.getglue.com/v2/glue/topUsers?category=books'
url = 'http://api.getglue.com/v2/user/profile?userId=getglue&stickerObjectId=tv_shows/dexter'
#url = 'https://api.getglue.com/oauth/access_token'
#url = 'http://getglue.com/oauth/authorize'
url = 'http://api.getglue.com/oauth/request_token'
#url = 'http://api.getglue.com/oauth/authorize'
#url = 'http://api.getglue.com/oauth/access_token'

r = requests.get(url, auth=auth)#, params={'userID': 'ianlangmore'})


def get_request_token(self):
    """ 
    Get the initial request token from GetGlue.

    Returns a dictionary.
    """
    url = urljoin(API_URL, '/oauth/request_token')
    oauth = OAuth1(settings.CONSUMER_KEY, settings.SECRET_KEY)
    response = requests.get(url, auth=oauth)
    return self._parse_query_string(response.text)

