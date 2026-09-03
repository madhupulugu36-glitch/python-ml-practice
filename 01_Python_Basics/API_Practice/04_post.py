import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "name": "John",
    "age":25,
    "course": "Python Programming",
    "city": "New York"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)

print("\nResponse Body:")
print(response.json())