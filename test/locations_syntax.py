from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com/locations/server/")

coordinates = driver.find_element(By.XPATH, "/html/body/div/table/tbody[2]/tr[578]/td[3]").text
print(coordinates)
print(type(coordinates))

driver.close()