import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.delete(url)

print("Status code:", response.status_code)

print("\nResponse:")

print(response.text)