import json
import pprint
import requests


def get_world_bank_sources():
    url = 'http://api.worldbank.org/v2/sources?format=json'
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)


def get_world_bank_country_code():
    url = 'http://api.worldbank.org/v2/countries?format=json'
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)


def search_world_bank_by_country_code(country_code):
    url = 'http://api.worldbank.org/v2/countries/' + country_code + '?format=json'
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)


def get_world_bank_income_level_code():
    url = 'http://api.worldbank.org/v2/incomeLevels?format=json'
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)


def get_world_bank_indictors():
    url = 'http://api.worldbank.org/v2/indicators?format=json'
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)


def search_world_bank_by_indicator():
    # indicator = '2.0.cov.Math.pl_3.prv'
    indicator = 'NY.GDP.MKTP.CD'
    url = 'http://api.worldbank.org/v2/indicators/' + indicator + '?format=json'
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)


def get_world_bank_topics():
    url = 'http://api.worldbank.org/v2/topics?format=json'
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)


def get_world_bank_data_catalog():
    url = 'http://api.worldbank.org/v2/datacatalog?format=json'
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)


def get_world_bank_metatypes():
    url = 'http://api.worldbank.org/v2/datacatalog/metatypes/name?format=json'
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)


def search_world_bank(topic):
    url = 'http://api.worldbank.org/v2/datacatalog/search/' + topic + '?format=json'
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)