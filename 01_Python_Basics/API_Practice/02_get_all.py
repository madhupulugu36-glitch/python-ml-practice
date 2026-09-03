import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
print("Status Code:", response.status_code)

posts = response.json()

print("\nNumber of posts:", len(posts))

print("\nFirst 3 posts:")

for post in posts[:3]:
    print("ID:", post["id"])
    print("Title:", post["title"])
    print("_" * 50)