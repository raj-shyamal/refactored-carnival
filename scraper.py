from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import time


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.codechef.com/")

time.sleep(10)


html = driver.page_source

print(html)
