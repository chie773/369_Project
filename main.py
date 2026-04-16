from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# https://sites.google.com/chromium.org/driver/

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

wait = WebDriverWait(driver, 10)

driver.get("https://app.grabdocs.com/")
time.sleep(5)

original_window = driver.current_window_handle
assert len(driver.window_handles) == 1

input_element = driver.find_element(By.ID, "username")
input_element.send_keys("chieburuoh@gmail.com")

input_element = driver.find_element(By.ID, "password")
input_element.send_keys("Chibueze123!")

time.sleep(1)

element = driver.find_elements(By.TAG_NAME, "button")
for e in element:
    if e.text == "Sign in":
        e.click()
        break


time.sleep(20)


driver.find_element(By.CSS_SELECTOR, '[title="Reach"]').click()

time.sleep(5)

elements = driver.find_elements(By.TAG_NAME, "button")

for e in elements:
    if e.text == "Create Meeting":
        e.click()
        break

time.sleep(5)

input_element = driver.find_elements(By.TAG_NAME, "input")
for i in input_element:
    if i.get_attribute("placeholder") == "Enter meeting name":
        i.send_keys("Test Meeting")

time.sleep(5)

elements = driver.find_element(By.CSS_SELECTOR, '[class="bg-white dark:bg-gray-800 rounded-lg shadow-xl max-w-sm w-full mx-4 border border-gray-200 dark:border-gray-700"]')
print(elements.tag_name)
s_element = elements.find_elements(By.TAG_NAME, "button")


for e in s_element:
    if e.text == "Create Meeting":
        e.click()
        break

time.sleep(10)


s_element = driver.find_elements(By.TAG_NAME, "button")

for e in s_element:
    if e.get_attribute("title") == "Join meeting":
        e.click()
        break

time.sleep(5)


elements = driver.find_element(By.CSS_SELECTOR, '[class="w-full text-blue-600 dark:text-blue-400 hover:underline font-medium py-2"]').click()


# for e in s_element:
#     if e.text == "Continue without microphone and camera":
#         e.click()
#         break


time.sleep(10)


wait.until(EC.number_of_windows_to_be(2))
for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break


time.sleep(10)

input_element = driver.find_elements(By.TAG_NAME, "input")
for i in input_element:
    if i.get_attribute("placeholder") == "Enter name":
        i.send_keys("Chibueze Eburuoh")
        break

time.sleep(10)


s_element = driver.find_elements(By.TAG_NAME, "button")


for e in s_element:
    if e.text == "Join Now":
        e.click()
        break

time.sleep(10)

driver.switch_to.window(original_window)

driver.find_element(By.CSS_SELECTOR, '[title="Chat"]').click()
time.sleep(5)

input_element = driver.find_elements(By.TAG_NAME, "textarea")
for i in input_element:
    if i.get_attribute("placeholder") == "Type a message... Use @ to mention users or workspaces":
        i.send_keys("This is a message Test")
        break

time.sleep(3)

s_element = driver.find_elements(By.TAG_NAME, "button")


for e in s_element:
    if e.get_attribute("class") == "px-3 py-1.5 bg-blue-600 text-white rounded-lg hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed transition-colors":
        e.click()
        break

time.sleep(50)



driver.quit()



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





