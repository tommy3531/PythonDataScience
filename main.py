import sys
import pprint

from Controller.Propublica import all_senators, get_senator_full_name, get_specific_member, get_member_roles, \
    show_senator_full_name_with_twitter_id
from Controller.Menu import get_crp_id
from Controller.OpenSecrets import get_top_contributors_for_rep, get_rep_summary, get_legislators_from_state, get_organizations
from Controller.Twitter import get_rep_information
# from Controller.CourtListener import court_listener_aba_ratings, get_jurisdictions
from Controller.LibraryOfCongress import library_of_congress_search, library_of_congress_collections, \
    search_collection, search_for_item, search_collection_by_location, search_maps, \
    search_audio_recordings, search_photo_print_drawings, search_manuscripts_mixed_material, \
    search_newspaper


#################################################### Twitter Controller ###############################\
# Get Legislators Tweets

senate_data = all_senators()
show_senator_full_name_with_twitter_id(senate_data)
crp_id = get_crp_id()
results_data = get_specific_member(crp_id)
twitter = results_data[0]['twitter_account']
get_rep_information(twitter)

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
# senate_data = all_senators()
# show_senator_full_name_with_twitter_id(senate_data)
# results_data = get_specific_member(crp_id)
# twitter = results_data[0]['twitter_account']
# crp_id = results_data[0]['crp_id']
# get_rep_information(twitter)


#################################################### END Propublica ###################################
#################################################### Menu Controller ##################################


# Get CRP_ID
# crp_id = get_crp_id()


#################################################### End of Menu ######################################
#################################################### Open Secrets #####################################


# get_top_contributors_for_rep(crp_id)


#################################################### End of Open Secrets ##############################