from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com/locations/server/")

#id = driver.find_element(By.XPATH, "/html/body/div/table/tbody[2]/tr[136]/td[1]").text
name = driver.find_element(By.XPATH, "//tr[td[text()='11116']]/td[2]").text
name1 = driver.find_element(By.XPATH, "//tr[td[text()='11117']]/td[2]").text
name2 = driver.find_element(By.XPATH, "//tr[td[text()='11118']]/td[2]").text

print(name + '-' + name1 + '-' + name2)


driver.close()