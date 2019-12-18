from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from Pages.create_location_page import CreateLocationPage
from Pages.list_locations_page import ListLocationsPage
from Pages.location_details_page import LocationDetailsPage
from create_location import list_page, locdet_page
from db.db_operations import DbOperation


class TestLocations:

    def setup_method(self):
        self.db_oper = DbOperation()
        self.db_oper.delete_locations()
        self.driver = webdriver.Chrome()
        self.locdet_page = LocationDetailsPage(self.driver)
        self.list_page = ListLocationsPage(self.driver)
        self.create_page = CreateLocationPage(self.driver)

    def teardown_method(self):
        self.driver.close()

    def test_empty_table(self):
        self.list_page.go()
        self.list_page.assert_count_of_table_rows_is(0)

    def test_when_create_location_then_details_are_correct(self):
        self.create_location()
        self.locdet_page.assert_details_are("Budapest", "1.0, 1.0")
        self.locdet_page.assert_message_has_been_appeared("Location has been created.")

    def test_when_create_loc_app_in_the_table(self):
        self.create_location()

        self.locdet_page.click_to_back_to_list_link()
        self.list_page.assert_table_contains_location("Budapest", "1.0, 1.0")

    def test_when_create_20_locations_then_appears_in_the_table(self):
        with open("../cities.csv", encoding="UTF-8") as file:
            for line in file:
                (name, lat, lon) = line.strip().split(",")
                self.create_location(name, f"{lat},{lon}")
        self.list_page.go()
        self.list_page.assert_count_of_table_rows_is(20)

    def create_location(self, name="Budapest", coords="1,1"):
        self.list_page.go()
        self.list_page.click_to_create_location_link()
        self.create_page.fill_create_location_form(name, coords)
        self.create_page.click_to_create_button()




