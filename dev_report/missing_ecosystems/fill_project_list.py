from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def generate_project_list():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    parameters = {
        # A16Z '605e2ce9d41eae1066535f7c',
        # Aptos Ecosystem: 635634b93e16136f3bb2ee9e
        # Gaming: 6051a82166fc1b42617d6dc1
        # NFTs: 60291fa0db1be76c46298e83
        # Top 200: 
        #'id': '60291fa0db1be76c46298e83',
        'vs_currency': 'usd',
        'per_page': 200,
        'order': 'market_cap_desc',
        #'limit': '300',
    }
    headers = {
        'Accepts': 'application/json',
        #'X-CMC_PRO_API_KEY': "a17e6724-1b3d-4a62-9732-7c991d5b7f49",
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    """coins = data['coins']
    names_and_market_cap = {}

    for coin in coins:
        names_and_market_cap[coin["name"]] = coin['quote']['USD']["market_cap"]

    names_and_market_cap = dict(sorted(names_and_market_cap.items(), key=lambda item: item[1], reverse=True))

    for name in names_and_market_cap:
        print(name + ": " + str(names_and_market_cap[name]))

    for name in names_and_market_cap:
        print(name)"""

    
    return data   

data = generate_project_list()

changes = open("new.txt").readlines()
changes = [x.lower() for x in changes]

original = open("original.txt").readlines()
original = [x.lower() for x in original]

for item in changes:
    if item not in original:
        print(item)