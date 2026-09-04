import requests

url = "http://127.0.0.1:5000/students"

response = requests.get(url)

print("Status Code:", response.status_code)

print("\nResponse:")
print(response.json())