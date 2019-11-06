from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://lordiman92.github.io/first-project/")
driver.find_element(By.XPATH, "/html/body/form/input[1]").send_keys("32")
driver.find_element(By.XPATH, "/html/body/form/input[2]").send_keys("23")
driver.find_element(By.XPATH, "/html/body/form/input[3]").click()

h1 = driver.find_element(By.XPATH, "//h1").text
print(h1)

assert h1 == "Számológép"


driver.close()




