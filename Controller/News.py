import requests
import pickle
from newsapi import NewsApiClient
import os
from os.path import join, dirname
from dotenv import load_dotenv


def get_news_articles(search_term):
    enviro_variable()
    newsKey = os.getenv('NEWS_KEY')

    api = NewsApiClient(api_key=newsKey)
    articles = api.get_everything(q=search_term)
    return articles


def show_new_articles(news_data):
    print(news_data)
    print(news_data['totalResults'])
    for item in news_data['articles']:
        print(item['author'])
        print(item['title'])
        print(item['url'])
        print(item['source']['name'])
        print("\n")


def un_pickle_file():
    infile = open('../PickleFile/NewsArticle', 'rb')
    new = pickle.load(infile)
    infile.close()
    print(new)


def enviro_variable():
    dotenv_path = join(dirname(__file__), '../apikeys.env')
    load_dotenv(dotenv_path)