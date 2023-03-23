import pytest
from selenium import webdriver
from features.pages.GoogleLandingPagePO import GoogleLandingPagePO


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.google.com/")
    yield driver
    driver.quit()


def test_google_search(driver):
    glp_po = GoogleLandingPagePO(driver)
    glp_po.decline_consent()
    glp_po.enter_search_value("hello world")
    glp_po.click_search_button()

    assert "https://www.google.com/search?q=hello+world" in driver.current_url
