import requests
import pickle
from newsapi import NewsApiClient
import json
from Model.Member import Member
import os
from os.path import join, dirname
from dotenv import load_dotenv
from jsontraverse.parser import JsonTraverseParser
from Model.Results import Results
import jsane
def all_senators():
    memberList = []
    ALL_SENATOR_URL = "https://api.propublica.org/congress/v1/115/senate/members.json"

    headers = {
        'X-API-KEY': 'SpzjlPZlkMlPKKGCLQS1OqZtCN96lPl7sszOTKra'
    }

    r = requests.get(url=ALL_SENATOR_URL, headers=headers)
    data = r.json()
    json_string = json.dumps(data)

    # j = jsane.loads(json_string)
    # print(j)
    # resul = j.results.r()
    # me = j.results[0].members.r()

    # member = Member()
    # results = Results()
    # print(type(results))
    parser = JsonTraverseParser(json_string)
    status = parser.traverse("status")
    copyright = parser.traverse("copyright")
    results = parser.traverse("results")
    mem = parser.traverse("results.members")
    first_name = parser.traverse("results.members.first_name")
    last_name = parser.traverse("results.members.last_name")
    full_name = first_name + last_name
    for i in full_name:
        print(i)

    # for Results in member.member_root:
    #     print(Results)
    # print(status)
    # print(copyright)

    # copyright = data["copyright"]
    # member = Member()
    # root1 = member.member_root
    # result_list = data['results']
    # print(result_list.keys())
    # member.member_root_node(data["results"])
    # for item in member.member_root:
    #     member.member_basic_information(data["results"][0]["members"])
    #     for item in data['results'][0]['members']:
    #         member.member_id = item['id']
    #         member.member_title = item['title']
    #         member.member_first_name = item['first_name']
    #         member.member_last_name = item['last_name']
    #         member.member_party = item['party']
    #         member.member_twitter_account = item['twitter_account']
    #         member.member_facebook_account = item['facebook_account']
    #         member.member_govTrack_ID = item['govtrack_id']
    #
    # return


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


member_list = all_senators()
