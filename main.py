from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome_driver_path = ChromeDriverManager().install()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

URL = "https://www.flipkart.com/kissan-hazelnut-choco-peanut-spread-350-g/p/itmb2d3625ed1724?pid=JASGG44MPAHSQUUE&lid=LSTJASGG44MPAHSQUUEP22FVR&marketplace=FLIPKART&store=eat%2Fxhv&srno=b_1_2&otracker=browse&fm=organic&iid=en_-FTkwyChchLAImqdr77LZdquq17b6PS3YhGRekqdl6pdEdUEyaPz7GA42ygBVIVsnuu6BWU1uF4zmfluhKnfofUFjCTyOHoHZs-Z5_PS_w0%3D&ppt=browse&ppn=browse&ssid=a1sirsvpkw0000001706106955462"
driver.get(url=URL)

price = driver.find_element_by_class_name("_30jeq3._16Jk6d")
print(price.text)

driver.quit()
