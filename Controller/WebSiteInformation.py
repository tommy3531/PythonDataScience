import newspaper


def get_website_links():
    # political = newspaper.build('http://www.politico.com/sitemap')
    # for article in political.articles:
    #     print(article.url)
    drudge = newspaper.build('http://www.drudgereport.com')
    for article in drudge.articles:
        print(article.url)
