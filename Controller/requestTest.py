import requests
import pickle
from newsapi import NewsApiClient
import json
import os
from os.path import join, dirname
from dotenv import load_dotenv
from jsontraverse.parser import JsonTraverseParser
from Controller.Propublica import all_senators, get_senator_full_name, get_specific_member, get_member_roles, get_member_committees, get_member_sub_committees


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


# senator_data = all_senators()
# senator_full_name = get_senator_full_name(senator_data)
# for i in senator_full_name:
#     print(i)

results_data = get_specific_member('K000388')
for result in results_data:
    print(result)
member_roles = get_member_roles(results_data)
for role in member_roles:
    print(role)
member_committes = get_member_committees(member_roles)
for committee in member_committes:
    print(committee)
member_subcommittees = get_member_sub_committees(member_roles)
for subcommittee in member_subcommittees:
    print(subcommittee)

