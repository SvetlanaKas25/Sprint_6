import allure
import pytest

from data import OrderData
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title("Проверка позитивного сценария заказа самоката: кнопка «{button_location}»")
    @pytest.mark.parametrize("button_location, data_key", [
        ("вверху страницы", "data_set1"),
        ("внизу страницы", "data_set2"),
    ])
    
    def test_order_buttons(self, driver, button_location, data_key):
        data = OrderData.data_sets[data_key]
        order_page = OrderPage(driver)

        if button_location == "вверху страницы":
            order_page.click_order_button_header()
        elif button_location == "внизу страницы":
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