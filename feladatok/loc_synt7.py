from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com/locations/server/")

#id = driver.find_element(By.XPATH, "/html/body/div/table/tbody[2]/tr[136]/td[1]").text
name = driver.find_element(By.XPATH, "//tr[td[text()='Tolmács']]/td[3]").text

jo= name.replace(',',' ')
print(jo.replace('.',','))

driver.close()