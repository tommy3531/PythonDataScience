import sys

from Controller.Propublica import all_senators, get_senator_full_name, get_specific_member, get_member_roles, \
    get_member_committees, get_member_sub_committees, show_member_details, show_member_roles, show_member_committees, \
    show_member_sub_committees, show_senator, show_senator_full_name_with_crp_id

from Controller.News import get_news_articles, enviro_variable, show_new_articles

from Controller.Menu import get_crp_id
from Controller.CKan import get_package_list, get_group_list, query_packages_and_resources, get_tags
from Controller.OpenSecrets import get_top_contributors_for_rep
# CKAN Controller
# get_package_list()
# get_group_list()
# query_packages_and_resources('spending')
# get_tags()

# PROPUBLICA Controller
# # Get all members of the senate
senate_data = all_senators()
show_senator_full_name_with_crp_id(senate_data)
#
# # Get legislator ID
crp_id = get_crp_id()
#
# # Member Basic information
# results_data = get_specific_member(leg_id)
# show_member_details(results_data)
#
# # Member roles
# member_roles = get_member_roles(results_data)
# show_member_roles(member_roles)
#
# # Member committees
# member_committees = get_member_committees(member_roles)
# show_member_committees(member_committees)
#
# # Member subcommittees
# member_subcommittees = get_member_sub_committees(member_roles)
# show_member_sub_committees(member_subcommittees)

get_top_contributors_for_rep(crp_id)

# NEWS Controller
# articles = get_news_articles('Primary Health and Retirement Security Subcommittee')
# show_new_articles(news_data=articles)
