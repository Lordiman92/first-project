from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://lordiman92.github.io/first-project/")
driver.find_element(By.XPATH, "/html/body/form/div/input[1]").send_keys("32")
driver.find_element(By.XPATH, "/html/body/form/div/input[2]").send_keys("23")
driver.find_element(By.XPATH, "/html/body/form/div/input[3]").click()

h1 = driver.find_element(By.XPATH, "//h1").text
eredmeny = driver.find_element(By.CSS_SELECTOR, "#result-input").get_attribute("value")
print(h1)
print(eredmeny)

assert h1 == "Számológép"
assert eredmeny == '53'

driver.close()




