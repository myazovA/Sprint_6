from selenium.webdriver.common.by import By
from data import URL_MAIN_PAGE
from pages.base_page import BasePage
import allure

class MainPage(BasePage):

    HEADER_ORDER_BUTTON = (By.XPATH, './/div/button[@class="Button_Button__ra12g"]')
    HEADER_TEXT = (By.XPATH, './/div[@class="Home_Header__iJKdX"]')
    BOTTOM_ORDER_BUTTON = (By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button')
    FAQ = (By.ID, 'accordion__heading-')
    FAQ_ANSWER = (By.XPATH, f'.//div/div[@id="accordion__panel-')
    DZEN_YANDEX_LOGO = (By.XPATH, './/img[@src="https://avatars.mds.yandex.net/get-direct-picture/117537/Q6ulef2SQr_K6plpIwCn5A/orig"]')
    SAMOCAT_LOGO = (By.XPATH, './/img[@src="/assets/scooter.svg"]')
    YANDEX_LOGO = (By.XPATH, './/img[@src="/assets/ya.svg"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step(f'Открыть {URL_MAIN_PAGE}')
    def open_main_page(self):
        self.navigate(URL_MAIN_PAGE)

    @allure.step('Выбрать пункт FAQ номер {num}')
    def click_faq(self, num):
        self.click_element((self.FAQ[0], self.FAQ[1]+str(num)))

    @allure.step('Получить текст ответа FAQ номер {num}')
    def get_faq_answer(self, num):
        return self.find_element((self.FAQ_ANSWER[0], self.FAQ_ANSWER[1]+f'{num}"]/p')).text

    @allure.step('Пролистать до FAQ номер {num}')
    def go_to_faq_element(self, num):
        self.go_to_element((self.FAQ[0], self.FAQ[1]+str(num)))

    @allure.step('Дождаться загрузки ответа FAQ номер {num}')
    def wait_for_faq_element(self, num):
        self.wait_for_element_visible((self.FAQ[0], self.FAQ[1]+str(num)))

    @allure.step('Нажать на кнопку "Заказть" сверху страницы')
    def click_header_order_button(self):
        self.click_element(self.HEADER_ORDER_BUTTON)

    @allure.step('Дождаться загрузки заголовка страницы')
    def wait_for_main_page_loading(self):
        self.wait_for_element_visible(self.HEADER_TEXT)

    @allure.step('Пролистать до кнопки "Заказть" снизу страницы')
    def go_to_bottom_order_button(self):
        self.go_to_element(self.BOTTOM_ORDER_BUTTON)

    @allure.step('Нажать на кнопку "Заказть" снизу страницы')
    def click_bottom_order_button(self):
        self.click_element(self.BOTTOM_ORDER_BUTTON)

    @allure.step('Нажать на лого Самоката')
    def click_samocat_logo(self):
        self.click_element(self.SAMOCAT_LOGO)

    @allure.step('Нажать на лого Яндекса')
    def click_yandex_logo(self):
        self.click_element(self.YANDEX_LOGO)

    @allure.step('Перейти на вкладку с Дзеном')
    def switch_to_dzen_tab(self):
        self.switch_tab(1)

    @allure.step('Подождать загрузку лого Яндекса на страницу Дзена')
    def wait_yandex_logo(self):
        self.wait_for_element_visible(self.DZEN_YANDEX_LOGO)

    @allure.step('Получить текущий url')
    def get_url(self):
        get_url = self.driver.current_url
        return get_url