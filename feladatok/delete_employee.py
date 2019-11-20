from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/create-employee.xhtml")

def delete_by_name(name):
    driver.find_element(By.XPATH, '//*[@name='name']/td[8]').click()

def find_id_by_name():