import requests
url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)
if response.status_code == 200:
    print("Сервер ответил успешно")

    data = response.json()
    usd_rate = data['Valute']['USD']['Value']
    print('КУрс доллара: ', usd_rate, 'рублей')
else:
    print('ОШибка!!!', response.status_code)
