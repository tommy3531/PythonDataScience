import requests
import json
import pprint

# API_KEY: a87bbee93e079f0dc5f262529c21ffdf02fb5c0c
# https://www.courtlistener.com/api/rest-info/

API_KEY = 'a87bbee93e079f0dc5f262529c21ffdf02fb5c0c'
BASE_URL_ABA_RATINGS = 'https://www.courtlistener.com/api/rest/v3/aba-ratings/'
BASE_URL_AUDIO = 'https://www.courtlistener.com/api/rest/v3/audio/'
BASE_URL_CLUSTERS = 'https://www.courtlistener.com/api/rest/v3/clusters/'
BASE_URL_COURTS = 'https://www.courtlistener.com/api/rest/v3/courts/'
BASE_URL_DOCKETS = 'https://www.courtlistener.com/api/rest/v3/dockets/'
BASE_URL_EDUCATIONS = 'https://www.courtlistener.com/api/rest/v3/educations/'
BASE_URL_OPINIONS_CITED = 'https://www.courtlistener.com/api/rest/v3/opinions-cited/'
BASE_URL_OPINIONS = 'https://www.courtlistener.com/api/rest/v3/opinions/'
BASE_URL_ORIGINITING_COURT_INFO = 'https://www.courtlistener.com/api/rest/v3/originating-court-information/'
BASE_URL_PEOPLE = 'https://www.courtlistener.com/api/rest/v3/people/'
BASE_URL_POLITICAL_AFFILIATIONS = 'https://www.courtlistener.com/api/rest/v3/political-affiliations/'
BASE_URL_SEARCH = 'https://www.courtlistener.com/api/rest/v3/search/'
BASE_URL_SOURCES = 'https://www.courtlistener.com/api/rest/v3/sources/'
HEADERS = {
    'X-API-KEY': API_KEY
}


def court_listener_aba_ratings():
    SPECIFIC_MEMBER_URL = BASE_URL_ABA_RATINGS

    court_data = requests.get(url=SPECIFIC_MEMBER_URL, headers=HEADERS)
    court_json = court_data.json()
    print(court_json)


def get_jurisdictions():
    COURTS_JURISDICTION_URL = BASE_URL_COURTS

    court_data = requests.get(url=COURTS_JURISDICTION_URL, headers=HEADERS)
    court_json = court_data.json()
    pprint.pprint(court_json)