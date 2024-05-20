from selenium.webdriver.common.by import By
from data import URL_MAIN_PAGE
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class MainPage:

    HEADER_ORDER_BUTTON = By.XPATH, './/div/button[@class="Button_Button__ra12g"]'
    HEADER_TEXT = By.XPATH, './/div[@class="Home_Header__iJKdX"]'
    BOTTOM_ORDER_BUTTON = By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button'

    def __init__(self, driver):
        self.driver = driver

    def open_main_page(self):
        self.driver.get(URL_MAIN_PAGE)

    def click_faq(self, num):
        self.driver.find_element(By.ID, f'accordion__heading-{num}').click()

    def get_faq_answer(self, num):
        return self.driver.find_element(By.XPATH, f'.//div/div[@id="accordion__panel-{num}"]/p').text

    def go_to_faq_element(self, num):
        element = self.driver.find_element(By.ID, f'accordion__heading-{num}')
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_faq_element(self, num):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, f'accordion__heading-{num}')))

    def click_header_order_button(self):
        self.driver.find_element(*self.HEADER_ORDER_BUTTON).click()

    def wait_for_main_page_loading(self):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((self.HEADER_TEXT)))

    def current_url(self):
        return self.driver.current_url

    def go_to_bottom_order_button(self):
        element = self.driver.find_element(*self.BOTTOM_ORDER_BUTTON)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_bottom_order_button(self):
        self.driver.find_element(*self.BOTTOM_ORDER_BUTTON).click()


