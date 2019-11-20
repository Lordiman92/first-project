from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/empapp/create-employee.xhtml")


def print_welcome():
    print('Welcome')


def click_to_name_input():
    driver.find_element(By.ID, 'create-form:name-input').click()


def type_to_name_input():
    szoveg = input("Írj: ")
    driver.find_element(By.ID, 'create-form:name-input').send_keys(szoveg)


def click_to_header():
    driver.find_element(By.XPATH, '//h1').click()


def wait_for_error_msg(message):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, "//span[@class = 'invalid-feedback']"), message))


def w8_4_monogram(expected_monogram):
    WebDriverWait(driver, 10).until(
        expected_conditions.text_to_be_present_in_element((By.ID, 'create-form:monogram-text'), expected_monogram))
    #monogram = driver.find_element(By.ID, 'create-form:monogram-text').text
    print(str(expected_monogram))


print_welcome()
click_to_name_input()
click_to_header()
click_to_name_input()
type_to_name_input()
click_to_header()
wait_for_error_msg('Az alkalmazott nevét meg kell adni!')
w8_4_monogram('JD')
