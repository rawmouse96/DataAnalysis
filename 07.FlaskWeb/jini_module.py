import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime

def jini():
    now = datetime.now()
    now
    ymd = now.strftime('%Y%m%d')
    hh = now.strftime('%H')
    ymd, hh
    from tqdm import tqdm
    jini_list = []
    for i in tqdm(range(1, 5)):
        url = f'https://www.genie.co.kr/chart/top200?ditc=D&ymd={ymd}&hh={hh}&rtm=Y&pg={i}'
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
        result = requests.get(url, headers=header)
        soup = BeautifulSoup(result.text, 'html.parser')
        trs = soup.select('tr.list')
        for tr in trs:
            rank = tr.select_one('.number').get_text().split('\n')[0].strip()       # strip : \n포함 문자열 양옆 공백 제거
            img = tr.select_one('.cover > img')['src']
            img = f'https:{img}'
            title = tr.select_one('.title.ellipsis').get_text().split('\n')[-1].strip()
            artists = tr.select_one('.artist.ellipsis').get_text()
            album = tr.select_one('.albumtitle.ellipsis').get_text()
            jini_list.append({'rank':rank, 'img':img, 'title':title, 'artists':artists, 'album':album})
        
    return jini_list
# df1.to_csv(f'static/csv/{ymd}{hh}_지니차트.csv', index=False)