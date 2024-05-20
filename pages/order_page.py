from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class OrderPage:

    NAME_FIELD = By.XPATH, './/div/input[@placeholder="* Имя"]'
    SURNAME_FIELD = By.XPATH, './/div/input[@placeholder="* Фамилия"]'
    ADRESS_FIELD = By.XPATH, './/div/input[@placeholder="* Адрес: куда привезти заказ"]'
    METRO_FIELD = By.XPATH, './/div/input[@placeholder="* Станция метро"]'
    METRO_SELECT = By.XPATH, './/ul/li[@data-value="1"]/button'
    PHONE_FIELD = By.XPATH, './/div/input[@placeholder="* Телефон: на него позвонит курьер"]'
    CONTINUE_BUTTON = By.XPATH, './/div/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    WHEN_FIELD = By.XPATH, './/div/input[@placeholder="* Когда привезти самокат"]'
    WHEN_FIELD_SELECT = By.XPATH, './/div[contains(@class,"react-datepicker__day--today")]'
    RENT_PERIOD_FIELD = By.XPATH, './/div[@class="Dropdown-placeholder"]'
    RENT_PERIOD_LIST = By.XPATH, './/div[contains(text(), "сутки")]'
    BLACK_COLOR_CHECKBOX = By.XPATH, '//*[@id="black"]'
    COMMENT_FIELD = By.XPATH, './/div/input[@placeholder="Комментарий для курьера"]'
    ORDER_BUTTON = By.XPATH, './/button[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    SAMOCAT_LOGO = By.XPATH, './/img[@src="/assets/scooter.svg"]'
    YANDEX_LOGO = By.XPATH, './/img[@src="/assets/ya.svg"]'
    ACCEPT_BUTTON = By.XPATH, './/button[contains(text(), "Да")]'
    SUCCESS_MESSAGE = By.XPATH, './/div[contains(text(), "Заказ оформлен")]'
    CHECK_STATUS_BUTTON = By.XPATH, './/button[contains(text(), "Посмотреть статус")]'
    DZEN_YANDEX_LOGO = By.XPATH, './/img[@src="https://avatars.mds.yandex.net/get-direct-picture/117537/Q6ulef2SQr_K6plpIwCn5A/orig"]'

    def __init__(self, driver):
        self.driver = driver

    def set_name(self, name):
        self.driver.find_element(*self.NAME_FIELD).send_keys(name)

    def set_surname(self, surname):
        self.driver.find_element(*self.SURNAME_FIELD).send_keys(surname)

    def set_adress(self, adress):
        self.driver.find_element(*self.ADRESS_FIELD).send_keys(adress)

    def choose_on_metro(self):
        self.driver.find_element(*self.METRO_FIELD).click()
        self.driver.find_element(*self.METRO_SELECT).click()

    def set_phone(self, phone):
        self.driver.find_element(*self.PHONE_FIELD).send_keys(phone)

    def click_continue_button(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()

    def set_when(self):
        self.driver.find_element(*self.WHEN_FIELD).click()
        self.driver.find_element(*self.WHEN_FIELD_SELECT).click()


    def set_rent_period(self):
        self.driver.find_element(*self.RENT_PERIOD_FIELD).click()
        self.driver.find_element(*self.RENT_PERIOD_LIST).click()

    def set_color(self):
        self.driver.find_element(*self.BLACK_COLOR_CHECKBOX).click()

    def set_comment(self, comment):
        self.driver.find_element(*self.COMMENT_FIELD).send_keys(comment)

    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def click_accept_order(self):
        self.driver.find_element(*self.ACCEPT_BUTTON).click()

    def check_success_message(self):
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text

    def click_go_to_status_window(self):
        self.driver.find_element(*self.CHECK_STATUS_BUTTON).click()

    def click_samocat_logo(self):
        self.driver.find_element(*self.SAMOCAT_LOGO).click()

    def click_yandex_logo(self):
        self.driver.find_element(*self.YANDEX_LOGO).click()

    def switch_to_dzen_tab(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])

    def switch_to_order_tab(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])

    def current_url(self):
        return self.driver.current_url

    def wait_yandex_logo(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((self.DZEN_YANDEX_LOGO)))


