import requests, os

url = "https://yahoo-weather5.p.rapidapi.com/weather"

my_dict = {
    1: 'Tashkent',
    2: 'Jizzax',
    3: 'Andijon ',
    4: 'Buxoro ',
    5: 'Samarkand',
    6: 'Navoiy',
    7: 'Namangan',
    8: 'Fargona',
    9: 'Xorazm',
    10: 'Qashqadaryo',
    11: 'Surxondaryo',
    12: 'Sirdaryo',
    13: 'Qoraqalpogiston',
}

for i, k in my_dict.items():
    print(f'{i}. {k}')

top_weather = int(input('Shaxar Raqamini Kiriting: '))

kunlar = {
    1: 'Mon',
    2: 'Tue',
    3: 'Wed',
    4: 'Thu',
    5: 'Fri',
    6: 'Sat',
    7: 'Sun'
}

for i, k in kunlar.items():
    print(f'{i}, {k}')

kun = int(input('Kunlardan birini tanlang: '))

if top_weather not in my_dict:
    print("Invalid city number")
    exit()

querystring = {
    "location": my_dict[top_weather],
    "format": "json",
    "u": "c"
}

headers = {
    "X-RapidAPI-Key": "26695146d6mshd355a859397fcdbp101dafjsnfd8e01908979",
    "X-RapidAPI-Host": "yahoo-weather5.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
if response.status_code == 200:
    os.system('clear')
    weather_data = response.json()
    city_name = weather_data["location"]["city"]

    for day in weather_data["forecasts"]:
        if day["day"] == kunlar[kun]:
            date = day["date"]
            day_of_week = day["day"]
            high_temp = day["high"]
            low_temp = day["low"]
            description = day["text"]
            print(f"Ob-havo \n\t{city_name}da, {day_of_week} kunida, Kun: {date}\n\tHarorat:  Yuqori: {high_temp}°C, Past: {low_temp}°C\n\tTavsif: {description}\n")

else:
    print("Serverda Xatolik", response.status_code)

