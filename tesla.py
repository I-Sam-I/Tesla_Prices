from selenium import webdriver
from bs4 import BeautifulSoup
from re import compile
import pyautogui as pag
from sys import exit


driver = webdriver.Chrome()
driver.minimize_window()
driver.get("https://www.tesla.com/inventory/new/my?arrangeby=plh&zip=75035&range=200")

content = driver.page_source
driver.close()

soup = BeautifulSoup(content, features='lxml')

for span in soup.findAll('span', attrs={'class': 'result-purchase-price tds-text--h4'}, limit=1, string=compile(r'^\$\d{2},\d{3}')):
    price = int(span.text.replace('$', '').replace(',', ''))
    
    if price < 50000:
        pag.alert(text=f"Price is ${price:,}", title="Alert")

exit()