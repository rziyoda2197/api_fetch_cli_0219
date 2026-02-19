import requests

url = "https://api.github.com"

r = requests.get(url)

print("Status:", r.status_code)
print("Headers:", r.headers.get("content-type"))
