import requests

url = "http://127.0.0.1:5000/students"

data = {
    "name": "Arjun",
    "course": "Machine Learning"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)

print("\nResponse:")
print(response.json())