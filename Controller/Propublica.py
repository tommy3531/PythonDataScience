import requests
import json
import pprint
from jsontraverse.parser import JsonTraverseParser

API_KEY = 'SpzjlPZlkMlPKKGCLQS1OqZtCN96lPl7sszOTKra'
BASE_URL = 'https://api.propublica.org/congress/v1'
HEADERS = {
    'X-API-KEY': API_KEY
}


def all_senators():
    ALL_SENATOR_URL = BASE_URL + "/115/senate/members.json"

    r = requests.get(url=ALL_SENATOR_URL, headers=HEADERS)
    data = r.json()
    json_string = json.dumps(data)
    parser = JsonTraverseParser(json_string)
    member_data = parser.traverse("results.members")
    return member_data


def show_senator(senator_data):
    pprint.pprint(senator_data)


def show_senator_full_name_with_crp_id(senator_data):
    for item in senator_data:
        print(item['first_name'] + " " + item['last_name'])
        if item['crp_id'] is None:
            print("NO crp_id" + "\n")
        else:
            print(item['crp_id'] + '\n')


def show_senator_full_name_with_facebook_id(senator_data):
    for item in senator_data:
        pprint.pprint(item)


def show_senator_full_name_with_twitter_id(senator_data):
    for item in senator_data:
        print(item['id'] + "\n")
        print(item['first_name'] + " " + item['last_name'])
        if item['twitter_account'] is None:
            print("No twitter ID" + "\n")

        else:
            print(item['twitter_account'])


def get_senator_full_name(senator_data):
    full_name = []
    for i in senator_data:
        first_name = i['first_name']
        last_name = i['last_name']
        full_name.append(first_name + " " + last_name)
    return full_name


def get_specific_member(member_id):
    SPECIFIC_MEMBER_URL = BASE_URL + "/members/" + member_id + ".json"

    r = requests.get(url=SPECIFIC_MEMBER_URL, headers=HEADERS)
    data = r.json()
    return data


def get_member_information(member_results):

    # JsonTraverseParser needs a string
    json_string = json.dumps(member_results)

    # Get a JsonTraverseParser Object
    parser = JsonTraverseParser(json_string)
    member_id = parser.traverse("results.member_id")
    first_name = parser.traverse("results.first_name")
    last_name = parser.traverse("results.last_name")
    date_of_birth = parser.traverse("results.date_of_birth")
    url = parser.traverse("results.url")
    govtrack_id = parser.traverse("results.govtrack_id")
    cspan_id = parser.traverse("results.cspan_id")
    votesmart_id = parser.traverse("results.votesmart_id")
    icpsr_id = parser.traverse("results.icpsr_id")
    twitter_account = parser.traverse("results.twitter_account")
    facebook_account = parser.traverse("results.facebook_account")
    crp_id = parser.traverse("results.crp_id")
    in_office = parser.traverse("results.in_office")
    congress = parser.traverse("results.roles.congress")
    chamber = parser.traverse("results.roles.chamber")
    title = parser.traverse("results.roles.title")
    ocd_id = parser.traverse("results.roles.ocd_id")
    fec_candidate_id = parser.traverse("results.roles.fec_candidate_id")
    bills_sponsored = parser.traverse("results.roles.bills_sponsored")
    committee_names = parser.traverse("results.roles.committees.name")
    sub_committee_names = parser.traverse("results.roles.subcommittees.name")
    sub_committee_parent_id = parser.traverse("results.roles.subcommittees.parent_committee_id")

    legislator_container = []

    # Create a legislator
    legislator_data = {

        'member_id': member_id,
        'first_name': first_name,
        'last_name': last_name,
        'date_of_birth': date_of_birth,
        'url': url,
        'govtrack_id': govtrack_id,
        'cspan_id': cspan_id,
        'votesmart_id': votesmart_id,
        'icpsr_id': icpsr_id,
        'twitter_account': twitter_account,
        'facebook_account': facebook_account,
        'crp_id': crp_id,
        'in_office': in_office,
        'congress': congress,
        'chamber': chamber,
        'title': title,
        'ocd_id': ocd_id,
        'fec_candidate_id': fec_candidate_id,
        'bills_sponsored': bills_sponsored,
        'committee_names': committee_names,
        'sub_committee_names': sub_committee_names,
        'sub_committee_parent_id': sub_committee_parent_id
    }

    legislator_container.append(legislator_data)

    pprint.pprint(legislator_container)




def get_member_roles(member_results):
    roles = member_results[0]['roles']
    return roles


def show_member_details(member_results):
    for result in member_results:
        print("Fullname: " + result['first_name'] + " " + result['last_name'])
        print("Legislator Id: " + result['member_id'] + "\n")


def show_member_roles(member_roles):
    print("\nRoles")
    for role in member_roles:
        print("OCD-ID: " + role['ocd_id'])


def get_members_twitter(member_results):
    twitter_id = ""
    for result in member_results:
        twitter_id = result['twitter_account']
    return twitter_id


def get_members_legislator_id(member_results):
    legislator_id = " "
    for results in member_results:
        legislator_id = results["member_id"]
    return legislator_id


def get_members_open_secrets_id(member_results):
    open_secrets_id = ""
    for result in member_results:
        open_secrets_id = result["crp_id"]
    return open_secrets_id


def get_member_committees(member_roles):
    committee = member_roles[0]['committees']
    return committee


def show_member_details(member_results):
    for result in member_results:
        pprint.pprint(result)


def show_member_committees(member_committees):
    print("\nCommittees")
    for committee in member_committees:
        print("Committe Name: " + committee['name'])
        print("Committe Code: " + committee['code'] + "\n")


def get_member_sub_committees(member_roles):
    sub_committee = member_roles[0]['subcommittees']
    return sub_committee


def show_member_sub_committees(member_subcommittees):
    print("\nSubcommittees")
    for subcommittee in member_subcommittees:
        print("Subcommittee Name: " + subcommittee['name'])
        print("Subcommittee Code: " + subcommittee['code'] + "\n")
