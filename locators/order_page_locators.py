from selenium.webdriver.common.by import By

class OrderPageLocators:

    # Форма Для кого самокат
    # Поле Имя
    NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")

    # Поле Фамилия
    SURNAME_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")

    # Поле Адрес
    ADDRESS_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")

    # Поле метро
    SUBWAY_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")
    
    # Метро с названием {Name}
    @staticmethod
    def SUBWAY_NAME(subway_name):
        return (By.XPATH, f"//div[text()='{subway_name}']")
    
    # Поле Телефон
    PHONE_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")

    # Кнопка Далее
    NEXT_BUTTON = (By.XPATH, "//button[contains(text(), 'Далее')]")


    # Форма Про аренду
    # Поле Когда привезти самокат
    DATE_FIELD = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    
    # Поле Срок аренды
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[@class='Dropdown-placeholder']")

    # Выпадающий список Сроки аренды
    RENTAL_PERIOD_LIST = (By.XPATH, "//div[@class='Dropdown-menu']")
    
    # Выбор в списке Период аренды
    @staticmethod
    def RENTAL_PERIOD(period):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown')]//div[normalize-space(.)='{period}']")
        
    # Цвет самоката
    @staticmethod
    def COLOUR_CHECKBOX(colour):
        return (By.ID, f"{colour}")
    
    # Поле Комментарий для курьера
    COMMENT_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Комментарий')]")
    
    # Кнопка "Заказать"
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Middle') and contains(text(), 'Заказать')]")

    
    # Форма подтверждения заказа
    # Кнопка "Да"
    YES_BUTTON = (By.XPATH, "//button[contains(text(), 'Да')]")

    # Окно с информацией о заказе
    STATUS_WINDOW = (By.XPATH, "//div[contains(text(),'Номер заказа')]")