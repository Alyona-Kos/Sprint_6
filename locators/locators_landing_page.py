from selenium.webdriver.common.by import By

class TestLocator_landing_questions:

    Button_questions_about_important = By.ID, "accordion__heading-{}"
    QUESTION_8 = By.ID, 'accordion__heading-7'

class TestLocator_landing_answer:

    Text_answer_question_about_important = By.ID, "accordion__panel-{}"

class Testlocators:
    Button_make_order_header = By.XPATH, '//div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]'
    Button_make_order_landing = By.XPATH, '//div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]'
    LOGO_SCOOTER = (By.CSS_SELECTOR, ".Header_LogoScooter__3lsAR img")
    YA_LOGO = (By.CSS_SELECTOR, "img[src='/assets/ya.svg']")