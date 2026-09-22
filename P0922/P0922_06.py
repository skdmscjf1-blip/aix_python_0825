import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)

soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법
print("*"*80)
# 태그,
print(soup.title.get_text())
# print(soup.find("a",{"class":"w5hRs"}).get_text())
# print(soup.find("a",{"class":"gb_6"}).get_text())
# print(soup.find_all("span",{"class":"blind"}))
# print(soup.find("a",{"class":"MyView-module__link_more___F2Dl0"}))
# print(soup.find("a",{"class":"MyView-module__link_more___F2Dl0"}))
# print(soup.find("a",{"class":"MyView-module__link_more___F2Dl0"}))
print(soup.find("h2",{"id":"mainServiceTitle"}))