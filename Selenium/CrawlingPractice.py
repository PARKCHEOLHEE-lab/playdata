from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome("c:/ChromeDriver/chromedriver", options=options)
driver.get("http://tour.interpark.com/")

input = driver.find_element_by_name("SearchGNBText") 
btn = driver.find_element_by_class_name("search-btn") 
input.clear() 
input.send_keys("서울 숙박")  
btn.click()             

total = driver.find_element_by_link_text("통합")
total.click()

html = driver.page_source
acommo = BeautifulSoup(html, 'html.parser')

# print(soup.prettify()) # completed html parsing 
# print(type(html)) # <class 'str'>

for i in range(10):
    print("숙소 위치 :", acommo.select(".productInfo")[i].div.span.next_sibling.string)
    print("숙소 이름 :", acommo.select(".productInfo")[i].a.string)
    print("쿠폰 내용 :", acommo.select(".subInfo")[i].string)
    print("숙소 가격 : ", acommo.select(".number")[i].string)
    print("숙소 리뷰 : ", acommo.select(".review")[i].string)
    print("예약 현황 : ", acommo.select(".reserveArea")[i].string)
    # print("숙소 링크", driver.find_element_by_css_selector("div.imgBox > a").get_attribute('href'))
    # print("숙소 링크", acommo.select(".imgBox > a ").find()["onclick"])

    print("======================================")


time.sleep(1)
driver.quit()
