from tweepy import API
from tweepy import OAuthHandler


def get_twitter_auth():
    """ Setup Twitter Authentication.

        Return: tweepy.OAuth Obj
    """
    consumer_key = "xIoIkf3n510nQummRrToTcMEW"
    consumer_secret = "tTKglNhypBJerQSRJsE1hmhWzxZrolw85NRObjbjb38HLvbiAH"
    access_token = "852662587934130176-scJ8ZEtjtyWpiiqJfAEG5DnyVH6BleU"
    access_secret = "wxedTgkOhsX1DLymQ8wze6r2UYigtFOKiSehF9LU9bo98"

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    client = API(auth)
    return client


# TODO: Parse need attributes from response
def get_all_tweets_from_user_timeline(senator_twitter_name):
    client = get_twitter_auth()

    # Go to senator timeline and get 150 tweets without retweets
    new_tweets = client.user_timeline(senator_twitter_name, count=150, include_rts=False)

    # new_tweets is a resultSet which allows attribute access via . notation
    status = new_tweets[0]

    # Get a list of the keys
    print(status._json.keys())


# TODO: Parse need attributes from response
def get_all_user_friends(senator_twitter_name):
    client = get_twitter_auth()

    # Get senator friends
    friends = client.friends(senator_twitter_name, count=150, include_rts=False)

    # friends is a resultSet which allows attribute access via . notation
    status = friends[0]

    print("\n" + "[+] Printing out all friends of the senator" + "\n")
    print(status._json.keys())


# TODO: Parse need attributes from response
def get_all_user_followers(senator_twitter_name):
    client = get_twitter_auth()

    # Get senator followers
    followers = client.friends(senator_twitter_name, count=150, include_rts=False)

    # friends is a resultSet which allows attribute access via . notation
    status = followers[0]

    print("\n" + "[+] Printing out all followers of senator")
    print(status._json.keys())


# TODO: Parse need attributes from response
def get_tends_from_specific_location(woeID):
    client = get_twitter_auth()

    # Get senator followers
    followers = client.trends_place(woeID)

    # friends is a resultSet which allows attribute access via . notation
    # print(followers)
    print("\n" + "[+] Printing out trends from a specific location")
    for i in followers:
        print(i)


def friendship_id(senator_twitter_name):
    client = get_twitter_auth()

    friendship = client.friends_ids(senator_twitter_name)

    print("\n" + "[+] Printing out senator friendship IDS")
    print(friendship)
