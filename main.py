import sys
import pprint

from Controller.Propublica import all_senators, get_senator_full_name, get_specific_member, get_member_roles, \
    show_senator_full_name_with_twitter_id
from Controller.Menu import get_crp_id
from Controller.OpenSecrets import get_top_contributors_for_rep, get_rep_summary, get_legislators_from_state, get_organizations
from Controller.Twitter import get_rep_information
from Controller.CourtListener import court_listener_aba_ratings, get_jurisdictions

# court_listener_aba_ratings()
get_jurisdictions()

############################## Get information from propublica, twitter, opensecrets
# PROPUBLICA Controller
# senate_data = all_senators()
# show_senator_full_name_with_twitter_id(senate_data)


# Get CRP_ID
# crp_id = get_crp_id()

# # Member Basic information
# results_data = get_specific_member(crp_id)
# twitter = results_data[0]['twitter_account']
# crp_id = results_data[0]['crp_id']
# get_rep_information(twitter)

# Open Secrets
# get_top_contributors_for_rep(crp_id)
