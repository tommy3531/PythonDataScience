import requests
import pickle
from newsapi import NewsApiClient
import json


def all_senators():
    ALL_SENATOR_URL = "https://api.propublica.org/congress/v1/115/senate/members.json"

    headers = {
        'X-API-KEY': 'SpzjlPZlkMlPKKGCLQS1OqZtCN96lPl7sszOTKra'
    }
    r = requests.get(url=ALL_SENATOR_URL, headers=headers)
    data = r.json()
    print(data)


def find_news_by_topic(search_term):
    api = NewsApiClient(api_key='2126949bf7be437480eaf1f2dcf0ce51')
    a = api.get_everything(q=search_term)
    print(json.dumps(a, indent=4, sort_keys=True))

find_news_by_topic(search_term='Trump')
