import requests

url = 'https://api.github.com/search/repositories?q=language:java&sort=stars'

headers = {'Accept': 'application/vnd.github.v3+json'}

r = requests.get(url, headers=headers)
print(f"Код состояния: {r.status_code}")

response_dict = r.json()
print(f"Все репозитарии: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Возвращенные репозитории: {len(repo_dicts)}")

# repo_dict = repo_dicts[0]
# print(f"\nКлючи: {len(repo_dicts)}")
# for key in sorted(repo_dict.keys()):
#     print(key)
print("\nВыбранная информация о каждом репозитории:")
for repo_dict in repo_dicts:
    print(f"Наименование : {repo_dict['name']}")
    print(f"Владелец : {repo_dict['owner']['login']}")
    print(f"Звезды: {repo_dict['stargazers_count']}")
    print(f"Хранилище: {repo_dict['html_url']}")
    # print(f"Созданный: {repo_dict['created_at']}")
    # print(f"Обновленный: {repo_dict['updated_at']}")
    print(f"Описание: {repo_dict['description']}")

