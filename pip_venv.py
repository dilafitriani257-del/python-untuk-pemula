import requests

r = requests.get("https://api.github.com")
print("Status code:", r.status_code)
