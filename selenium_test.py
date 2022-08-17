"""from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time


s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

driver.get("https://www.google.com")

time.sleep(10)

driver.close()"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser = webdriver.Firefox(executable_path="./selenium_firefox/drivers/geckodriver")
browser.get('https://www.linuxhint.com')
print('Title: %s' % browser.title)
browser.quit()