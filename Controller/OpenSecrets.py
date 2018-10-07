# API: 95616cf411e10bdf902c3681fe59fda5
import requests
import pprint


def get_top_contributors_for_rep(crp_id):
    print("Top Contributors" + "\n")
    api_key = '95616cf411e10bdf902c3681fe59fda5'
    url = 'https://www.opensecrets.org/api/?method=candContrib&cid=' + crp_id + '&cycle=2018&output=json&apikey=' + api_key
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)


def get_rep_summary(crp_id):
    print("Open Secret Rep Summary" + "\n")
    api_key = '95616cf411e10bdf902c3681fe59fda5'
    url = 'http://www.opensecrets.org/api/?method=candSummary&cid=' + crp_id + '&cycle=2018&output=json&apikey=' + api_key
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)


def get_legislators_from_state(state):
    print("Open Secret get legislator from State: " + "\n")
    api_key = '95616cf411e10bdf902c3681fe59fda5'
    url = 'http://www.opensecrets.org/api/?method=getLegislators&id=' + state + '&output=json&apikey=' + api_key
    data = requests.get(url)
    json_data = data.json()
    print(json_data)
