from pages.landing_page import LandingPage
import allure
import pytest


@allure.suite("Тесты вопросов на главной странице")
class TestLandingPage:
    # Константы с ожидаемыми ответами вынесены в класс теста
    ANSWERS = {
        0: 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        1: 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
        2: 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
        3: 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
        4: 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
        5: 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
        6: 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
        7: 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    }
    
    @pytest.mark.parametrize("question_num, expected_answer", ANSWERS.items())
    @allure.title("Тест вопроса №{question_num}")
    def test_landing_page_questions(self, driver, question_num, expected_answer):
        with allure.step("Открываем главную страницу Самоката"):
            landing_page = LandingPage(driver)
            landing_page.open_url()

        with allure.step("Прокручиваем страницу до раздела с вопросами"):
            landing_page.scroll_to_questions()

        with allure.step(f"Кликаем на вопрос №{question_num}"):
            landing_page.click_question(question_num)

        with allure.step("Ожидаем отображение ответа"):
            landing_page.wait_for_answer_displayed(question_num)

        with allure.step("Получаем текст ответа и проверяем его"):
            actual_answer = landing_page.get_answer_text(question_num)
            assert actual_answer == expected_answer, \
                f"Ожидался ответ: '{expected_answer}', но получен: '{actual_answer}'"