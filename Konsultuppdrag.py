import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

driver = webdriver.Chrome('/home/sandip/buildmeasure/darwin/driver/chromedriver')

url = 'https://upgraded.se/lediga-uppdrag/'

driver.get(url)
soup = BeautifulSoup(driver.page_source, 'lxml')

table = soup.find('table', class_ = 'konsultuppdrag-table')
table

headers = []

for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)
df = pd.DataFrame(columns = headers)