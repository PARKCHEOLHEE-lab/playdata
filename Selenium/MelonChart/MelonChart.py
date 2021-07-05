from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome("c:/ChromeDriver/chromedriver.exe", options=options)
driver.get("https://www.melon.com/chart/index.htm")

# chart = driver.find_element_by_link_text("멜론차트")
# chart.click()

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
# print(soup.prettify)

songs = soup.select('div.ellipsis.rank01')
singers = soup.select('div.ellipsis.rank02')
albums = soup.select('div.ellipsis.rank03')
chart_len = str(songs).count("<a href")

# print(singers[0].span.a.string)
# print(songs[0].span.a.string)
songs_list = [songs[song].span.a.string for song in range(chart_len)]
singers_list = [singers[singer].span.a.string for singer in range(chart_len)]
albums_list = [albums[album].a.string for album in range(chart_len)]

# for song in range(songs_len):
#     print(songs[song].span.a.string)

data = pd.DataFrame(data=zip(range(1,101), songs_list, singers_list, albums_list),\
                    columns=['Rank', 'Title', 'Singer', 'Album'])

print(data.head())

data.to_csv('MelonChart.csv', encoding="utf-8-sig", index=False)

driver.quit()