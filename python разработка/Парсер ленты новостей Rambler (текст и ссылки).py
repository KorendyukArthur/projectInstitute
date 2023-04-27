import time
import requests
from bs4 import BeautifulSoup
 
#while True:
# Making a GET request
r = requests.get('https://www.rambler.ru/?utm_source=news_media&utm_campaign=self_promo&utm_medium=topline&utm_content=head')
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
# Getting the leftbar
leftbar = soup.find('div', class_='r-iCBQweh7')
# All the li under the above ul
lines = leftbar.find_all('a')
for line in lines:
    print(line.text)
# персер ссылок на сайте
for line1 in lines:
    print(line.get('href'))
    
    #time.sleep()