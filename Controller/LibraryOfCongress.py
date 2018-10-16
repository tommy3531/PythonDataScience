# https://github.com/LibraryOfCongress/data-exploration/blob/master/LOC.gov%20JSON%20API.ipynb
import json
import pprint
import requests

BASE_URL_SEARCH = 'https://www.loc.gov/'
JSON = 'fo=json'


def library_of_congress_search():
    searchTerm = "baseball"
    SEARCH_URL = BASE_URL_SEARCH + "/search" + "?q=" + searchTerm + "&" + JSON
    search_data = requests.get(SEARCH_URL)
    pprint.pprint(search_data.json())


## TODO: Fix func use async need to research how to to do this
def library_of_congress_collections():
    COLLECTION_URL = BASE_URL_SEARCH + "/collections" + "?" + JSON
    collection_json = requests.get(COLLECTION_URL).json()

    while True:
        for collection in collection_json['results']:
            print(collection['title'])

        # Get the next page
        next_page = collection_json['pagination']['next']
        if next_page is not None: # Make sure we havent hit the end of the pages
            collection_json = requests.get(next_page).json()
        else:
            break # We are done and can stop looping

