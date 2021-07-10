from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome("c:/ChromeDriver/chromedriver.exe", options=options)
driver.get("https://www.starbucks.co.kr/store/store_map.do")


''' ------------------------------------------------ step 01

              starbucks find-store page open
        & button click, all of seoul store search

    ------------------------------------------------ step 01 '''

time.sleep(3)
store = driver.find_element_by_link_text("지역 검색")
store.click()

seoul = driver.find_element_by_class_name("set_sido_cd_btn")
seoul.click()

time.sleep(2)
region = driver.find_element_by_link_text("전체")
region.click()


''' ------------------------------------------------ step 02

                       html extraction
                seoul store data collecting

    ------------------------------------------------ step 02 '''

time.sleep(3)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

all_store = soup.select("li.quickResultLstCon") # length error
store_list = []

for k in range(10, len(all_store)):
    branch = all_store[k].strong.text  
    address = str(all_store[k].p.text)[:-9]  
    tel = str(all_store[k].p.text)[-9:]  
    lat = all_store[k]["data-lat"]
    long = all_store[k]["data-long"]
    typ = str(all_store[k].i)[14:21]

    store_list.append([branch, address, tel, typ, lat, long])

driver.quit()

''' ------------------------------------------------ step 03

                  create DataFrame & save file

    ------------------------------------------------ step 03 '''

columns = ["branch", "address", "telephone", "branch_type", "latitude", "longitude"]
sbks_seoul = pd.DataFrame(store_list, columns=columns)
print(sbks_seoul.head())

sbks_seoul.to_excel("Starbucks/Starbucks.xlsx", index=False)