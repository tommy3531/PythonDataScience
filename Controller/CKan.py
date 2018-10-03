import requests
from jsontraverse.parser import JsonTraverseParser
import pprint


def get_package_list():
    response = requests.get('http://demo.ckan.org/api/3/action/package_list')
    data = response.json()
    pprint.pprint(data)


def get_group_list():
    response = requests.get('http://demo.ckan.org/api/3/action/group_list')
    data = response.json()
    pprint.pprint(data)


def get_tags():
    response = requests.get('http://demo.ckan.org/api/3/action/tag_list')
    data = response.json()
    pprint.pprint(data)


def query_packages_and_resources(query):
    response = requests.get('http://demo.ckan.org/api/3/action/package_search?q=' + query)
    data = response.json()
    pprint.pprint(data)
