from selenium import webdriver
import bs4
#driver = webdriver.Firefox(firefox_binary="/usr/bin/firefox-esr")

#driver.get('https://www.baseball-reference.com/players/j/judgeaa01.shtml')

#elem = driver.find_elements_by_css_selector('.groupstuff > div:nth-child(2) > p:nth-child(1) > a:nth-child(1)')
#elem.click()

#driver.back()
#driver.forwad()
#driver.refresh()
#driver.quit()

import requests

res = requests.get('https://www.baseball-reference.com/players/j/judgeaa01.shtml')
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')

#elem = driver.find_element_by_css_selector('#batting_standard')
table = soup.select('#batting_standard')
formatted = table.replace(' ', '\t')
print(formatted)
