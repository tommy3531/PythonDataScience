import requests
import json
from jsontraverse.parser import JsonTraverseParser


def all_senators():
    ALL_SENATOR_URL = "https://api.propublica.org/congress/v1/115/senate/members.json"

    headers = {
        'X-API-KEY': 'SpzjlPZlkMlPKKGCLQS1OqZtCN96lPl7sszOTKra'
    }

    r = requests.get(url=ALL_SENATOR_URL, headers=headers)
    data = r.json()
    json_string = json.dumps(data)

    parser = JsonTraverseParser(json_string)
    member_data = parser.traverse("results.members")
    return member_data


def get_senator_full_name(senator_data):
    full_name = []
    for i in senator_data:
        first_name = i['first_name']
        last_name = i['last_name']
        full_name.append(first_name + " " + last_name)
    return full_name


def get_specific_member(member_id):
    SPECIFIC_MEMBER_URL = "https://api.propublica.org/congress/v1/members/" + member_id + ".json"

    headers = {
        'X-API-KEY': 'SpzjlPZlkMlPKKGCLQS1OqZtCN96lPl7sszOTKra'
    }

    r = requests.get(url=SPECIFIC_MEMBER_URL, headers=headers)
    data = r.json()
    json_string = json.dumps(data)
    parser = JsonTraverseParser(json_string)
    results_data = parser.traverse("results")
    return results_data


def get_member_roles(member_results):
    roles = member_results[0]['roles']
    return roles


def show_member_details(member_results):
    for result in member_results:
        print(result['first_name'])
        print(result['last_name'])
        print(result['member_id'])


def show_member_roles(member_roles):
    print("\nRoles")
    for role in member_roles:
        print(role['ocd_id'])


def get_member_committees(member_roles):
    committee = member_roles[0]['committees']
    return committee


def show_member_committees(member_committees):
    print("\nCommittees")
    for committee in member_committees:
        print(committee['name'])
        print(committee['code'])


def get_member_sub_committees(member_roles):
    sub_committee = member_roles[0]['subcommittees']
    return sub_committee


def show_member_sub_committees(member_subcommittees):
    print("\nSubcommittees")
    for subcommittee in member_subcommittees:
        print(subcommittee['name'])
        print(subcommittee['code'])