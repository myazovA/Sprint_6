from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage

class OrderPage(BasePage):

    NAME_FIELD = (By.XPATH, './/div/input[@placeholder="* Имя"]')
    SURNAME_FIELD = (By.XPATH, './/div/input[@placeholder="* Фамилия"]')
    ADRESS_FIELD = (By.XPATH, './/div/input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.XPATH, './/div/input[@placeholder="* Станция метро"]')
    METRO_SELECT = (By.XPATH, './/ul/li[@data-value="1"]/button')
    PHONE_FIELD = (By.XPATH, './/div/input[@placeholder="* Телефон: на него позвонит курьер"]')
    CONTINUE_BUTTON = (By.XPATH, './/div/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    WHEN_FIELD = (By.XPATH, './/div/input[@placeholder="* Когда привезти самокат"]')
    WHEN_FIELD_SELECT = (By.XPATH, './/div[contains(@class,"react-datepicker__day--today")]')
    RENT_PERIOD_FIELD = (By.XPATH, './/div[@class="Dropdown-placeholder"]')
    RENT_PERIOD_LIST = (By.XPATH, './/div[contains(text(), "сутки")]')
    BLACK_COLOR_CHECKBOX = (By.XPATH, '//*[@id="black"]')
    COMMENT_FIELD = (By.XPATH, './/div/input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    ACCEPT_BUTTON = (By.XPATH, './/button[contains(text(), "Да")]')
    SUCCESS_MESSAGE = (By.XPATH, './/div[contains(text(), "Заказ оформлен")]')
    CHECK_STATUS_BUTTON = (By.XPATH, './/button[contains(text(), "Посмотреть статус")]')


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Ввести значение поля Имя')
    def set_name(self, name):
        self.enter_text(self.NAME_FIELD, name)

    @allure.step('Ввести значение поля Фамилия')
    def set_surname(self, surname):
        self.enter_text(self.SURNAME_FIELD, surname)

    @allure.step('Ввести значение поля Адрес')
    def set_adress(self, adress):
        self.enter_text(self.ADRESS_FIELD, adress)

    @allure.step('Выбрать значение поля Метро')
    def choose_on_metro(self):
        self.click_element(self.METRO_FIELD)
        self.click_element(self.METRO_SELECT)

    @allure.step('Ввести значение поля Телефон')
    def set_phone(self, phone):
        self.enter_text(self.PHONE_FIELD, phone)

    @allure.step('Нажать кнопку Далее')
    def click_continue_button(self):
        self.click_element(self.CONTINUE_BUTTON)

    @allure.step('Ввести значение поля Когда привезти')
    def set_when(self):
        self.click_element(self.WHEN_FIELD)
        self.click_element(self.WHEN_FIELD_SELECT)

    @allure.step('Ввести значение поля Период аренды')
    def set_rent_period(self):
        self.click_element(self.RENT_PERIOD_FIELD)
        self.click_element(self.RENT_PERIOD_LIST)

    @allure.step('Ввести значение поля Цвет')
    def set_color(self):
        self.click_element(self.BLACK_COLOR_CHECKBOX)

    @allure.step('Ввести значение поля Комментарий')
    def set_comment(self, comment):
        self.enter_text(self.COMMENT_FIELD, comment)

    @allure.step('Нажать кнопку Заказть')
    def click_order_button(self):
        self.click_element(self.ORDER_BUTTON)

    @allure.step('Нажать кнопку подтверждения заказа')
    def click_accept_order(self):
        self.click_element(self.ACCEPT_BUTTON)

    @allure.step('Проверить сообщение об успешном заказе')
    def check_success_message(self):
        return self.find_element(self.SUCCESS_MESSAGE).text

    @allure.step('Нажать кнопку Посмотреть статус')
    def click_go_to_status_window(self):
        self.click_element(self.CHECK_STATUS_BUTTON)




