from pages.order_page import OrderPage
import allure
import pytest


@allure.suite("Тесты успешного оформления заказа")
class TestOrderSuccess:
    
    @allure.title("Тест оформления заказа через кнопку в хедере")
    def test_order_via_header_button(self, driver):
        with allure.step("Открываем главную страницу"):
            order_page = OrderPage(driver)
            order_page.open_url()

        with allure.step("Кликаем на кнопку заказа в хедере"):
            order_page.click_header_order_button()

        with allure.step("Заполняем первую страницу формы заказа"):
            order_page.fill_first_order_page(
                name="Иван",
                surname="Петров",
                address="ул. Ленина, д. 10",
                metro_station="Сокольники",
                phone="+79991234567"
            )
            order_page.click_next_button()

        with allure.step("Заполняем вторую страницу формы заказа"):
            order_page.fill_second_order_page(
                delivery_date="2024-12-31",
                rental_period="сутки",
                color="black",
                comment="Позвонить за час до доставки"
            )
            order_page.click_order_button()

        with allure.step("Подтверждаем заказ в модальном окне"):
            order_page.confirm_order()

        with allure.step("Проверяем успешное оформление заказа"):
            assert order_page.is_order_successful(), "Заказ не был успешно оформлен"

    @allure.title("Тест оформления заказа через кнопку на странице")
    def test_order_via_page_button(self, driver):
        with allure.step("Открываем главную страницу"):
            order_page = OrderPage(driver)
            order_page.open_url()

        with allure.step("Кликаем на кнопку заказа на странице"):
            order_page.click_page_order_button()

        with allure.step("Заполняем первую страницу формы заказа"):
            order_page.fill_first_order_page(
                name="Иван",
                surname="Петров",
                address="ул. Ленина, д. 10",
                metro_station="Сокольники",
                phone="+79991234567"
            )
            order_page.click_next_button()

        with allure.step("Заполняем вторую страницу формы заказа"):
            order_page.fill_second_order_page(
                delivery_date="2024-12-31",
                rental_period="сутки",
                color="black",
                comment="Позвонить за час до доставки"
            )
            order_page.click_order_button()

        with allure.step("Подтверждаем заказ в модальном окне"):
            order_page.confirm_order()

        with allure.step("Проверяем успешное оформление заказа"):
            assert order_page.is_order_successful(), "Заказ не был успешно оформлен"

    @allure.title("Тест полного оформления заказа с использованием удобного метода")
    def test_complete_order_flow(self, driver):
        with allure.step("Открываем главную страницу"):
            order_page = OrderPage(driver)
            order_page.open_url()

        with allure.step("Кликаем на кнопку заказа в хедере"):
            order_page.click_header_order_button()

        with allure.step("Выполняем полный процесс оформления заказа"):
            order_data = {
                'name': 'Мария',
                'surname': 'Сидорова',
                'address': 'пр. Мира, д. 25',
                'metro_station': 'Лубянка',
                'phone': '+79987654321',
                'delivery_date': '2024-12-25',
                'rental_period': 'двое суток',
                'color': 'grey',
                'comment': 'Оставить у двери'
            }
            order_page.make_complete_order(order_data)

        with allure.step("Проверяем успешное оформление заказа"):
            assert order_page.is_order_successful(), "Заказ не был успешно оформлен"

    @allure.title("Тест оформления заказа с минимальными данными")
    def test_minimal_order_data(self, driver):
        with allure.step("Открываем главную страницу"):
            order_page = OrderPage(driver)
            order_page.open_url()

        with allure.step("Кликаем на кнопку заказа на странице"):
            order_page.click_page_order_button()

        with allure.step("Заполняем первую страницу формы заказа минимальными данными"):
            order_page.fill_first_order_page(
                name="Анна",
                surname="Иванова",
                address="ул. Пушкина, д. 1",
                metro_station="Красные Ворота",
                phone="+79991112233"
            )
            order_page.click_next_button()

        with allure.step("Заполняем вторую страницу формы заказа минимальными данными"):
            order_page.fill_second_order_page(
                delivery_date="2024-12-20",
                rental_period="сутки",
                color="black",
                comment=""
            )
            order_page.click_order_button()

        with allure.step("Подтверждаем заказ в модальном окне"):
            order_page.confirm_order()

        with allure.step("Проверяем успешное оформление заказа"):
            assert order_page.is_order_successful(), "Заказ не был успешно оформлен"