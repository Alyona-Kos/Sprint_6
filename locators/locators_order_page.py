from selenium.webdriver.common.by import By
from data import Person

class Oder_page_locators:

    INPUT_NAME = (By.CSS_SELECTOR, "input[placeholder='* Имя']")
    INPUT_SURNAME = (By.CSS_SELECTOR, "input[placeholder='* Фамилия']")
    INPUT_ADRESS = (By.CSS_SELECTOR, "input[placeholder='* Адрес: куда привезти заказ']")
    Metro_one = (By.CSS_SELECTOR, "input[placeholder='* Станция метро']")
    INPUT_PHONE_NUMBER = (By.CSS_SELECTOR, "input[placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, '//button[text()="Далее"]')
    INPUT_DATE = (By.CSS_SELECTOR, "input[placeholder='* Когда привезти самокат']")
    SELECTED_DATE = (By.XPATH,
                     f"//div[@class='react-datepicker__day react-datepicker__day--00{Person.random_date} react-datepicker__day--selected']")
    RENTAL_PERIOD = [By.CSS_SELECTOR, 'div[class="Dropdown-root"]']
    Dropdown_RENTAL_PERIOD = (By.XPATH, f'//div[text()="{Person.random_period}"]')
    CHECKBOX_COLOUR = (By.XPATH, f'//input[@id="{Person.random_color}"]')
    INPUT_COMMENT = (By.CSS_SELECTOR, "input.Input_Input__1iN_Z.Input_Responsible__1jDKN[placeholder='Комментарий для курьера']")
    CREATE_ORDER = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']
    BUTTON_CONFIRM_ORDER_YES = [By.XPATH, '//button[text()="Да"]']
    
    # Добавленные локаторы для проверки успешного заказа
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    ORDER_NUMBER = (By.XPATH, "//div[contains(@class, 'Order_Text')]")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")