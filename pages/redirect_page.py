import allure
from pages.base_page import BasePage
from locators.locators_landing_page import Testlocators
from locators.locators_redirect_page import Redirect_page_locators




class RedirectPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по Лого Самокат в шапке Сервиса')
    def click_on_LOGO_SCOOTER(self):
        self.click_on_element(Testlocators.LOGO_SCOOTER)

    @allure.step('Клик по Лого Яндекс в шапке Сервиса')
    def click_on_LOGO_YANDEX(self):
        self.click_on_element(Testlocators.YA_LOGO)

    @allure.step('Проверка перепоха на главную Дзена')
    def find_element_find_button(self):
        self.find_element_with_wait(Redirect_page_locators.FIND_BUTTON)