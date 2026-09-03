# HTTP Request and Response Basics

url = "https://example.com/students"
method = "GET"

print("HTTP Basics")
print("-------------------")

print("URL:", url)
print("Method:", method)

print("\nRequest:")
print("Client -> Server")

print("\nResponse:")
print("Server -> Client")

status_code = 200

print("\nStatus Code:", status_code)

if status_code == 200:
    print("Request was successful!")