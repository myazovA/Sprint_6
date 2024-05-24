import allure
from pages.main_page import MainPage
import pytest

class TestMainPage:

    @pytest.mark.parametrize('num, answer',
                             [[0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'],
                              [1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'],
                              [2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'],
                              [3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'],
                              [4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
                              [5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'],
                              [6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
                              [7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.']])
    @allure.title('Проверка открытия вопроса FAQ номер {num}')
    def test_faq_click_answer_opens(self, driver, num, answer):
        main_page = MainPage(driver)
        main_page.open_main_page()
        main_page.go_to_faq_element(num)
        main_page.wait_for_faq_element(num)
        main_page.click_faq(num)
        assert main_page.get_faq_answer(num) == answer