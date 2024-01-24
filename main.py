from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

URL = "https://www.google.com/"
driver.get(url=URL)

driver.quit()
