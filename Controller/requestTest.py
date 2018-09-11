import requests

URL = "https://jsonplaceholder.typicode.com/posts"

r = requests.get(url=URL)
data = r.json()
print(data)
