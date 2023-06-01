from Tbilgi import kullanacıAdı,Sifre
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.options import Options

options=Options()

options.add_experimental_option('excludeSwitches',['enable,-logging'])

driver=webdriver.Chrome(executable_path=r"/Users/sevketugurel/Desktop/Python Kişisel Notlarım/chromedriver.exe",chrome_options=options)

url ="https://twitter.com/i/flow/login"

driver.get(url)
time.sleep(2)
driver.maximize_window()
time.sleep(2)

ka=driver.find_elements(By.XPATH,"//input[@autocomplete='username']")[0]
ka.send_keys(kullanacıAdı)
time.sleep(2)
ka.send_keys(Keys.ENTER)
time.sleep(3)

sif=driver.find_elements(By.XPATH,"//input[@autocomplete='current-password']")[0]
sif.send_keys(Sifre)
time.sleep(2)
sif.send_keys(Keys.ENTER)
time.sleep(3)




