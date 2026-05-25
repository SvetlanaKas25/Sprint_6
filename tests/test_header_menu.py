import allure

from pages.header_menu import HeaderMenuComponent
from data import URLs


class TestNavigation:

    @allure.title("Проверка перехода по логотипу Самоката")
    def test_samokat_logo_redirects_to_main(self, driver):
        
        header_menu = HeaderMenuComponent(driver)
        header_menu.change_page()
        header_menu.click_logo_scooter()
        
        expected_url = URLs.MAIN_PAGE
        actual_url = header_menu.url
        assert expected_url == actual_url, (f"Ожидался URL: {expected_url}, но получен: {actual_url}")

    @allure.title("Проверка открытия Дзена в новой вкладке по клику на логотип Яндекса")
    def test_yandex_logo_opens_dzen(self, driver):
        
        header_menu = HeaderMenuComponent(driver)
        header_menu.click_yandex_logo()
        
        new_url = header_menu.url
        
        assert URLs.DZEN_PAGE in new_url, (f"Ожидалось открытие Дзена (dzen.ru), но открыт URL: {new_url}")