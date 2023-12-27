import sys
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pyautogui

###########################
# Loop of all the pages
###########################

#Loop to go over all pages
pages = open(sys.argv[1])
data=[]
chop = webdriver.ChromeOptions()
path = "./src.crx"
chop.add_extension(path)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = chop)
action = ActionChains(driver)
driver.get("https://www.google.com")
sleep(3)

for page in pages:
    print(page)
    driver.get(page)
    sleep(1)
    pyautogui.click()
    sleep(1)