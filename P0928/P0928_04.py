from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv
import undetected_chromedriver as uc

# # 2. selenium : 자동화 도구 - 스크롤없이 가져옴
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=recent&traceId=muksjcx4"
options = uc.ChromeOptions()
options.add_argument("--no-first-run --no-service-autorun --password-store=basic")
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36")
browser = uc.Chrome(options=Options)


browser.maximize_window() # 화면 최대창 확대
browser.get(url)
time.sleep(2)
# 파일저장
soup = BeautifulSoup(browser.page_source,'lxml')
with open('aix_python_0825/P0928/file/coupang1.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())

print("완료")
input()