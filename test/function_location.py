from selenium import webdriver
from selenium.webdriver.common.by import By


def print_coords_by_name(name):
    xpath = "//tr[td[text()='name']]/td[3]".replace("name", name)
    coords = driver.find_element(By.XPATH, xpath).text
    print(coords)


driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/locations/server/")
print_coords_by_name("Aba")
driver.close()
