from flask import Flask, render_template, request
import folium, json, requests, os
from urllib.parse import quote
import pandas as pd

def hotplace(places, app):
    # 도로명주소
    with open('../04.지도시각화/data/roadapikey.txt') as f:
        road_key = f.read()
    base_url = 'https://www.juso.go.kr/addrlink/addrLinkApiJsonp.do'
    params1 = f'confmKey={road_key}&currentPage=1&countPerPage=10'
    road_addr = []
    for gov in places:
        params2 = f'keyword={quote(gov)}&resultType=json'
        url=f'{base_url}?{params1}&{params2}'    
        result = requests.get(url)
        if result.status_code == 200:
            res = json.loads(result.text[1:-1])
            road_addr.append(res['results']['juso'][0]['roadAddr'])
        else:
            print(result.status_code)
    df = pd.DataFrame({'place':places, 'addr':road_addr})
    # 위도 경도
    base_url = 'https://dapi.kakao.com/v2/local/search/address.json'
    with open('../04.지도시각화/data/kakaoapikey.txt') as d:
        kakao_key = d.read()
    lat = []
    lon = []
    header = {"Authorization": f'KakaoAK {kakao_key}'}
    for addr in road_addr:
        url = f'{base_url}?query={quote(addr)}'
        result = requests.get(url, headers=header).json()
        lat.append(float(result['documents'][0]['y']))
        lon.append(float(result['documents'][0]['x']))
    df['위도'] = lat
    df['경도'] = lon
    
    map = folium.Map(location=[df['위도'].mean(), df['경도'].mean()], zoom_start=13)
    for i in df.index:
        folium.Marker(
        location=[df.위도[i],df.경도[i]],    
        popup=folium.Popup(df.addr[i], max_width=200),
        radius=300,fill=True,
        tooltip=df.place[i]
        ).add_to(map) 
    filename = os.path.join(app.static_folder, 'img/hotplaces.html')
    map.save(filename)