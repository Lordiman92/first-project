from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com/locations/server/")

#id = driver.find_element(By.XPATH, "/html/body/div/table/tbody[2]/tr[136]/td[1]").text
t1 = driver.find_element(By.XPATH, "//tr[td[text()='Tiszakerecseny']]/td[3]").text
t2 = driver.find_element(By.XPATH, "//tr[td[text()='Tiszarád']]/td[3]").text

t11=float(t1.split(";"))
#t12=float()
#t21=float()
#t22=float()

print(t11)

driver.close()