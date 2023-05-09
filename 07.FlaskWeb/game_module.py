import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup

def pc():
    url = 'https://www.gamemeca.com/ranking.php'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    trs = soup.select('.ranking-table-rows')
    temp = []
    for tr in trs:
        rank = tr.select_one('.rank').get_text()
        name = tr.select_one('.game-name').get_text()
        info = tr.select('.game-info > span')[-2].get_text()
        img = tr.select_one('.game-icon')['src']
        temp.append({'rank':rank, 'name':name, 'info':info, 'img':img})
    return temp    