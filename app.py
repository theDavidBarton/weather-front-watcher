import re
import urllib.request
from bs4 import BeautifulSoup

with urllib.request.urlopen('https://www.hazipatika.com/orvosmeteorologia') as response:
    html = response.read()
soup = BeautifulSoup(html, 'html.parser')
front_name = soup.css.select('.o-humanMeteoDay__frontEffectBox span')[0].text.lower()

if 'hidegfront' in front_name:
    print('hidegfront 🥶')
elif 'melegfront' in front_name:
    print('melegfront 🥵')
elif 'kettősfront' in front_name:
    print('kettősfront 🤕')
else:
    print('nincs front 😊')
