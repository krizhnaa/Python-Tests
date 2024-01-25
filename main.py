from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_driver_path = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

URL = "https://www.python.org/"
driver.get(url=URL)

dates = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/time')

titles = driver.find_elements(By.XPATH, value='//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li/a')

events = {}

for n in range(len(dates)):
    events[n] = {
        "time": dates[n].text,
        "name": titles[n].text
    }

print(events)

driver.quit()
