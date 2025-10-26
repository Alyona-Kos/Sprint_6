from selenium.webdriver.common.by import By
from .base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        """
        Page Object для страницы оформления заказа.
        """
        super().__init__(driver)
        self.url = "https://qa-scooter.praktikum-services.ru/"
        
        # Локаторы для кнопок заказа
        self.header_order_button = (By.XPATH, "//button[@class='Button_Button__ra12g']")
        self.page_order_button = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button")
        
        # Локатор для cookie баннера и кнопки принятия
        self.cookie_banner = (By.CLASS_NAME, "App_CookieConsent__1yUIN")
        self.cookie_accept_button = (By.ID, "rcc-confirm-button")
        
        # Локаторы для формы заказа (первая страница)
        self.name_input = (By.XPATH, "//input[@placeholder='* Имя']")
        self.surname_input = (By.XPATH, "//input[@placeholder='* Фамилия']")
        self.address_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
        self.metro_input = (By.XPATH, "//input[@placeholder='* Станция метро']")
        self.metro_dropdown_option = (By.XPATH, "//div[@class='select-search__select']//button")
        self.phone_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
        self.next_button = (By.XPATH, "//button[text()='Далее']")
        
        # Локаторы для формы заказа (вторая страница)
        self.delivery_date_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
        self.rental_period_dropdown = (By.CLASS_NAME, "Dropdown-placeholder")
        self.rental_period_option = (By.XPATH, "//div[@class='Dropdown-option']")
        self.color_black_checkbox = (By.ID, "black")
        self.color_grey_checkbox = (By.ID, "grey")
        self.comment_input = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
        self.order_button = (By.XPATH, "//button[contains(@class, 'Button_Middle') and text()='Заказать']")
        
        # Локаторы для подтверждения заказа
        self.confirm_order_button = (By.XPATH, "//button[text()='Да']")
        self.order_success_message = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
        
        # Локатор для заголовка страницы (чтобы кликнуть и закрыть календарь)
        self.page_header = (By.CLASS_NAME, "Order_Header__BZXOb")

    def open_url(self):
        """Открывает URL страницы заказа и закрывает cookie баннер"""
        super().open_url(self.url)
        self.accept_cookies()

    def accept_cookies(self):
        """Закрывает cookie баннер, если он присутствует"""
        if self.is_element_visible(self.cookie_banner):
            self.click_element(self.cookie_accept_button)

    def click_header_order_button(self):
        """Кликает на кнопку заказа в хедере"""
        self.accept_cookies()  # На всякий случай закрываем cookies
        self.click_element(self.header_order_button)

    def click_page_order_button(self):
        """Кликает на кнопку заказа на странице"""
        self.accept_cookies()  # На всякий случай закрываем cookies
        self.click_element(self.page_order_button)

    def fill_first_order_page(self, name, surname, address, metro_station, phone):
        """
        Заполняет первую страницу формы заказа.
        """
        self.input_text(self.name_input, name)
        self.input_text(self.surname_input, surname)
        self.input_text(self.address_input, address)
        self.select_metro_station(metro_station)
        self.input_text(self.phone_input, phone)

    def select_metro_station(self, station_name):
        """
        Выбирает станцию метро из выпадающего списка.
        """
        # Кликаем на поле ввода метро
        self.click_element(self.metro_input)
        
        # Ждем появления выпадающего списка
        self.wait_for_element_visible(self.metro_dropdown_option)
        
        # Ищем и кликаем на нужную станцию
        station_locator = (By.XPATH, f"//button/div[text()='{station_name}']")
        self.click_element(station_locator)

    def click_next_button(self):
        """Кликает на кнопку 'Далее' для перехода ко второй странице"""
        self.click_element(self.next_button)

    def fill_second_order_page(self, delivery_date, rental_period, color, comment):
        """
        Заполняет вторую страницу формы заказа.
        """
        self.input_text(self.delivery_date_input, delivery_date)
        self.close_datepicker()  # Закрываем календарь перед выбором срока аренды
        self.select_rental_period(rental_period)
        self.select_scooter_color(color)
        if comment:
            self.input_text(self.comment_input, comment)

    def close_datepicker(self):
        """Закрывает календарь, кликая на заголовок страницы"""
        self.click_element(self.page_header)

    def select_rental_period(self, period):
        """
        Выбирает период аренды из выпадающего списка.
        """
        self.click_element(self.rental_period_dropdown)
        period_locator = (By.XPATH, f"//div[@class='Dropdown-option' and text()='{period}']")
        self.click_element(period_locator)

    def select_scooter_color(self, color):
        """
        Выбирает цвет самоката.
        """
        if color.lower() == 'black':
            self.click_element(self.color_black_checkbox)
        elif color.lower() == 'grey':
            self.click_element(self.color_grey_checkbox)

    def click_order_button(self):
        """Кликает на кнопку 'Заказать'"""
        self.click_element(self.order_button)

    def confirm_order(self):
        """Подтверждает заказ в модальном окне"""
        self.click_element(self.confirm_order_button)

    def is_order_successful(self):
        """Проверяет, успешно ли оформлен заказ"""
        return self.is_element_visible(self.order_success_message)

    def get_success_message(self):
        """Получает сообщение об успешном оформлении заказа"""
        return self.get_element_text(self.order_success_message)

    def make_complete_order(self, order_data):
        """
        Выполняет полный процесс оформления заказа.
        """
        # Первая страница
        self.fill_first_order_page(
            order_data['name'],
            order_data['surname'],
            order_data['address'],
            order_data['metro_station'],
            order_data['phone']
        )
        self.click_next_button()
        
        # Вторая страница
        self.fill_second_order_page(
            order_data['delivery_date'],
            order_data['rental_period'],
            order_data['color'],
            order_data['comment']
        )
        self.click_order_button()
        
        # Подтверждение
        self.confirm_order()