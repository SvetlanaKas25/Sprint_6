import allure

from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    
    @allure.step("Кликаем на Кнопку Заказать вверху главной страницы")
    def click_order_button_header(self):
        self.click_element(OrderPageLocators.ORDER_BUTTON_HEADER)
    
    @allure.step("Кликаем на Кнопку Заказать внизу главной страницы")
    def click_order_button_middle(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON_MIDDLE)
        self.click_element(OrderPageLocators.ORDER_BUTTON_MIDDLE)

    @allure.step("Выбираем станцию метро: {subway_name}")
    def choice_subway(self, subway_name):
        self.click_element(OrderPageLocators.SUBWAY_FIELD)
        self.scroll_to_element(OrderPageLocators.SUBWAY_NAME(subway_name))
        self.click_element(OrderPageLocators.SUBWAY_NAME(subway_name))

    @allure.step("Кликаем на Кнопку Далее")
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    
    @allure.step("Выбираем Период аренды: {period}")
    def choice_rental_period(self, period):
        self.click_element(OrderPageLocators.RENTAL_PERIOD_FIELD)
        self.wait_for_element(OrderPageLocators.RENTAL_PERIOD_LIST)
        self.scroll_to_element(OrderPageLocators.RENTAL_PERIOD(period))
        self.click_element(OrderPageLocators.RENTAL_PERIOD(period))
    
    @allure.step("Клик вне области попапа Календарь")
    def click_outside_calendar(self):
        self.click_by_offset()

    @allure.step("Кликаем на Заказать в Форме заказа")
    def click_make_order_button(self):
        self.click_element(OrderPageLocators.MAKE_ORDER_BUTTON)

    @allure.step("Выбор цвета самоката")
    def choose_colour(self, colour):
        self.click_element(OrderPageLocators.COLOUR_CHECKBOX(colour))
    
    @allure.step("Подтверждение заказа. Кликаем кнопку Да")
    def click_accept_order(self):
        self.wait_for_element(OrderPageLocators.YES_BUTTON, 10)
        self.click_element(OrderPageLocators.YES_BUTTON)
    
    @allure.step("Проверяем наличие окна с информацией о заказе")
    def check_order_status_window(self):
        return self.is_element_displayed(OrderPageLocators.STATUS_WINDOW)

    @allure.step("Заполняем форму Для кого самокат. Вводим Имя: {name}, Фамилия: {surname}, Адрес: {address},  Станцию метро: {subway_name}, Телефон: {phone}.")
    def fill_first_form(self, name, surname, address, subway_name, phone):
        self.accept_cookies()
        self.wait_for_element(OrderPageLocators.NAME_FIELD, 10)
        self.send_keys_to_element(OrderPageLocators.NAME_FIELD, name)
        self.send_keys_to_element(OrderPageLocators.SURNAME_FIELD, surname)
        self.send_keys_to_element(OrderPageLocators.ADDRESS_FIELD, address)
        self.choice_subway(subway_name)
        self.send_keys_to_element(OrderPageLocators.PHONE_FIELD, phone)
        self.click_next_button()

    @allure.step("Заполняем форму Про аренду. Вводим Дату, когда привезти самокат: {date}, выбираем период аренды: {period}, Цвет самоката: {colour},  Комментарий для курьера: {comment}.")
    def fill_second_form(self, date, period, colour, comment):
        self.wait_for_element(OrderPageLocators.DATE_FIELD, 10)
        self.send_keys_to_element(OrderPageLocators.DATE_FIELD, date)
        self.click_outside_calendar()
        self.choice_rental_period(period)
        self.choose_colour(colour)
        self.send_keys_to_element(OrderPageLocators.COMMENT_FIELD, comment)
        self.click_make_order_button()
        self.click_accept_order()