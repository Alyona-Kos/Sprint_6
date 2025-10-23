
from pages.landing_page import LandingPage
from pages.redirect_page import RedirectPage
import allure



def test_LOGO_REDIRECT(driver):
    order_page = LandingPage(driver)
    order_page.open_url()

    with allure.step(f"Проверяем переход на главную страницу Я.Самокат при клике на Лого сервиса в шапке"):
        order_page.click_on_order_button()

        logo_page = RedirectPage(driver)
        logo_page.click_on_LOGO_SCOOTER()
        assert logo_page.get_current_url() == 'https://qa-scooter.praktikum-services.ru/'


def test_LOGO_REDIRECT_DZEN(driver):
    order_page = LandingPage(driver)
    order_page.open_url()

    with allure.step('Проверяем редирект при клике на логотип яндекса в хедере.'):
        redirect_dzen_test = RedirectPage(driver)
        redirect_dzen_test.click_on_LOGO_YANDEX()

        # Переключаемся на новую вкладку:
        handles = driver.window_handles
        assert len(handles) == 2
        driver.switch_to.window(handles[1])
        redirect_dzen_test.find_element_find_button()
        final_url = redirect_dzen_test.get_current_url()
        assert 'dzen' in final_url