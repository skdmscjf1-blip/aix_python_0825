from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# url = "https://flight.naver.com/flights/domestic/SEL:city-CJU:airport-20261006/CJU:airport-SEL:city-20261008?adult=1&fareType=YC"
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() # 화면 최대창 확대
# browser.get(url)
# time.sleep(2)

# # 스크롤 추가
# # execute_script : 자바스크립트 언어 사용가능
# #현재 스크롤 높이 가져옴
# prev_height = browser.execute_script('return document.body.scrollHeight')


# while True:
#     #스크롤 높이 출력
#     print('높이 : ',prev_height) 
#     #스크롤 내리기
#     browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     time.sleep(2)
#     #스크롤이 추가되엇는지 확인
#     next_height = browser.execute_script('return document.body.scrollHeight')
#     if prev_height == next_height :
#         break
#     prev_height = next_height

# # input()

# # 파일저장
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('flight2.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())

# print('완료')

# 3. 파일 BeautifulSoup변환
# with open('flight2.html','r',encoding='utf-8') as f:
#     soup = BeautifulSoup(f,'lxml')

# flights = soup.find_all('div',{'class':'domestic_Flight__8bR_b'})

# name = flights[0].find('b',{'class':'airline_name__0Tw5w'}).get_text(strip=True)
# start = flights[0].find_all('b',{'class':'route_time__xWu7a'})
# star1 = start[0].get_text(strip=True)
# end = start[1].get_text(strip=True)
# price = flights[0].find('i',{'class':'domestic_num__ShOub'}).get_text(strip=True)
# i_price = int(price.replace(',',''))

# # print(name,star1,end,i_price)
# # print(len(flights))

# for i in range(1,303) :
#     name = flights[i].find('b',{'class':'airline_name__0Tw5w'}).get_text(strip=True)
#     start = flights[i].find_all('b',{'class':'route_time__xWu7a'})
#     star1 = start[0].get_text(strip=True)
#     end = start[1].get_text(strip=True)
#     price = flights[i].find('i',{'class':'domestic_num__ShOub'}).get_text(strip=True)
#     i_price = int(price.replace(',',''))
#     if i_price <= 50000 :
#         print(f"{i},항공 : {name}\t출발시간 : {star1}\t도착시간 : {end}\t가격 : {i_price}")


#----------------------------------------------------------------------------------------------------
    
# url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B2%BD%EC%A3%BC&checkIn=2026-09-28&checkOut=2026-09-29&personal=2&typoCorrect=true&nonAffiliated=true"
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() # 화면 최대창 확대
# browser.get(url)
# time.sleep(2)

# # 스크롤 추가
# # execute_script : 자바스크립트 언어 사용가능
# #현재 스크롤 높이 가져옴
# prev_height = browser.execute_script('return document.body.scrollHeight')


# while True:
#     #스크롤 높이 출력
#     print('높이 : ',prev_height) 
#     #스크롤 내리기
#     browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#     time.sleep(2)
#     #스크롤이 추가되엇는지 확인
#     next_height = browser.execute_script('return document.body.scrollHeight')
#     if prev_height == next_height :
#         break
#     prev_height = next_height

# # input()

# # 파일저장
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('yeogi1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())


# 3. 파일 BeautifulSoup변환
# with open('yeogi1.html','r',encoding='utf-8') as f:
#     soup = BeautifulSoup(f,'lxml')

# hotel = soup.find('ul',{'class':'css-y5z6rw'})
# li_all = hotel.find_all('li',{'class':'gc-thumbnail-type-seller-card-wrapper css-13wylk3'})
# name = li_all[0].find('h3',{'class':'gc-thumbnail-type-seller-card-title css-1gsfgy5'}).get_text(strip=True)
# price = li_all[0].find('span',{'class':'css-1llao6q'}).get_text(strip=True)
# i_price = int(price.replace(",",""))
# star = li_all[0].find('span',{'class':'css-ry30z7'}).get_text(strip=True)
# i_star =float(star)

# # print(f"{name}\t{i_price}\t{i_star}")

# # print(len(li_all)) #826

# for i in range(0,825): 
#     try : 
#     # li_all = hotel.find_all('li',{'class':'gc-thumbnail-type-seller-card-wrapper css-13wylk3'})
#         name = li_all[i].find('h3',{'class':'gc-thumbnail-type-seller-card-title css-1gsfgy5'}).get_text(strip=True)
#         price = li_all[i].find('span',{'class':'css-1llao6q'}).get_text(strip=True)
#         i_price = int(price.replace(",",""))
#         star = li_all[i].find('span',{'class':'css-ry30z7'}).get_text(strip=True)
#         i_star =float(star)
#         if i_price >= 200000 and i_star >= 9.5 :
#             print(f"{i}.{name}\t{i_price}\t{i_star}")
#     except : 
#         pass

#---------------------------------------------------------------------------------------------------------

# 1. requests 파일 가져오기
for i in range(1,6) : 
    page = i
    url = f"https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&checkedInfo=N&volumeType=allvs&page={page}&limit=40&sort=saveDESC&list=list&boost=true&tab=goods&addDelivery=N&simpleDescOpen=Y&mode=simple&isInitTireSmartFinder=N&recommendedSort=N&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10580%7C0&defaultVmTab=104290&defaultVaTab=8809942&isZeroPrice=Y&quickProductYN=N&priceUnitSort=N&priceUnitSortOrder=A"
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
    res = requests.get(url,headers=headers)
    res.raise_for_status() #에러시 종료
    soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법
    print("-"*50)

    ul = soup.find('ul',{'class':'product_list'})
    lis = ul.find_all('li',{'class':'prod_item'})
    name = lis[0].find('p',{'class','prod_name'}).get_text(strip=True)
    # price =lis[0].find('p',{'class':'price_sect'}).get_text(strip=True)
    price =lis[0].a.get_text(strip=True)
    print(f"{name}\t{price}")







# #.env파일 읽어와서 변수값 입력
# load_dotenv()
# id = os.getenv('id')
# #id = 'admin' # 프로그램에 노출이 됨.

# print(id)