from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


# https://sites.google.com/chromium.org/driver/

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://google.com")


input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.send_keys("grabdocs" + Keys.ENTER)

time.sleep(60)

input_element = driver.find_element(By.CSS_SELECTOR, ".LC20lb.MBeuO.DKV0Md")
ActionChains(driver).context_click(input_element).perform()

driver.quit()





