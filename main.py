import sys

from Controller.Propublica import all_senators, get_senator_full_name, get_specific_member, get_member_roles, \
    get_member_committees, get_member_sub_committees, show_member_details, show_member_roles, show_member_committees, \
    show_member_sub_committees, show_senator, show_senator_full_name_with_crp_id

from Controller.News import get_news_articles, enviro_variable, show_new_articles

from Controller.Menu import get_crp_id
from Controller.CKan import get_package_list, get_group_list, search_dataset, get_tags
from Controller.OpenSecrets import get_top_contributors_for_rep, get_rep_summary, get_legislators_from_state, get_organizations, \
    get_candidate_and_sector, get_open_secrets_legislators, get_independent_expedure
from Controller.WorldBank import get_world_bank_sources, get_world_bank_country_code, search_world_bank_by_country_code, \
    get_world_bank_income_level_code, get_world_bank_indictors, search_world_bank_by_indicator, get_world_bank_topics, \
    get_world_bank_data_catalog, get_world_bank_metatypes, search_world_bank


# CKAN Controller
# get_package_list()
# get_group_list()
# query_packages_and_resources('spending')
# get_tags()
# search_dataset("Spending")


# PROPUBLICA Controller
# # Get all members of the senate
# senate_data = all_senators()
# show_senator_full_name_with_crp_id(senate_data)
#
# # Get open secret ID
# crp_id = get_crp_id()


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

# get_top_contributors_for_rep(crp_id)
# get_rep_summary(crp_id)
# get_legislators_from_state("MO")
# get_organizations("Goldman")
# get_candidate_and_sector(crp_id)
# get_open_secrets_legislators("MO")
# get_independent_expedure()

# NEWS Controller
# articles = get_news_articles('Primary Health and Retirement Security Subcommittee')
# show_new_articles(news_data=articles)

# WorldBank
# get_world_bank_sources()
# get_world_bank_country_code()
# search_world_bank_by_country_code("BR")
# get_world_bank_income_level_code()
# get_world_bank_indictors()
# search_world_bank_by_indicator()
# get_world_bank_topics()
# get_world_bank_data_catalog()
# get_world_bank_metatypes()
# search_world_bank("poverty")