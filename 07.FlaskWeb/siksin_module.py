import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup

def siksin():
    base_url = 'https://www.siksinhot.com/search'
    url = f'{base_url}?keywords={quote("장안문")}'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    lis = soup.select('.localFood_list > li')
    temp = []
    for li in lis:
        img = li.find('img')['src']
        title = li.select_one('.textBox > h2').get_text()
        score = li.select_one('.textBox > span').get_text()
        atags = li.select('.cate > a')
        loc = atags[0].get_text()
        menu = atags[1].get_text()
        temp.append({'img': img, 'title': title, 'score': score, 'loc': loc, 'menu': menu})
    return temp