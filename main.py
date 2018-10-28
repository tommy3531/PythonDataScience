import sys
import pprint

from Controller.Propublica import all_senators, get_senator_full_name, get_specific_member, get_member_roles, \
    show_senator_full_name_with_twitter_id, get_members_twitter, get_members_open_secrets_id, get_members_legislator_id, \
    show_member_details, get_member_information, show_senator
from Controller.Menu import get_crp_id
from Controller.OpenSecrets import get_top_contributors_for_rep, get_rep_summary, get_legislators_from_state, get_organizations
from Controller.Twitter import get_all_tweets_from_user_timeline, get_all_user_friends, get_all_user_followers, get_tends_from_specific_location, \
    friendship_id
# from Controller.CourtListener import court_listener_aba_ratings, get_jurisdictions
from Controller.LibraryOfCongress import library_of_congress_search, library_of_congress_collections, \
    search_collection, search_for_item, search_collection_by_location, search_maps, \
    search_audio_recordings, search_photo_print_drawings, search_manuscripts_mixed_material, \
    search_newspaper


#################################################### Twitter Controller & Propublica #################\
# Get Legislators Tweets
woeID = "523920"
id = "W000817"
id2 = "K000388"
leg_id = "S001202"
twitter_name = "SenatorStrange"
# senate_data = all_senators()
# show_senator_full_name_with_twitter_id(senate_data)
# crp_id = get_crp_id()
# legislator_details = get_specific_member(crp_id)
#
# twitter_name = get_members_twitter(legislator_details)
# legislator_id = get_members_legislator_id(legislator_details)
# open_secrets_id = get_members_open_secrets_id(legislator_details)
# print(twitter_name)
# print(legislator_id)
# print(open_secrets_id)
#
# get_all_tweets_from_user_timeline(twitter_name)
# get_all_user_followers(twitter_name)
# get_tends_from_specific_location(woeID)
# friendship_id(twitter_name)
# show_member_details(legislator_details)

#################################################### Library Of Congress ##############################
# library_of_congress_search()
# library_of_congress_collections()
# search_collection()
# search_for_item()
# search_collection_by_location()
# search_maps()
# search_audio_recordings()
# search_photo_print_drawings()
# search_manuscripts_mixed_material()
# search_newspaper()


################################################### END OF LIBRARY OF CONGRESS ########################
################################################### Court listener Controller
# court_listener_aba_ratings()
# get_jurisdictions()


################################################### PROPUBLICA Controller ############################
senate_data = all_senators()
# show_senator_full_name_with_twitter_id(senate_data)
show_senator(senate_data)

# results_data = get_specific_member(id2)
# get_member_information(results_data)


#################################################### END Propublica ###################################
#################################################### Menu Controller ##################################


# Get CRP_ID
# crp_id = get_crp_id()


#################################################### End of Menu ######################################
#################################################### Open Secrets #####################################


# get_top_contributors_for_rep(crp_id)


#################################################### End of Open Secrets ##############################