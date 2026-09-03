import requests

url= "https://jsonplaceholder.typicode.com/posts/1"

data = {
    "id": 1,
    "title": "Updated Python API",
    "body": "Learning PUT request",
    "userId": 1
}

response = requests.put(url, json=data)

print("Status code:", response.status_code)

print("\nUpdated data:")
print(response.json())