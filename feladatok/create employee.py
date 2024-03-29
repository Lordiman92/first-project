from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/create-employee.xhtml")

driver.find_element(By.ID, 'create-form:name-input').click()
driver.find_element(By.XPATH, '//h1').click()

WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element((By.XPATH,"//span[@class = 'invalid-feedback']"), "Az alkalmazott nevét meg kell adni!"))

error_message = driver.find_element(By.XPATH, "//span[@class = 'invalid-feedback']").text
print(error_message)

