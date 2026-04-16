import requests

result = requests.get("https://google.com/")

print(result.text)