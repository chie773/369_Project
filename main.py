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


driver.get("https://app.grabdocs.com/")

time.sleep(10)

input_element = driver.find_element(By.ID, "username")
input_element.send_keys("chieburuoh@gmail.com")

time.sleep(2)

input_element = driver.find_element(By.ID, "password")
input_element.send_keys("Chibueze123!")

time.sleep(2)

element = driver.find_elements(By.TAG_NAME, "button")
for e in element:
    if e.text == "Sign in":
        e.click()
        break


time.sleep(20)


driver.find_element(By.CSS_SELECTOR, '[title="Reach"]').click()


# input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
# input_element.send_keys("grabdocs" + Keys.ENTER)

# time.sleep(20)

# driver.find_element(By.CSS_SELECTOR, ".LC20lb.MBeuO.DKV0Md").click()

# time.sleep(20)

# driver.find_element(By.CSS_SELECTOR, ".btn.text-white.px-6.py-2.rounded-lg.font-medium.transition-all.duration-200.flex.items-center.space-x-2").click()

# time.sleep(10)

# input_element = driver.find_element(By.ID, "username")
# input_element.send_keys("chieburuoh@gmail.com")

# time.sleep(2)

# input_element = driver.find_element(By.ID, "password")
# input_element.send_keys("Chibueze123!")


# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR, "button.rounded-xl.bg-blue-600.px-8.py-3.text-xl.font-bold.text-white.shadow-sm.transition-all.duration-200.hover:bg-blue-700.hover:shadow-lg.focus:outline-none.focus:ring-2.focus:ring-blue-500.focus:ring-offset-2.disabled:opacity-60.disabled:cursor-not-allowed.w-full.flex.justify-center.items-center.font-['Space_Grotesk',sans-serif]").click()


# time.sleep(30)





