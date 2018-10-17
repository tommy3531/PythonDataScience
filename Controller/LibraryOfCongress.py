# https://libraryofcongress.github.io/data-exploration/requests.html
import json
import pprint
import requests


BASE_URL_SEARCH = 'https://www.loc.gov/'
JSON = 'fo=json'


# TODO: Search by specific term
def library_of_congress_search():
    searchTerm = "baseball"
    SEARCH_URL = BASE_URL_SEARCH + "/search" + "?q=" + searchTerm + "&" + JSON
    search_json = requests.get(SEARCH_URL).json()
    pprint.pprint(search_json)


# TODO: Fix func use async need to research how to to do this
def library_of_congress_collections():
    COLLECTION_URL = BASE_URL_SEARCH + "/collections" + "?" + JSON
    collection_json = requests.get(COLLECTION_URL).json()

    while True:
        for collection in collection_json['results']:
            print(collection['title'])

        # Get the next page
        next_page = collection_json['pagination']['next']
        if next_page is not None:  # Make sure we havent hit the end of the pages
            collection_json = requests.get(next_page).json()
        else:
            break  # We are done and can stop looping


# TODO: Search within a specific collection
def search_collection():
    collection_name = "world-war-i-sheet-music"
    COLLECTION_SEARCH_URL = BASE_URL_SEARCH + "collections/" + collection_name + "/?" + JSON
    collection_json = requests.get(COLLECTION_SEARCH_URL).json()
    pprint.pprint(collection_json)


# TODO: Search by item_id from search
def search_for_item():
    # https: // www.loc.gov / item / ggb2006012811 /?fo = json
    item_id = 'http://www.loc.gov/rr/business/BERA/issue3/baseball.html'
    ITEM_SEARCH_URL = BASE_URL_SEARCH + "item/" + item_id + "/?" + JSON
    item_json = requests.get(ITEM_SEARCH_URL).json()
    pprint.pprint(item_json)


def search_collection_by_location():
    searchTerm = "baseball"
    location = "Ohio"
    SEARCH_URL = BASE_URL_SEARCH + "/search" + "?q=" + searchTerm + "&fa=location:" + location + "&" + JSON
    search_json = requests.get(SEARCH_URL).json()
    pprint.pprint(search_json)


def search_maps():
    MAPS_URL = BASE_URL_SEARCH + "maps/" + "?q=civil%20war&fo=json"
    map_json = requests.get(MAPS_URL).json()
    pprint.pprint(map_json)


def search_audio_recordings():
    AUDIO_URL = BASE_URL_SEARCH + "audio/" + "?q=rain&fo=json"
    audio_json = requests.get(AUDIO_URL).json()
    pprint.pprint(audio_json)


def search_photo_print_drawings():
    PRINT_URL = BASE_URL_SEARCH + "photos/" + "?q=trees&fo=json"
    print_json = requests.get(PRINT_URL).json()
    pprint.pprint(print_json)


def search_manuscripts_mixed_material():
    MANUSCRIPTS_URL = BASE_URL_SEARCH + "manuscripts/" + "?q=trees&fo=json"
    print(MANUSCRIPTS_URL)
    manuscript_json = requests.get(MANUSCRIPTS_URL).json()
    pprint.pprint(manuscript_json)


def search_newspaper():
    NEWSPAPER_URL = BASE_URL_SEARCH + "newspapers/" + "?q=chicago&fo=json"
    print(NEWSPAPER_URL)
    newspaper_json = requests.get(NEWSPAPER_URL).json()
    pprint.pprint(newspaper_json)


def search_film_and_video():
    pass

def search_printed_music():
    pass

def search_archived_websites():
    pass

