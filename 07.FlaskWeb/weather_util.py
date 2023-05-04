import requests, os

def get_weather(app):
    key_file = os.path.join(app.static_folder, 'key/openweather.txt')
    with open(key_file) as f:
        weather_key = f.read()
    base_url = 'https://api.openweathermap.org/data/2.5/weather'
    # 수원지역
    lat = 37.295
    lon = 127.045
    url = f'{base_url}?lat={lat}&lon={lon}&appid={weather_key}&units=metric&lang=kr'
    res = requests.get(url).json()

    desc = res['weather'][0]['description']
    icon_code = res['weather'][0]['icon']
    icon_url = f'https://openweathermap.org/img/wn/{icon_code}.png'
    temp_ = res['main']['temp']
    temp = round(float(temp_), 1)

    html = f'''<img src="{icon_url}" height="32"><strong>{desc}</strong>
                온도:<strong>{temp}</strong>&#8451'''
                
    return html