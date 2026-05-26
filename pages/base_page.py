import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.base_page_locators import BasePageLocators

TIMEOUT = 10

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # Возвращает текущий URL страницы
    @property
    def url(self):
        return self.driver.current_url
    
    @allure.step("Ожидание элемента {locator} и взаимодействие с ним")
    def wait_for_element(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    
    @allure.step("Ожидать появления новой вкладки")
    def wait_for_new_tab(self, initial_tabs_count, timeout=15):
    #"""Ждёт, пока количество вкладок станет больше initial_tabs_count."""
        return WebDriverWait(self.driver, timeout).until(
        lambda driver: len(driver.window_handles) > initial_tabs_count
    )

    @allure.step("Проверить отображение элемента {locator}")
    def is_element_displayed(self, locator):
        try:
            return self.wait_for_element(locator).is_displayed()
        except:
            return False
    
    @allure.step("Кликнуть по элементу {locator}")
    def click_element(self, locator):
        element = self.wait_for_element(locator)
        element.click()

    @allure.step('Принимаем куки')
    def accept_cookies(self):
        self.click_element(BasePageLocators.COOKIE_BUTTON)
       
    @allure.step("Прокрутить до элемента {locator}")
    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Скроллим страницу до самого низа')
    def scroll_page_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Отправить текст '{keys}' в элемент {locator}")
    def send_keys_to_element(self, locator, keys):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(keys)

    @allure.step("Получить текст из элемента {locator}")
    def get_text_from_element(self, locator):
        element = self.wait_for_element(locator)
        return element.text

    @allure.step('Переключиться на вкладку браузера')
    def switch_window(self, window_number: int = 1):
        return self.driver.switch_to.window(self.driver.window_handles[window_number])
    
    @allure.step('Ожидаем пока текущий URL вкладки перестанет быть равным about:blank')
    def wait_url_until_not_about_blank(self, time=10):
        return WebDriverWait(self.driver, time).until_not(EC.url_to_be('about:blank'))
    
    @allure.step('Определяем текущее количество открытых вкладок.')
    def get_current_tab_count(self):
        return len(self.driver.window_handles)