import pytest
from pages.home_page import HomePage

def test_full_purchase_flow(driver):
    # --- INIT PAGE ---
    home_page = HomePage(driver)

    # --- HOME ---
    home_page.select_pop_up()
    home_page.select_accept()
    home_page.select_notification()
    home_page.select_allow()
    home_page.select_automation_module()