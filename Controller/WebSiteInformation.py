import newspaper


def get_website_information():
    cnn_paper = newspaper.build('http://cnn.com')
    for article in cnn_paper.articles:
        print(article.url)
