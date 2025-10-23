from pages.base_page import BasePage
from locators.locators_landing_page import TestLocator_landing_questions
from locators.locators_landing_page import TestLocator_landing_answer
from locators.locators_landing_page import Testlocators
import allure

class LandingPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Прокрутить страницу до блока вопросов')
    def scroll_to_questions(self):
        self.scroll_to_element(TestLocator_landing_questions.QUESTION_8)

    @allure.step('Кликнуть по вопросу')
    def click_on_question(self, question_num):
        formatted_questions_locator = self.format_locator(TestLocator_landing_questions.Button_questions_about_important, question_num)
        self.click_on_element(formatted_questions_locator)

    @allure.step('Получить текст ответа')
    def get_answer_text(self, question_num):
        formatted_text_answer_locator = self.format_locator(TestLocator_landing_answer.Text_answer_question_about_important, question_num)
        return self.get_text_from_element(formatted_text_answer_locator)

    @allure.step('Клик по кнопке Заказать вверху лэндинга')
    def click_on_order_button(self):  # Измените имя метода
        self.click_on_element(Testlocators.Button_make_order_header)