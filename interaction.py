from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

URL = "https://secure-retreat-92358.herokuapp.com/"
driver.get(url=URL)

f_name = driver.find_element(By.NAME, value="fName")
f_name.send_keys("Krizhna")

l_name = driver.find_element(By.NAME, value="lName")
l_name.send_keys("Brem")

mail = driver.find_element(By.NAME, value="email")
mail.send_keys("lololol@gmail.com")

butt = driver.find_element(By.CLASS_NAME, value="btn")
butt.click()

# driver.quit()