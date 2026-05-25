from selenium.webdriver.common.by import By

class MainPageLocators:

    # Вопросы 
    @staticmethod
    def QUESTION_LOCATORS(number):
        return (By.XPATH, f"//div[@id='accordion__heading-{number}']")
    

    # Ответы 
    @staticmethod
    def ANSWER_LOCATORS(number):
        return (By.XPATH, f"//div[@id='accordion__panel-{number}']")
    
    