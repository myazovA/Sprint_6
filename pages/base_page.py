from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self,  url: str):
        self.driver.get(url)

    def find_element(self, locator: tuple, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            print(f'Element with {locator} not found within {timeout} seconds')
            return None

    def click_element(self, locator: tuple, timeout: int = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.click()
        else:
            print(f'Failed to click on element with locator {locator}')

    def enter_text(self, locator: tuple, text: str, timeout: int = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.clear()
            element.send_keys(text)
        else:
            print(f'Failede to enter text in element with locator {locator}')

    def wait_for_element_visible(self, locator: tuple, timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))
        except TimeoutException:
            print(f'Element with {locator} not visible after {timeout} seconds')
            return None

    def element_is_present(self, locator: tuple, timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def go_to_element(self, locator: tuple):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_tab(self, tab: int):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[tab])