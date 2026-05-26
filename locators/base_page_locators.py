from selenium.webdriver.common.by import By

class BasePageLocators:

   # Кнопка Принять куки
   COOKIE_BUTTON = (By.ID, "rcc-confirm-button") 

   # Логотип Яндекс
   LOGO_YANDEX = (By.CLASS_NAME, "Header_LogoYandex__3TSOI") 

   # Логотип Самокат
   LOGO_SCOOTER = (By.CLASS_NAME, "Header_LogoScooter__3lsAR") 