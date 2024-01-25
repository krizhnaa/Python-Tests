from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_driver_path = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

URL = "https://en.wikipedia.org/wiki/Main_Page"
driver.get(url=URL)

no_of_articles = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a')
print(no_of_articles.text)

driver.quit()