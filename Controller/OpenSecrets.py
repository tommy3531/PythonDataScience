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
    pprint.pprint(json_data)


def get_organizations(company):
    print("Open Secret get Organiztions: " + "\n")
    api_key = '95616cf411e10bdf902c3681fe59fda5'
    url = 'https://www.opensecrets.org/api/?method=getOrgs&org=' + company + '&output=json&apikey=' + api_key
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)


def get_candidate_and_sector(crp_id):
    print("Open secret get candiate and sector: " + "\n")
    api_key = '95616cf411e10bdf902c3681fe59fda5'
    url = 'http://www.opensecrets.org/api/?method=candSector&cid=' + crp_id + '&cycle=2012&output=json&apikey=' + api_key
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)


def get_open_secrets_legislators(state):
    print("Open secret get legislators: " + "\n")
    api_key = '95616cf411e10bdf902c3681fe59fda5'
    url = 'http://www.opensecrets.org/api/?method=getLegislators&id=' + state + '&output=json&apikey=' + api_key
    data = requests.get(url)
    json_data = data.json()
    pprint.pprint(json_data)
