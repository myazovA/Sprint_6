from pages.main_page import MainPage
from pages.order_page import OrderPage
import pytest
from data import URL_DZEN, URL_MAIN_PAGE

class TestOrderPage:

    @pytest.mark.parametrize('name, surname, adress, phone, comment', [['Артем', 'Мязов', 'Чкалова 111',
                                                                        '77777777777', '11']])
    def test_making_order_with_header_button_successful(self, driver, name, surname, adress, phone, comment):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.click_header_order_button()
        order_page = OrderPage(driver)

        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_adress(adress)
        order_page.choose_on_metro()
        order_page.set_phone(phone)
        order_page.click_continue_button()

        order_page.set_when()
        order_page.set_rent_period()
        order_page.set_color()
        order_page.set_comment(comment)
        order_page.click_order_button()

        order_page.click_accept_order()
        assert 'Заказ оформлен' in order_page.check_success_message()
        order_page.click_go_to_status_window()

        order_page.click_yandex_logo()
        order_page.switch_to_dzen_tab()
        order_page.wait_yandex_logo()
        assert URL_DZEN in driver.current_url

    @pytest.mark.parametrize('name, surname, adress, phone, comment', [['Денис', 'Пашков', 'Пушкина 222',
                                                                        '66666666666', '1337']])
    def test_making_order_with_bottom_button_successful(self, driver, name, surname, adress, phone, comment):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.go_to_bottom_order_button()
        main_page.click_bottom_order_button()
        order_page = OrderPage(driver)

        order_page.set_name(name)
        order_page.set_surname(surname)
        order_page.set_adress(adress)
        order_page.choose_on_metro()
        order_page.set_phone(phone)
        order_page.click_continue_button()

        order_page.set_when()
        order_page.set_rent_period()
        order_page.set_color()
        order_page.set_comment(comment)
        order_page.click_order_button()

        order_page.click_accept_order()
        assert 'Заказ оформлен' in order_page.check_success_message()
        order_page.click_go_to_status_window()

        order_page.click_samocat_logo()
        main_page.wait_for_main_page_loading()
        assert URL_MAIN_PAGE in driver.current_url