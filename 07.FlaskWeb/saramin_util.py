import requests
from urllib.parse import quote
import pandas as pd
from bs4 import BeautifulSoup
import math

def jobkorea(): 
    url = f'https://www.jobkorea.co.kr/Search/?stext=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&local=B000%2CI000&careerType=1&jobtype=1&payType=1&payMin=3000&tabType=recruit&Page_No={1}&Ord=EditDtDesc'
    result = requests.get(url)
    soup = BeautifulSoup(result.text, 'html.parser')
    num1 = int(soup.select_one('.filter-text').get_text()[-3:-1])
    page = math.ceil(num1/20)
    temp = []
    for i in range(page):
        url = f'https://www.jobkorea.co.kr/Search/?stext=%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0&local=B000%2CI000&careerType=1&jobtype=1&payType=1&payMin=3000&tabType=recruit&Page_No={i}&Ord=EditDtDesc'
        result = requests.get(url)
        soup = BeautifulSoup(result.text, 'html.parser')
        p1 = soup.select_one('.recruit-info')
        p2 = p1.select('.list-post > .post')
        for post in p2:
            try:
                corp_name = post.select_one('.post-list-corp > a').get_text()
                title = post.select_one('.post-list-info > a').get_text().strip()
                post_url = 'https://www.jobkorea.co.kr' + post.select_one('.post-list-info > a')['href']
                temp.append({'name':corp_name, 'title':title, 'url':post_url})
            except:
                continue

    return temp