from selenium.webdriver.common.by import By
from data import URL_MAIN_PAGE
from pages.base_page import BasePage
import allure

class MainPage(BasePage):

    HEADER_ORDER_BUTTON = (By.XPATH, './/div/button[@class="Button_Button__ra12g"]')
    HEADER_TEXT = (By.XPATH, './/div[@class="Home_Header__iJKdX"]')
    BOTTOM_ORDER_BUTTON = (By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step(f'Открыть {URL_MAIN_PAGE}')
    def open_main_page(self):
        self.navigate(URL_MAIN_PAGE)

    @allure.step('Выбрать пукет FAQ номер {num}')
    def click_faq(self, num):
        self.click_element(((By.ID, f'accordion__heading-{num}')))

    @allure.step('Получить текст ответа FAQ номер {num}')
    def get_faq_answer(self, num):
        return self.find_element((By.XPATH, f'.//div/div[@id="accordion__panel-{num}"]/p')).text

    @allure.step('Пролистать до FAQ номер {num}')
    def go_to_faq_element(self, num):
        self.go_to_element(((By.ID, f'accordion__heading-{num}')))

    @allure.step('Дождаться загрузки ответа FAQ номер {num}')
    def wait_for_faq_element(self, num):
        self.wait_for_element_visible((By.ID, f'accordion__heading-{num}'))

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


