import requests
import pickle
from newsapi import NewsApiClient
import os
from os.path import join, dirname
from dotenv import load_dotenv


def find_news_by_topic(search_term):
    dotenv_path = join(dirname(__file__), '../apikeys.env')
    newsKey = os.getenv('NEWS_KEY')

    news_article = []
    api = NewsApiClient(api_key=newsKey)
    articles = api.get_everything(q=search_term)
    for article in articles['articles']:
        author = article['author']
        description = article['description']
        title = article['title']
        news_article.append(author)
        news_article.append(description)
        news_article.append(title)
    outfile = open('../PickleFile/NewsArticle', 'wb')
    pickle.dump(news_article, outfile)
    outfile.close()


def un_pickle_file():
    infile = open('../PickleFile/NewsArticle', 'rb')
    new = pickle.load(infile)
    infile.close()
    print(new)


def enviro_variable():
    dotenv_path = join(dirname(__file__), '../apikeys.env')
    load_dotenv(dotenv_path)

    twitter = os.getenv('NEWS_KEY')

    print(twitter)