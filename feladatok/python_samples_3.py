from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("http://www.learnwebservices.com/locations/")


def print_when_between(name):
    wait_xpath = "//tbody/tr"
    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, wait_xpath)))

    lat = get_lat_by_name(name)

    if 48.2 <= lat <= 48.4:
        print('Nagyobb, mint 48')
    else:
        print('Kisebb')


def get_lat_by_name(name):
    xpath = "//tr[td[contains(text(),'name')]]/td[3]".replace("name", name)
    coords = driver.find_element(By.XPATH, xpath).text
    print(coords)
    lat = float(coords[0:coords.index(",")])
    print(lat)
    return lat









chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.learnwebservices.com/locations/")


