# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import requests
# from bs4 import BeautifulSoup
# import time
# import os

# browesr = webdriver.Chrome()
# url = "http://www.naver.com"

# browesr.get(url)

# elem = browesr.find_element(By.ID,'query')
# elem.click()
# elem.send_keys("뉴스")
# elem.send_keys(Keys.ENTER)
# time.sleep(3)
# elem2 = browesr.find_element(By.CLASS_NAME,"sds-comps-text")
# elem2.click()

# input()




# import requests
# from bs4 import BeautifulSoup
# import os
# url = "https://www.melon.com/chart/index.htm"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status() #에러시 종료

# soup = BeautifulSoup(res.text,'lxml')

# # with open('melon2.html','w',encoding='utf-8') as f:
# #     f.write(soup.prettify())

# print("-"*80)
# s_tbody=soup.tbody
# trs=s_tbody.find_all('tr')
# for idx,tr in enumerate(trs) : 
#     tds=tr.find_all('td')
#     try:
#         print("순위 : ",tds[1].find('span',{'class':'rank'}).get_text())
#         img = tds[3].find("img")['src']
#         print("이미지 링크 : ",img)

#         os.makedirs("./melon_img",exist_ok=True)

#         img_res = requests.get(img,headers=headers)
#         with open(f"melon_img/melon_2026_{idx+1}.jpg",'wb') as f:
#             f.write(img_res.content)
#     except Exception as e:
#         print(e)

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.melon.com/chart/index.htm"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)
# res.raise_for_status()

# # with open('melon1.html','w',encoding='utf-8') as f :
# #     f.write(res.text)

# soup = BeautifulSoup(res.text,'lxml')
# print("-"*80)
# s_tbody=soup.tbody
# trs = s_tbody.find_all("tr",{'class':"lst50"})
# for i in range(50): 
#     tds = trs[i].find_all('td')
#     title = tds[5].find('span').get_text(strip=True)
#     s_title = tds[5].find('span',{'class':'checkEllipsis'}).get_text()
#     print(f"{i+1}\t{title}\t{s_title}")


# import requests
# from bs4 import BeautifulSoup

# url = "https://www.daum.net"
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
# res = requests.get(url,headers=headers)

# soup = BeautifulSoup(res.text,'lxml')
# print("-"*80)
# # print(soup.title.get_text())
# print(soup.find("a",{'class':'w5hRs'}).get_text())

# import requests
# from bs4 import BeautifulSoup

# url = "https://www.melon.com/chart/index.htm"
# headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
# res =requests.get(url,headers=headers)
# res.raise_for_status

# soup = BeautifulSoup(res.text,'lxml')
# print("-"*80)

# # print(soup.find("div",{"id":"header"}))
# # print(soup.find("div",{"id":"utill_menu"}))
# # print(soup.find("div",{"class" : "wrap t_right"}))
# print(soup.find("input",{"class":"input_check d_checkall"})['title'])


# import requests

# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
# headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}

# res = requests.get(url,headers=headers)

# res.raise_for_status() #에러나면 프로그램 종료

# with open('melon2.html','w',encoding='utf-8') as f:
#     f.write(res.text)

# print("저장완료")


# import requests
# res = requests.get("https://www.google.com/")
# res.raise_for_status()
# print(res.text)
# print(len(res.text))

# with open('google.html','w',encoding='utf-8') as f :
#     f.write(res.text)
# print("파일저장완료")