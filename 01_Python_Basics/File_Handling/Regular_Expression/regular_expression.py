import re

text = "My phone number is 9876543210"

result = re.search(r"\w{10}", text)
print(result.group())