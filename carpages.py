# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# page = requests.get('https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7')

# soup = BeautifulSoup(page.text, 'lxml')

# postings = soup.find_all('div', class_ = 't-flex t-gap-6 t-items-start t-p-6')

# df = pd.DataFrame({'link': [''], 'name': [''], 'price': [''], 'color': ['']})

# for post in postings:
#     link = post.find('a', class_ = 't-flex t-items-start t-w-[130px] t-shrink-0').get('href')
#     link_full = 'https://www.carpages.ca'+ link
#     name = post.find('h4', class_ = 'hN').text.strip()
#     price = post.find('span', class_ = 't-font-bold t-text-xl')
#     color = post.find('span', class_ = 't-text-sm t-font-bold').text.strip()
    
#     price_text = price.text.strip() if price else 'N/A'
#     df = df.append({'link': link_full, 'name': name, 'price': price, 'color': color}, ignore_index = True)
    
    
    
import requests
from bs4 import BeautifulSoup
import pandas as pd

page = requests.get('https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7')

soup = BeautifulSoup(page.text, 'lxml')

postings = soup.find_all('div', class_='t-flex t-gap-6 t-items-start t-p-6')

df = pd.DataFrame({'link': [], 'name': [], 'price': [], 'color': []})

for post in postings:
    link = post.find('a', class_='t-flex t-items-start t-w-[130px] t-shrink-0').get('href')
    link_full = 'https://www.carpages.ca' + link
    name = post.find('h4', class_='hN').text.strip()
    price = post.find('span', class_='t-font-bold t-text-xl')
    color = post.find('span', class_='t-text-sm t-font-bold').text.strip()

    # Extract text from the price object
    price_text = price.text.strip() if price else 'N/A'

    df = df.append({'link': link_full, 'name': name, 'price': price_text, 'color': color}, ignore_index=True)

print(df)
    
    
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd

# page = requests.get('https://www.carpages.ca/used-cars/search/?fueltype_id%5B0%5D=3&fueltype_id%5B1%5D=7')

# soup = BeautifulSoup(page.text, 'lxml')

# postings = soup.find_all('div', class_='t-flex t-gap-6 t-items-start t-p-6')

# df = pd.DataFrame({'link': [], 'name': [], 'price': [], 'color': []})

# counter = 0
# while counter < 20:
    
#     postings = soup.find_all('div', class_='t-flex t-gap-6 t-items-start t-p-6')   
    
    
#     for post in postings:
#         link = post.find('a', class_='t-flex t-items-start t-w-[130px] t-shrink-0').get('href')
#         link_full = 'https://www.carpages.ca' + link
#         name = post.find('h4', class_='hN').text.strip()
#         price = post.find('span', class_='t-font-bold t-text-xl')
#         color = post.find('span', class_='t-text-sm t-font-bold').text.strip()
    
#         # Check if price is not None before accessing text attribute
#         price_text = price.text.strip() if price else 'N/A'
    
#         df = df.append({'link': link_full, 'name': name, 'price': price_text, 'color': color}, ignore_index=True)
#         next_page = soup.find('a', class_ = 'nextprev').get('href')
#         page = requests.get(next_page)
#         soup = BeautifulSoup(page.text, 'lxml')
        
#         counter += 1
    


