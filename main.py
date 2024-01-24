from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_driver_path = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

URL = "https://github.com/krizhnaa"
driver.get(url=URL)

name = driver.find_element(By.XPATH, value='/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1/span[1]')
print(name.text)

driver.quit()
