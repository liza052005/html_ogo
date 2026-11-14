import requests

username = "liza052005"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()
print(f"Найдено репозиториев:{len(repos)}")
for repo in repos[:3]:
    name = repo['name']

    print(f'Репозиторий: {name}')
