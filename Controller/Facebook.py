import facebook


def facebook_test():
    fields = ["name"]
    graph = facebook.GraphAPI(access_token="EAAJ8A1c8urcBADDFNlewXZAdFBCRtm68Hi7Eoyy3qXHUtUtUTclQ1rpU9NUTRGvPSuyZAnJZCrE1v4R2qKNH3vv41krFBDd48jVyTabyioYGSHpPkSrume70Bczi9TA8usJf3jDJkkjW1RNNoWq1NZCidkYlKrMZD", version="2.12")
    print(graph.get_object(id='me', connection_name='friends'))