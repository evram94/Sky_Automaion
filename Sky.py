from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import time


driver = webdriver.Chrome()
driver.get("https://www.skyscanner.net/")
assert "skyscanner" in driver.title
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="fsc-destination-search"]'))
          )
finally:
    elem = driver.find_element_by_xpath('//*[@id="fsc-destination-search"]')

elem.clear()
elem.send_keys("Köln (CGN)")
driver.find_element_by_xpath('//*[@id="flights-search-controls-root"]/div/div/form/div[3]/button').click()
time.sleep(5)
assert "No results found." not in driver.page_source

try:
    element = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/button[2]/p[1]'))
          )
finally:
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[2]/button[2]/p[1]').click()
    
Direct = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[1]/dl[1]/div/dd/div/div/div[1]/label/input')
OneStop = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[1]/dl[1]/div/dd/div/div/div[2]/label/span')
TwoPlusStops = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[1]/dl[1]/div/dd/div/div/div[3]/label/span')
time.sleep(5)

        
if Direct.is_selected():
            
            OneStop.click()
            TwoPlusStops.click()
            
else:
          
            TwoPlusStops.click()

time.sleep(3)        
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[1]/div/a').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[3]/div/div/section/div/div/div[1]/div[4]/div[1]/div[2]/a').click()
time.sleep(5)
driver.quit()
print("A round ticket from Cairo to London is booked")
time.sleep(3)
print("Exiting....., bye")
time.sleep(2)