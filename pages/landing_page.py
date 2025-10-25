from selenium.webdriver.common.by import By
from .base_page import BasePage


class LandingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://qa-scooter.praktikum-services.ru/"
        self.order_button = (By.XPATH, "//button[@class='Button_Button__ra12g']")
        self.questions_section = (By.CLASS_NAME, "Home_FourPart__1uthg")
        self.question_locator = (By.ID, "accordion__heading-{}")
        self.answer_locator = (By.ID, "accordion__panel-{}")

    def open_url(self):
        super().open_url(self.url)

    def click_on_order_button(self):
        self.click_element(self.order_button)

    def scroll_to_questions(self):
        """Прокручивает страницу до раздела с вопросами"""
        questions_section = self.find_element(self.questions_section)
        self.driver.execute_script("arguments[0].scrollIntoView();", questions_section)

    def click_question(self, question_num):
        """Кликает на вопрос по номеру"""
        question_locator = (
            By.ID, 
            f"accordion__heading-{question_num}" if isinstance(question_num, int) else question_num
        )
        self.click_element(question_locator)

    def get_answer_text(self, question_num):
        """Получает текст ответа по номеру вопроса"""
        answer_locator = (
            By.ID,
            f"accordion__panel-{question_num}" if isinstance(question_num, int) else question_num
        )
        return self.get_element_text(answer_locator)

    def wait_for_answer_displayed(self, question_num):
        """Ожидает отображение ответа"""
        answer_locator = (
            By.ID,
            f"accordion__panel-{question_num}" if isinstance(question_num, int) else question_num
        )
        return self.wait_for_element_visible(answer_locator)