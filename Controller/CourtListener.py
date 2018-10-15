import requests
import json
import pprint

# API_KEY: a87bbee93e079f0dc5f262529c21ffdf02fb5c0c
# https://www.courtlistener.com/api/rest-info/

API_KEY = 'a87bbee93e079f0dc5f262529c21ffdf02fb5c0c'
BASE_URL = 'https://www.courtlistener.com/api/rest/v3/dockets/'
HEADERS = {
    'X-API-KEY': API_KEY
}


def court_listener_test():
    SPECIFIC_MEMBER_URL = BASE_URL

    court_data = requests.get(url=SPECIFIC_MEMBER_URL, headers=HEADERS)
    court_json = court_data.json()
    for i in court_json['results']:
        pprint.pprint(i)