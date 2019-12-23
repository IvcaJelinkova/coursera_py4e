# ex13_securing_API_requests.py

import urllib.request, urllib.parse, urllib.error
# import twurl        # drchuck wrote this
import json
import oauth            # drchuck wrote this
import hidden           # drchuck wrote this; apps.twitter.com; create new app and get the four strings – def oauth → return consumer_key, consumer_secret, token_key, token_secret
import ssl

def augment(url, parameters):
    secrets = hidden.oauth()
    consumer = oauth.OAuthConsumer(secrets['consumer_key'], secrets['consumer_secret'])
    token = oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])
    oauth_request = oauth.OAuthRequest.from_consumer_and_token(consumer, token=token, http_method='GET',
                                                               http_url=url, parameters=parameters)
    oauth_request.sing_request(oauth.OAuthSignatureMethod_HMAC_SHA1(), consumer, token)
    return oauth_request.to_url()


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'


while True:
    print('')
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1):
        break
    url = augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '5'})
    print('Retrieving:', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()                   # string representation of json
    headers = dict(connection.getheaders())
    print('Remaining', headers['x-rate-limit-remaining'])
    js = json.loads(data)                               # parsing → dict
    print(json.dumps(js, indent=4))

    for u in js['users']:
        print(u['screen_name'])
        s = u['status']['text']
        print('    ', s[:50])


