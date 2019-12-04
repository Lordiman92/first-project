from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("http://localhost:8081")


xpath = "//h2"


def assert_title_is(title):
    cim = driver.title
    assert cim == title
    print(cim)


def assert_header_is(title):
    cim = driver.find_element(By.XPATH, xpath).text
    assert cim == title
    print(cim)


def assert_image_is_present(kepnev):
    keppath = "//img[contains(@src,'image')]"
    keppath = keppath.replace("image", kepnev)
    #driver.find_element(By.XPATH, keppath)
    kep = len(driver.find_elements(By.XPATH, keppath))
    assert kep > 0
    if (len(driver.find_elements(By.XPATH, keppath)) > 0):
        print("Van képed hozzá")


def goto_home_page():
    xpathe="//a[contains(@href,'/')]"
    driver.find_element(By.XPATH, xpathe).click()
    print("I'm @ " + driver.find_element(By.XPATH, "//a[contains(@title, 'home page')]/span[2]").text)


def goto_find_owners():
    xpathe="//a[contains(@href,'/owners/find')]"
    driver.find_element(By.XPATH, xpathe).click()
    print("I'm @ " + driver.find_element(By.XPATH, "//a[contains(@title, 'find owners')]/span[2]").text)

def goto_veterinarians():
    xpathe="//a[contains(@href,'/vets.html')]"
    driver.find_element(By.XPATH, xpathe).click()
    print("I'm @ " + driver.find_element(By.XPATH, "//a[contains(@title, 'veterinarians')]/span[2]").text)


def print_veterinarian_count():
    goto_veterinarians()
    xpathi = "//tbody/tr"
    db = len(driver.find_elements(By.XPATH, xpathi))
    print(db)


def print_veterinarian_names():
    goto_veterinarians()
    xpathh = "//td[1]"
    nevek = driver.find_elements(By.XPATH, xpathh)
    for nev in nevek:
        print(nev.text)

def test_home_page():
    assert_title_is("PetClinic :: a Spring Framework demonstration")
    assert_header_is("Welcome")
    assert_image_is_present("pets.png")
    goto_home_page()
    goto_find_owners()
    goto_veterinarians()
    print_veterinarian_count()
    print_veterinarian_names()


test_home_page()



driver.quit()
