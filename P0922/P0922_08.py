import requests
from bs4 import BeautifulSoup
url = "https://www.melon.com/chart/index.htm"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
res = requests.get(url,headers=headers)
res.raise_for_status() #에러시 종료

soup = BeautifulSoup(res.text,'lxml') #html소스 변경-css문법
print("*"*80)
s_tbody = soup.tbody
trs = s_tbody.find_all("tr",{"class":"lst50"})
for i in range(50) :
    tds = trs[i].find_all('td')
    rank = tds[1].find("span",{"class":"rank"}).get_text()
    img = tds[3].find("img")["src"]
    title = tds[5].find("a").get_text()
    al = tds[6].find("a").get_text()
    # s_title = tds[5].find("span",{"class":"title"}).get_text 실패
    print(f"{rank},{img},{title},{al}")
