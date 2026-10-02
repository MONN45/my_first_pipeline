import requests

import json


url  = "https://jsonplaceholder.typicode.com/posts"

params = {"start": 0,"limit":2}

response  = requests.get(url,params=params,timeout=10)

print(f"Status code  = {response.status_code}")
print(f" Full Url called {response.url}")

posts = response.json()

print(type(posts))
print("*****************")
print(f"length of the postd{len(posts)}")

print("*******************")



print(response.json())


print("*********************")

print(f"\n First post :")

print(json.dumps(posts[0],indent=2))


print("\n field in each post:",list(posts[0].keys()))