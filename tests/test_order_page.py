import allure

from data import OrderData
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title("Проверка позитивного сценария Заказа самоката через кнопку «Заказать» вверху страницы")
    
    def test_order_button_header(self, driver):
        
        data = OrderData.data_sets["data_set1"]
        order_page = OrderPage(driver)
        
        order_page.click_order_button_header()
        order_page.fill_first_form(
            data["name"],
            data["surname"],
            data["address"],
            data["subway_name"],
            data["phone"]
        )
        order_page.fill_second_form(
            data["date"],
            data["period"],
            data["colour"],
            data["comment"]
        )
                
        assert order_page.check_order_status_window(), ("Окно с информацией о заказе не появилось")

    @allure.title("Проверка позитивного сценария Заказа самоката через кнопку «Заказать» внизу страницы")
    
    def test_order_button_middle(self, driver):
        
        data = OrderData.data_sets["data_set2"]
        order_page = OrderPage(driver)
        
        order_page.click_order_button_middle()
        order_page.fill_first_form(
            data["name"],
            data["surname"],
            data["address"],
            data["subway_name"],
            data["phone"]
        )
        order_page.fill_second_form(
            data["date"],
            data["period"],
            data["colour"],
            data["comment"]
        )
                
        assert order_page.check_order_status_window(), ("Окно с информацией о заказе не появилось")