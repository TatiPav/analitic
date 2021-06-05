import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Acsept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Код состояния: {r.status_code}")

response_dict = r.json()

print(response_dict.keys())