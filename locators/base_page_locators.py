from selenium.webdriver.common.by import By

class BasePageLocators:

   # Кнопка Принять куки
   COOKIE_BUTTON = (By.ID, "rcc-confirm-button") 

   # Кнопка Заказать вверху главной страницы
   ORDER_BUTTON_HEADER = (By.XPATH, ".//div[@class='Header_Nav__AGCXC']/button[@class='Button_Button__ra12g']")

   # Кнопка Заказать внизу главной страницы
   ORDER_BUTTON_MIDDLE = (By.XPATH, "//div[@class='Home_FinishButton__1_cWm']/button[contains(text(), 'Заказать')]")

   # Логотип Яндекс
   LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI") 

   # Логотип Самокат
   LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR") 