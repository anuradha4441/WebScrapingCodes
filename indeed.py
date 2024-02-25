from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome('/home/sandip/buildmeasure/darwin/driver/chromedriver')

driver.get('https://se.indeed.com/')
