from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com/locations/server/")

#id = driver.find_element(By.XPATH, "/html/body/div/table/tbody[2]/tr[136]/td[1]").text
Vel = driver.find_element(By.XPATH, "//tr[td[text()='Velence']]/td[1]").text
Bat= driver.find_element(By.XPATH, "//tr[td[text()='Báta']]/td[1]").text

Vel=int(Vel)
print(Vel)
print(type(Vel))

Bat=int(Bat)
print(Bat)
print(type(Bat))

print(Bat+Vel)

driver.close()