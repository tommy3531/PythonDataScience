import facebook


def facebook_test():
    graph = facebook.GraphAPI(access_token="EAAJ8A1c8urcBAB1c4RPQfqtHD1AdqnGlKZAniN5uDfpKj4cM4jFYLLfivegQN3BnV2MDx70iCdB6k53HKZBwXjj3ZCAbXCdssQvXuCQuYOEMz6EMNWeFlGBrdwgniF8wvC2azo1Dsz601vuKx519K7O3PpMtVZAp6Xh67OvnZCC91dSa736TGYTETRhZBZBOhIZD", version="2.12")
    print(graph)