from pages.base_page import BasePage
from locators.locators_landing_page import Testlocators
from locators.locators_order_page import Oder_page_locators
from data import Person
import allure
import random
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    @allure.step('Открываем форму оформления заказа кликоп по "Заказать" в шапке лэндинга')
    def click_on_element_make_order_header(self, button: object) -> object:
        if button == 'header_button':
            self.click_on_element(Testlocators.Button_make_order_header)
        elif button == 'page_button':
            self.scroll_to_element(Testlocators.Button_make_order_landing)
            self.click_on_element(Testlocators.Button_make_order_landing)


    @allure.step('Убедиться, что страница заказа загрузилась (проверяем видимость поля Имя)')
    def name_field_find_element_with_wait(self):
        self.find_element_with_wait(Oder_page_locators.INPUT_NAME).is_enabled()

    @allure.step('Заполняем поля "Имя"')
    def fill_name_field(self):
        self.find_element_with_wait(Oder_page_locators.INPUT_NAME).send_keys(Person.random_name)

    @allure.step('Заполняем поля "Фамилия"')
    def fill_surname_field(self):
        self.find_element_with_wait(Oder_page_locators.INPUT_SURNAME).send_keys(Person.random_surname)

    @allure.step('Заполняем поля "Адрес"')
    def fill_adress_field(self):
        person = Person()  # Создаем объект Person
        person.fill_adress_field()  # Вызываем функцию для генерации адреса
        self.find_element_with_wait(Oder_page_locators.INPUT_ADRESS).send_keys(person.adress)

    @allure.step('В форме создания заказа выбираем станцию метро')
    def select_metro(self):
        self.click_on_element(Oder_page_locators.Metro_one)
        self.find_element_with_wait(Oder_page_locators.Metro_one).send_keys(Person.random_station)
        self.find_element_with_wait(Oder_page_locators.Metro_one).send_keys(Keys.DOWN, Keys.ENTER)
        # return self

    @allure.step('Заполняем поле Телефон')
    def fill_phone_field(self):
        self.find_element_with_wait(Oder_page_locators.INPUT_PHONE_NUMBER).send_keys(Person.random_phone_number)

    @allure.step('Кликом по Далее переходим на вторую страницу формы заказа')
    def click_on_element_next(self):
        self.click_on_element(Oder_page_locators.BUTTON_NEXT)

    @allure.step('Выбираем дату заказа')
    def pick_date(self):
        self.find_element_with_wait(Oder_page_locators.INPUT_DATE).send_keys(Person.random_date)
        self.find_element_with_wait(Oder_page_locators.INPUT_DATE).send_keys(Keys.ENTER)

    @allure.step('Выбираем срок аренды')
    def pick_rental_period(self):
        self.click_on_element(Oder_page_locators.RENTAL_PERIOD)
        self.find_element_with_wait(Oder_page_locators.Dropdown_RENTAL_PERIOD)
        self.click_on_element(Oder_page_locators.Dropdown_RENTAL_PERIOD)

    @allure.step('Выбираем цвет самоката (черный)')
    def click_on_element_color_black(self):
        self.click_on_element(Oder_page_locators.CHECKBOX_COLOUR)

    @allure.step('Заполняем поле Комментарий')
    def fill_comment_field(self):
        person = Person()
        person.fill_comment_field()
        self.find_element_with_wait(Oder_page_locators.INPUT_COMMENT).send_keys(person.comment)

    @allure.step('Клик по кнопке Заказать в конце формы заказа')
    def click_on_element_create_order(self):
        self.click_on_element(Oder_page_locators.CREATE_ORDER)

    @allure.step('Клик по кнопке Да - подтверждение заказа')
    def click_on_element_confirm_order_yes(self):
       self.click_on_element(Oder_page_locators.BUTTON_CONFIRM_ORDER_YES)