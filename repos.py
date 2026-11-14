import requests
import json
username = "liza052005"
url = f"https://api.github.com/users/{username}/repos"
response = requests.get(url)
repos = response.json()
with open("repos.json", "w", encoding="utf-8")as file:
    json.dump(repos, file, ensure_ascii=False, indent=4)
print("Ваш файл создан!")