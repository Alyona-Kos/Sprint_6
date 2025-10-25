from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver, timeout=10):
        """
        Базовый класс для всех page objects.
        
        :param driver: экземпляр WebDriver
        :param timeout: время ожидания по умолчанию в секундах
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
        self.timeout = timeout

    def open_url(self, url):
        """
        Открывает указанный URL в браузере.
        
        :param url: URL для открытия
        """
        self.driver.get(url)

    def get_current_url(self):
        """
        Возвращает текущий URL страницы.
        
        :return: текущий URL
        """
        return self.driver.current_url

    def click_element(self, locator):
        """
        Кликает на элемент после ожидания его кликабельности.
        
        :param locator: кортеж (By, selector) для поиска элемента
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def find_element(self, locator):
        """
        Находит элемент после ожидания его присутствия в DOM.
        
        :param locator: кортеж (By, selector) для поиска элемента
        :return: найденный элемент
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        """
        Находит все элементы по локатору после ожидания присутствия хотя бы одного.
        
        :param locator: кортеж (By, selector) для поиска элементов
        :return: список найденных элементов
        """
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def wait_for_element_visible(self, locator):
        """
        Ожидает видимость элемента на странице.
        
        :param locator: кортеж (By, selector) для поиска элемента
        :return: видимый элемент
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_element_invisible(self, locator):
        """
        Ожидает исчезновение элемента со страницы.
        
        :param locator: кортеж (By, selector) для поиска элемента
        :return: True если элемент невидим, иначе исключение
        """
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def get_element_text(self, locator):
        """
        Возвращает текст элемента.
        
        :param locator: кортеж (By, selector) для поиска элемента
        :return: текст элемента
        """
        element = self.find_element(locator)
        return element.text

    def input_text(self, locator, text):
        """
        Вводит текст в поле ввода.
        
        :param locator: кортеж (By, selector) для поиска поля ввода
        :param text: текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def switch_to_window(self, window_index):
        """
        Переключается на окно по индексу.
        
        :param window_index: индекс окна (0 - первое, 1 - второе и т.д.)
        """
        handles = self.driver.window_handles
        if len(handles) > window_index:
            self.driver.switch_to.window(handles[window_index])

    def get_window_handles_count(self):
        """
        Возвращает количество открытых окон/вкладок.
        
        :return: количество окон
        """
        return len(self.driver.window_handles)

    def close_current_window(self):
        """
        Закрывает текущее окно и переключается на первое доступное.
        """
        self.driver.close()
        if self.driver.window_handles:
            self.driver.switch_to.window(self.driver.window_handles[0])

    def refresh_page(self):
        """
        Обновляет текущую страницу.
        """
        self.driver.refresh()

    def go_back(self):
        """
        Возвращается на предыдущую страницу.
        """
        self.driver.back()

    def go_forward(self):
        """
        Переходит на следующую страницу в истории.
        """
        self.driver.forward()

    def is_element_present(self, locator):
        """
        Проверяет наличие элемента на странице.
        
        :param locator: кортеж (By, selector) для поиска элемента
        :return: True если элемент присутствует, False если нет
        """
        try:
            self.find_element(locator)
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator):
        """
        Проверяет видимость элемента на странице.
        
        :param locator: кортеж (By, selector) для поиска элемента
        :return: True если элемент видим, False если нет
        """
        try:
            self.wait_for_element_visible(locator)
            return True
        except TimeoutException:
            return False

    def wait_for_url_contains(self, text):
        """
        Ожидает, что текущий URL содержит указанный текст.
        
        :param text: текст для проверки в URL
        """
        return self.wait.until(EC.url_contains(text))

    def wait_for_url_to_be(self, url):
        """
        Ожидает, что текущий URL будет точно соответствовать указанному.
        
        :param url: ожидаемый URL
        """
        return self.wait.until(EC.url_to_be(url))

    def take_screenshot(self, filename):
        """
        Делает скриншот текущей страницы.
        
        :param filename: имя файла для сохранения скриншота
        """
        self.driver.save_screenshot(filename)

    def execute_script(self, script, *args):
        """
        Выполняет JavaScript код на странице.
        
        :param script: JavaScript код для выполнения
        :param args: аргументы для скрипта
        :return: результат выполнения скрипта
        """
        return self.driver.execute_script(script, *args)