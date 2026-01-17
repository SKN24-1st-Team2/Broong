from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
# from bs4 import BeautifulSoup
import os, time


# 경로 설정
url = 'https://stat.molit.go.kr/portal/cate/statMetaView.do?hRsId=58'
rel_path = '../../../data/raw'
abs_path = os.path.abspath(rel_path)


chrome_options = Options()
# 다운로드 경로 설정
chrome_options.add_experimental_option("prefs", {
    "download.default_directory": abs_path,
    "download.prompt_for_download": False,
    "safebrowsing.enabled": True
})

service = Service()
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)
time.sleep(1)

# 박스 찾을 때까지 스크롤
while True:
    body = driver.find_element(By.TAG_NAME, 'body')
    body.send_keys(Keys.PAGE_DOWN)

    if driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[1]/div/div[2]/div[2]/div'):
        break



# driver.find_element(By.XPATH, '//*[@id="main"]/div/div[3]/div[1]/div/div[2]/div[2]/div')
time.sleep(2)


