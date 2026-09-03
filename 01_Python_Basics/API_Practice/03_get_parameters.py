"""import requests

url = "https://jsonplaceholder.typicode.com/posts"

parms = {
    "userId": 1
}

response = requests.get(url, params=parms)

print("Status code:", response.status_code)

posts = response.json()

print("\nNumber of posts:", len(posts))

print("\nPosts:")

for post in posts:
    print("ID:", post["id"])
    print("Title:", post["title"])
    print("_" * 50)"""
import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1,
    "_limit": 3
}

response = requests.get(url, params=params)

print("Status Code:", response.status_code)

print("Requested URL:", response.url)

posts = response.json()

print("\nNumber of posts:", len(posts))

print("\nPosts:")

for post in posts:
    print("ID:", post["id"])
    print("User ID:", post["userId"])
    print("Title:", post["title"])
    print("-" * 50)