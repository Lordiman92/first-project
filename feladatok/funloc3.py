from selenium import webdriver
from selenium.webdriver.common.by import By


def print_coords_by_name(id):
    xpath = "//tr[td[text()='id']]/td[2]".replace("id", id)
    coords = driver.find_element(By.XPATH, xpath).text
    print(coords)


driver = webdriver.Chrome()
driver.get("http://www.learnwebservices.com/locations/server/")
print_coords_by_name("8369")
driver.close()