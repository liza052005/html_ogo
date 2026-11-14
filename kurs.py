import requests
url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)
data = response.json()
usd_rate = data['Valute']['USD']['Value']
eur = data['Valute']['EUR']['Value']

with open("kurs.txt", "w", encoding="utf-8")as file:
    file.write("Курс валют на сегодня\n")
    file.write(f"Доллар: {usd_rate}\n")
    file.write(f"Евро: {eur}\n")
print("Файл создан!")