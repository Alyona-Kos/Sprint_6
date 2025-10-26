from pages.landing_page import LandingPage
from pages.redirect_page import RedirectPage
import allure


@allure.suite("Тесты редиректов по логотипам")
class TestLogoRedirects:
    
    @allure.title("Тест редиректа на главную страницу через логотип Самоката")
    def test_logo_redirect(self, driver):
        with allure.step("Открываем главную страницу Самоката"):
            landing_page = LandingPage(driver)
            landing_page.open_url()

        with allure.step("Кликаем на кнопку заказа для перехода на страницу заказа"):
            landing_page.click_on_order_button()

        with allure.step("Кликаем на логотип Самоката в хедере"):
            redirect_page = RedirectPage(driver)
            redirect_page.click_on_logo_scooter()

        with allure.step("Проверяем, что произошел редирект на главную страницу"):
            current_url = redirect_page.get_current_url()
            expected_url = 'https://qa-scooter.praktikum-services.ru/'
            assert current_url == expected_url

    @allure.title("Тест редиректа на Дзен через логотип Яндекса")
    def test_logo_redirect_dzen(self, driver):
        with allure.step("Открываем главную страницу Самоката"):
            landing_page = LandingPage(driver)
            landing_page.open_url()

        with allure.step("Кликаем на логотип Яндекса в хедере"):
            redirect_page = RedirectPage(driver)
            redirect_page.click_on_logo_yandex()

        with allure.step("Проверяем, что открылась новая вкладка"):
            window_count = redirect_page.get_window_handles_count()
            assert window_count == 2

        with allure.step("Переключаемся на новую вкладку"):
            redirect_page.switch_to_window(1)

        with allure.step("Ожидаем загрузку страницы Дзена и проверяем элементы"):
            redirect_page.find_element_find_button()
            
        with allure.step("Проверяем, что URL содержит 'dzen'"):
            current_url = redirect_page.get_current_url()
            assert 'dzen' in current_url