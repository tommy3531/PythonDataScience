import praw


def reddit_test():
    r = praw.Reddit(client_id='yectwVFdxNU8Gg',
                    client_secret='wcxztTa1jrWNitXvia7Ki8xMX8A',
                    user_agent='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')
    page = r.subreddit('aww')
    top_posts = page.hot(limit=None)
    for post in top_posts:
        print(post.title, post.ups)