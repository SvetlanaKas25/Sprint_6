from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    
    #'Кликаем на вопрос номер {number}'
    def click_question(self, number):
        self.click_element(MainPageLocators.QUESTION_LOCATORS(number))

    #'Получаем текст ответа на вопрос {number}'
    def get_answer_text(self, number):
        self.accept_cookies()
        self.scroll_page_down()
        self.click_question(number)
        answer_text = self.get_text_from_element(MainPageLocators.ANSWER_LOCATORS(number))

        return answer_text