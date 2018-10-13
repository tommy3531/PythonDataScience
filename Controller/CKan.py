# SAM_API: https://api.data.gov/sam/v1/registrations/1459697830000?api_key=mOlhsNuafzQnM65L62ptwtwJ7P12sETKY62NBTfU
# GSA: https://api.data.gov/gsa/auctions?api_key=hDWqpz7qe1s7VmhdGz5IKUQVRh2e0NNO4jlKKov6&format=JSON
# FuelStation: https://developer.nrel.gov/api/alt-fuel-stations/v1/nearest.json?api_key=WP6uLj9SNvthAR035ODJQWfpXnrX5cAIZcgOs8lO&location=Denver+CO
# GSA Analystics: https://api.gsa.gov/analytics/dap/v1/reports/download/data?api_key=8XLhihpZD5w2y2EIknNq5oIMazANpLJhzJjPvGTn


import requests
from jsontraverse.parser import JsonTraverseParser
import pprint


def get_package_list():
    response = requests.get('http://demo.ckan.org/api/3/action/package_list')
    data = response.json()
    pprint.pprint(data)


def get_group_list():

    """
    Get names of all datasets in the data-explorer
    :return:
    """
    response = requests.get('http://demo.ckan.org/api/3/action/group_list')
    data = response.json()
    pprint.pprint(data)


def get_tags():
    response = requests.get('http://demo.ckan.org/api/3/action/tag_list')
    data = response.json()
    pprint.pprint(data)


def search_dataset(query):
    """
    Search for datasets matching the search query
    :param query:
    :return:

    """
    response = requests.get('http://demo.ckan.org/api/3/action/package_search?q=' + query)
    data = response.json()
    pprint.pprint(data)
