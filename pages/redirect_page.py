from selenium.webdriver.common.by import By
from .base_page import BasePage  # относительный импорт из той же папки


class RedirectPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.logo_scooter = (By.XPATH, "//a[@class='Header_LogoScooter__3lsAR']")
        self.logo_yandex = (By.XPATH, "//a[@class='Header_LogoYandex__3TSOI']")
        self.find_button = (By.XPATH, "//form//button")
        self.dzen_page_indicator = (By.CSS_SELECTOR, "[data-testid='dzen-header']")

    def click_on_logo_scooter(self):
        self.click_element(self.logo_scooter)

    def click_on_logo_yandex(self):
        self.click_element(self.logo_yandex)

    def find_element_find_button(self):
        return self.find_element(self.find_button)

    def wait_for_dzen_page_load(self):
        self.wait_for_element_visible(self.dzen_page_indicator)

    def is_dzen_page_loaded(self):
        return self.is_element_visible(self.dzen_page_indicator)

    def get_scooter_logo_url(self):
        logo_element = self.find_element(self.logo_scooter)
        return logo_element.get_attribute("href")

    def get_yandex_logo_url(self):
        logo_element = self.find_element(self.logo_yandex)
        return logo_element.get_attribute("href")