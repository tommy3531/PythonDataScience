import sys

from Controller.Propublica import all_senators, get_senator_full_name, get_specific_member, get_member_roles, \
    get_member_committees, get_member_sub_committees, show_member_details, show_member_roles, show_member_committees, \
    show_member_sub_committees, show_senator, show_senator_full_name_with_legislator_id

from Controller.News import get_news_articles, enviro_variable, show_new_articles

from Controller.Menu import get_legislator_id

# Get all members of the senate
senate_data = all_senators()
show_senator_full_name_with_legislator_id(senate_data)

# Get legislator ID
leg_id = get_legislator_id()

# Member Basic information
results_data = get_specific_member(leg_id)
show_member_details(results_data)

# Member roles
member_roles = get_member_roles(results_data)
show_member_roles(member_roles)

# Member committees
member_committees = get_member_committees(member_roles)
show_member_committees(member_committees)

# Member subcommittees
member_subcommittees = get_member_sub_committees(member_roles)
show_member_sub_committees(member_subcommittees)

# News
articles = get_news_articles('Primary Health and Retirement Security Subcommittee')
show_new_articles(news_data=articles)
