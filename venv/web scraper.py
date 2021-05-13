import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

driver = webdriver.Chrome(executable_path='C:/Users/LENOVO/Desktop/chromedriver.exe')
driver.get('https://downtowndallas.com/places/cambria-hotel/')
results = []

content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for b in soup.findAll(attrs='place-header'):
    best = b.find('h1')
    if best not in results:
        results.append(best.text)

for element in soup.findAll(attrs='place-info-address'):
    name = element.find('a')
    if name not in results:
        results.append(name.text)

for c in soup.findAll(attrs='place-info-image'):
    bestt = c.find('img')
    out = bestt.attrs['src']
    if bestt not in results:
        results.append(out)



print(results)

df = csv.writer(open('Scraping.csv','w'))
df.writerow(['Name','Address','Phone','Area','Image URL'])
df.writerow([results[0],results[1],results[2],results[3],results[4]])

