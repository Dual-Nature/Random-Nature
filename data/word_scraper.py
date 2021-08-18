from os import write
from bs4 import BeautifulSoup
from constants import BASIC_EMOTIONS
import requests
import csv

URL = 'https://www.enchantedlearning.com/wordlist/emotions.shtml'
r = requests.get(URL)
# print(r.content)
soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())
table = soup.find_all('div', attrs={'class': 'wordlist-item'})
# print(table)
word_list = []
for item in table:
    # print(item.get_text())
    word_list.append(item.get_text())

with open('word_list.csv', 'w', newline= '') as f:
    writer = csv.writer(f)
    writer.writerow(['words']+ BASIC_EMOTIONS)
    for word in word_list:
        writer.writerow([word])