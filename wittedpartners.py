
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome('/home/sandip/buildmeasure/darwin/driver/chromedriver')

df = pd.DataFrame({'job_link': [], 'job_title': [], 'job_description': [], 'job_details': []})

for page_num in range(1, 3): 
    url = f'https://wittedpartners.com/projects/p3/?_paged={page_num}'
    driver.get(url)
    time.sleep(3)  
    soup = BeautifulSoup(driver.page_source, 'lxml')

    postings = soup.find_all('div', class_='p-30 m:p-50')

    for post in postings:
        container = post.find_parent('a')
        job_link = container.get('href') if container else ''
        job_title = post.find('h2', class_='ingress font-semibold mb-25').text.strip()
        job_description = post.find('p', class_='line-clamp mb-25').text.strip()
        job_details = post.find('ul', class_='flex flex-wrap mb-50').text.strip()

        df = df.append({
            'job_link': job_link,
            'job_title': job_title,
            'job_description': job_description,
            'job_details': job_details
        }, ignore_index=True)

driver.quit()
print(df)   


