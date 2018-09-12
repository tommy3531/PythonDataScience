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
    newsarticle = []
    api = NewsApiClient(api_key='2126949bf7be437480eaf1f2dcf0ce51')
    articles = api.get_everything(q=search_term)
    for article in articles['articles']:
        author = article['author']
        description = article['description']
        title = article['title']
        newsarticle.append(author)
        newsarticle.append(description)
        newsarticle.append(title)
    outfile = open('NewsArticle', 'wb')
    pickle.dump(newsarticle, outfile)
    outfile.close()


def un_pickle_file():
    infile = open('NewsArticle', 'rb')
    new = pickle.load(infile)
    infile.close()
    print(new)


find_news_by_topic(search_term='Trump')
un_pickle_file()
