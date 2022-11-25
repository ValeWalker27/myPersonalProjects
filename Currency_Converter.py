import os
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors-spki-list")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--start-maximized")
options.add_argument("--headless")

os.environ["WDM_LOG"] = "0"
os.environ["WDM_LOG_LEVEL"] = "0"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_page_load_timeout(300)

driver.get("https://www.currencyconverterx.com/USD/INR/1")
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'convert-form__result')))

print (driver.find_element(By.CLASS_NAME, "convert-form__result").find_element(By.XPATH, 'strong/span[3]').text)
print (driver.find_element(By.XPATH, '//*[@class="table__responsive"]/table/tbody/tr/td[2]').text)
