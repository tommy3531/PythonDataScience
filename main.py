from Controller.Propublica import all_senators, get_senator_full_name, get_specific_member, get_member_roles, \
    get_member_committees, get_member_sub_committees, show_member_details, show_member_roles, show_member_committees, \
    show_member_sub_committees, show_senator, show_senator_full_name_with_legislator_id

from Controller.News import find_news_by_topic, enviro_variable, un_pickle_file

enviro_variable()
find_news_by_topic(search_term='Trump')
# Get all members of the senate
# senate_data = all_senators()
# show_senator_full_name_with_legislator_id(senate_data)

# # Member Basic information
# results_data = get_specific_member('K000388')
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
