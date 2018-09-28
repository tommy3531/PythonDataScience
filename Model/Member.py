class Member:

    def __init__(self):
        self.copyright = ""
        self.member_root = []
        self.member_basic_info = []
        self.member_id = ""
        self.member_title = ""
        self.member_first_name = ""
        self.member_last_name = ""
        self.member_date_of_birth = ""
        self.member_party = ""
        self.member_twitter_account = ""
        self.member_facebook_account = ""
        self.member_govTrack_ID = ""
        self.member_cspand_ID = ""
        self.member_votesmart_ID = ""
        self.member_icpsr_ID = ""
        self.member_crp_ID = ""
        self.member_fec_ID = ""
        self.member_in_office = ""
        self.member_next_election = ""
        self.member_missed_votes = ""
        self.member_total_votes = ""
        self.member_ocd_ID = ""
        self.member_office = ""
        self.member_lis_ID = ""

    def member_root_node(self, root):
        self.member_root.append(root)

    def member_basic_information(self, member_basic_info):
        self.member_basic_info.append(member_basic_info)




