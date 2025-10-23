from pages.landing_page import LandingPage
from data import LandingAnswers
import allure
import pytest


@pytest.mark.parametrize("question_num, expected_answer", LandingAnswers.ANSWERS.items())
def test_landing_page(driver, question_num, expected_answer):
    landing_page = LandingPage(driver)
    landing_page.open_url()
    landing_page.scroll_to_questions()

    with allure.step(f"Проверяем вопрос {question_num}"):
        landing_page.click_on_question(question_num)
        answer_text = landing_page.get_answer_text(question_num)
        assert answer_text == expected_answer, f"Ответ для вопроса {question_num} не совпадает с ожидаемым"