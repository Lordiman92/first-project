from selenium import webdriver

from Pages.create_location_page import CreateLocationPage
from Pages.list_locations_page import ListLocationsPage
from Pages.location_details_page import LocationDetailsPage
from db.db_operations import DbOperation

driver = webdriver.Chrome()

list_page = ListLocationsPage(driver)
db_oper = DbOperation()
locdet_page= LocationDetailsPage(driver)

db_oper.delete_locations()
list_page.go()
list_page.assert_title_is_ok()
#list_page.assert_table_contains_location("Miskolc", "48.1034775, 20.7784384")
list_page.assert_count_of_table_rows_is(0)
list_page.click_to_create_location_link()
create_page = CreateLocationPage(driver)
create_page.fill_create_location_form()
create_page.click_to_create_button()
locdet_page.click_to_back_to_list_link()
list_page.assert_count_of_table_rows_is(1)



list_page.quit()