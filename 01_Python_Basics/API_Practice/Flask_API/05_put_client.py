import requests

url = "http://127.0.0.1:5000/students/99"

data = {}

response = requests.put(url, json=data)

print("Status Code:", response.status_code)

print("\nResponse:")
print(response.json())