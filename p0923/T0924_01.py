# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
# import requests
# from bs4 import BeautifulSoup
# import time
# import os
# from dotenv import load_dotenv

# # options = Options()

# # options.add_experimental_option("excludeSwitches", ["enable-automation"])
# # options.add_experimental_option("useAutomationExtension", False)
# # options.add_argument("--disable-blink-features=AutomationControlled")
# # browser = webdriver.Chrome(options=options)
# # browser.maximize_window() # 화면 최대창 확대
# # url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B2%BD%EC%A3%BC&autoKeyword=%EA%B2%BD%EB%B6%81+%EA%B2%BD%EC%A3%BC%EC%8B%9C&checkIn=2026-09-23&checkOut=2026-09-24&personal=2"
# # browser.get(url)
# # time.sleep(2)
# # # # 자바스크립트를 통해 브라우저 높이 가져오기
# # # pre_height = browser.execute_script('return document.body.scrollHeight')
# # # print("처음 높이 : ",pre_height)
# # # while True:
# # #     # 스크롤 내리기
# # #     browser.execute_script('window.scroll(0,document.body.scrollHeight)')
# # #     time.sleep(5) # 내용추가하는데 시간대기

# # #     # 다시 높이 가져오기
# # #     next_height = browser.execute_script('return document.body.scrollHeight')
# # #     print('변경된 높이 : ',next_height)

# # #     if pre_height==next_height: break
# # #     else : pre_height = next_height

# # # print('더 이상 높이 변경이 없음')
# # # time.sleep(1)

# # # # 파일저장해서 저장한 파일을 가지고 정보를 가져오기
# # # # 이미지, 숙소명, 별점, 리뷰수, 금액
# # # # 파일저장
# # # soup = BeautifulSoup(browser.page_source,'lxml')
# # # with open('yeogi1.html','w',encoding='utf-8') as f:
# # #     f.write(soup.prettify())
# # input()

# with open('yeogi1.html','r',encoding='utf-8') as f:
#     soup = BeautifulSoup(f,'lxml')
# s_ul = soup.find('ul',{'class':'css-y5z6rw'})
# lis = s_ul.find_all('li')
# for idx,li in enumerate(lis) : 
#     print(f"{idx+1}")
#     try :
#         s_img = li.find('img')['src']
#         print("이미지 : ",s_img)
#         s_title = li.find('h3',{'class':'gc-thumbnail-type-seller-card-title css-1gsfgy5'}).get_text(strip=True)
#         print("숙소명 : ",s_title)
        
#     except Exception as e:
#         print(e)













# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # import requests
# # from bs4 import BeautifulSoup
# # import time
# # import os

# # headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# # browser = webdriver.Chrome()
# # url = 'https://comic.naver.com/bestChallenge'
# # browser.get(url)
# # time.sleep(4)

# # # soup = BeautifulSoup(browser.page_source,'lxml')
# # # with open('webtoon1.html','w',encoding='utf-8') as f:
# # #     f.write(soup.prettify())

# # with open('webtoon1.html','r',encoding='utf-8') as f :
# #     soup = BeautifulSoup(f,'lxml')

# # s_ul = soup.find('ul',{'class':'HotChallengeList__hot_challenge_list--I91_w'})
# # lis = s_ul.find_all('li')

# # for i in range(3) :
# #     title = lis[i].find('span',{'class':'ContentTitle__title--e3qXt'}).get_text(strip=True)
# #     print(title)
# #     s_title = lis[i].find('a',{'class':'ContentAuthor__author--CTAAP'}).get_text(strip=True)
# #     print(s_title)
# #     star_avg1 = lis[i].find('span',{'class':'Rating__star_area--dFzsb'})
# #     star_avg2 = float(star_avg1.find('span',{'class':'text'}).get_text(strip=True))
# #     print(star_avg2)
# #     view1 = lis[i].find('span',{'class':'Rating__view_area--GQb_S'})
# #     view2 = int(view1.find('span',{'class':'text'}).get_text(strip=True).replace(",",""))
# #     print(view2)
# #     s_img = lis[i].find('img',{'class':'Poster__image--d9XTI'})['src']
# #     print(s_img)
# #     print("-"*100)

# #     img_res = requests.get(s_img,headers=headers)
# #     os.makedirs('./p0923/webtoon',exist_ok=True)
# #     with open(f'p0923/webtoon/w_{i}.jpg','wb') as f:
# #         f.write(img_res.content)
# # print("완료")







# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # import requests
# # from bs4 import BeautifulSoup
# # import time
# # import os

# # # 2. selenium : 자동화 도구
# # # browser = webdriver.Chrome()
# # # url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
# # # browser.get(url)
# # # time.sleep(4)
# # # soup = BeautifulSoup(browser.page_source,'lxml')
# # # with open('stock1.html','w',encoding='utf-8') as f :
# # #     f.write(soup.prettify())

# # with open('stock1.html','r',encoding='utf-8') as f:
# #     soup = BeautifulSoup(f,'lxml')

# # s_headTitle = []
# # s_tr = soup.thead.tr
# # ths = s_tr.find_all('th')
# # for th in ths:
# #     s_headTitle.append(th.get_text(strip=True))
# #     # print(th.get_text())
# # print("순위\t{}\t\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(*s_headTitle))
# # print("-"*80)
# # s_tbody=soup.tbody
# # trs = s_tbody.find_all('tr')
# # for tr in trs:
# #     tds = tr.find_all('td')
# #     rank = tds[0].find('span',{"class":'index'}).get_text(strip=True)
# #     s_Title = tds[0].find('span',{'class':'SingleLineText_text__HI_cb'}).get_text(strip=True)
# #     s_price = tds[1].find('span',{'class':'SingleLinePrice_price__g_6VV'}).get_text(strip=True)
# #     s_compare =tds[2].find('span',{'class':'ModulePriceChange_amount__4QYMz'}).get_text(strip=True)
# #     s_trade =tds[3].find('span',{'class':'SingleLinePrice_price__g_6VV'}).get_text(strip=True)
# #     s_trade_val =tds[4].find('span',{'class':'SingleLinePrice_price__g_6VV'}).get_text(strip=True)
# #     s_max =tds[5].find('span',{'class':'SingleLinePrice_single-line-price__bnpQv SingleLinePrice_medium__QoN_F'}).get_text(strip=True)
# #     s_min =tds[6].find('span',{'class':'SingleLinePrice_single-line-price__bnpQv SingleLinePrice_medium__QoN_F'}).get_text(strip=True)
# #     s_total =tds[7].find('span',{'class':'SingleLineText_single-line-text__hCqgu default SingleLineText_medium__x_OcH'}).get_text(strip=True)    
# #     print(f"{rank}\t{s_Title}\t{s_price}\t{s_compare}\t{s_trade}\t {s_trade_val}\t\t{s_max}\t{s_min}\t{s_total}")