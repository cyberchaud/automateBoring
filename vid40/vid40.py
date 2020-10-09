import bs4
import requests

res = requests.get('https://www.baseball-reference.com/players/j/judgeaa01.shtml')

res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, 'html.parser')
height = soup.select('#meta > div:nth-child(2) > p:nth-child(4) > span:nth-child(1)')
weight = soup.select('#meta > div:nth-child(2) > p:nth-child(4) > span:nth-child(2)')

print(height, weight)
print("Aaron Judge's height is: " + height[0].text)
print("Aaron Judge's weight is: " + weight[0].text)