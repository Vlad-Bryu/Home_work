import requests

def weather_in_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {
        "key": "174c05b5083d4342a89153144193105",
        "q": city_name,
        "format": "json",
        "num_of_days": "1",
        "lang": "ru"
    }
    result = requests.get(weather_url, params=params)
    weather = result.json()
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False
    return False

if __name__ == '__main__':
    print(weather_in_city("Moscow,Russia"))

