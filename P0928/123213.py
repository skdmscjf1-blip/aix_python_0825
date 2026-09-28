from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# 1. requests 파일 가져오기
for i in range(1,2):
    page = i
    url = f"https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&checkedInfo=N&volumeType=allvs&page={page}&limit=40&sort=saveDESC&list=list&boost=true&tab=goods&addDelivery=N&simpleDescOpen=Y&mode=simple&isInitTireSmartFinder=N&recommendedSort=N&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10580%7C0&defaultVmTab=104290&defaultVaTab=8809942&isZeroPrice=Y&quickProductYN=N&priceUnitSort=N&priceUnitSortOrder=A"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
    res = requests.get(url,headers=headers)
    res.raise_for_status() #에러시 종료
    soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법
    print("-"*50)
    ul = soup.find('ul',{'class':'product_list'})
    lis = ul.find_all('li',{'class':'prod_item'})
    for li in lis:
        try:
            print(li.find('p',{'class':'prod_name'}).get_text(strip=True))
            price_li = li.find('li',{'class':'rank_one'})
            price_li_str = price_li.a.get_text(strip=True)[:-1]
            price_li_int = int(price_li_str.replace(',',''))
            print(price_li.a.get_text(strip=True))
            print(price_li_int)
        except:
            print('이름 / 값 없음')
        print("-"*10)
    print(i,":",len(lis))