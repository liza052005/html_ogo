import requests
api_key = "f3ecf66891a236c26fc1f45a8c223f61".strip()
city = "Vladivostok"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    description  = data['weather'][0]['description']
    print('Погода в VDK')
    print("Температура", temp)
    print("Описание", description)
else:
    print("Ошибка", response.status_code)