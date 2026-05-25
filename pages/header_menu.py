import allure

from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage
from data import URLs

class HeaderMenuComponent(BasePage):
    
    #'Клик по логотипу Самоката'
    def click_logo_scooter(self):
        self.accept_cookies()
        self.click_element(BasePageLocators.LOGO_SCOOTER)
        return self

    #'Переход по логотипу Яндекса'
    def click_yandex_logo(self):
        self.accept_cookies()
        initial_tabs = len(self.driver.window_handles)
        self.click_element(BasePageLocators.LOGO_YANDEX)
        self.wait_for_new_tab(initial_tabs)
        self.switch_window(1) 
        self.wait_url_until_not_about_blank()

    @allure.step('Переход на страницу Формы заказа')
    def change_page(self):
        self.driver.get(URLs.ORDER_PAGE)
    