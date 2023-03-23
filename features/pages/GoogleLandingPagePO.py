from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium import webdriver


class GoogleLandingPagePO:
    def __init__(self, driver):
        self.driver = driver
        #self.search_input = (By.CSS_SELECTOR, '[title="Suche"]')
        self.search_input = (By.NAME, "q")
        #self.search_button = (By.CSS_SELECTOR, '[type="submit"]')
        self.search_button = (By.XPATH, '//form/div/div/div/center/input[@name="btnK"]')
        self.consent_decline_button = (By.XPATH, "//button/div[contains(text(),'Alle ablehnen')]")

    def decline_consent(self):
        self.driver.find_element(*self.consent_decline_button).click()

    def enter_search_value(self, value):
        self.driver.find_element(*self.search_input).send_keys(value)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    @given("I am on the Google homepage")
    def step_impl(context):
        context.driver = webdriver.Chrome()
        context.driver.get("https://www.google.com/")

    @when('I enter "{term}" in the search box')
    def step_impl(context, term):
        context.enter_search_value(term)

    @when('I click the "Search" button')
    def step_impl(context):
        context.click_search_button()

    @then('I should see search results for "{term}"')
    def step_impl(context, term):
        search_results = context.driver.find_elements_by_css_selector('.g')
        for result in search_results:
            assert term.lower() in result.text.lower()

        context.driver.quit()
