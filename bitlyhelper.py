try:
    from urllib.request  import urlopen
except ImportError:
    from urllib2 import urlopen
import json

TOKEN = "af0551b6ba198c42f211e56e12cce634ca8b6b3e"
ROOT_URL = "https://api-ssl.bitly.com"
SHORTEN = "/v3/shorten?access_token={}&longUrl={}"


class BitlyHelper:

    def shorten_url(self, longurl):
        try:
            url = ROOT_URL + SHORTEN.format(TOKEN, longurl)
            response = urlopen(url).read()
            jr = json.loads(response.decode())
            return jr['data']['url']
        except Exception as e:
            return e
