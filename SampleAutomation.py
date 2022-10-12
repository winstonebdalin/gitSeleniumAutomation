from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj = Service(executable_path="C:\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://shop.thetestingworld.com/")

driver.find_element(By.XPATH, "//input[@name='search']").send_keys('Mac')
driver.find_element(By.CSS_SELECTOR, ".btn.btn-default.btn-lg").click()

products = driver.find_elements(By.CSS_SELECTOR, ".product-layout")
