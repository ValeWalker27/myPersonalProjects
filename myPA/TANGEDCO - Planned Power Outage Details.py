import os
from time import sleep

from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-errors-spki-list")
options.add_argument("--ignore-certificate-errors")
options.add_argument("--ignore-ssl-errors")
options.add_argument("--start-maximized")

os.environ["WDM_LOG"] = "0"
os.environ["WDM_LOG_LEVEL"] = "0"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.set_page_load_timeout(300)
# driver.maximize_window()

# Row number 6 => Chennai
# Row number 36 => Tirunelveli

for row in [6, 36]:
    
    driver.get('https://www.tnebltd.gov.in/outages/viewshutdown.xhtml')
    sleep(2)
    
    driver.find_element(By.XPATH, '//main/section/div/div/div/form/div/div[2]/table/tbody/tr[1]/td[2]/div/div[3]/span').click()
    sleep(1)
    driver.find_element(By.XPATH, f'//div[3]/div/ul/li[{row}]').click()
    sleep(1)

    driver.find_element(By.XPATH, '//main/section/div/div/div/form/div/div[2]/table/tbody/tr[1]/td[3]/button').click()
    sleep(5)

    for row in driver.find_elements(By.XPATH, '//*[@id="wrap"]/div/form/div/div/div/div[2]/div/table/tbody/tr'):
        print (f"\nTown:\t\t{row.find_element(By.XPATH, 'td[2]').text}")
        print (f"Substation:\t{row.find_element(By.XPATH, 'td[3]').text}")
        print (f"Location:\t{row.find_element(By.XPATH, 'td[5]').text}")
        print (f"From:\t\t{row.find_element(By.XPATH, 'td[7]').text} to {row.find_element(By.XPATH, 'td[8]').text}")
