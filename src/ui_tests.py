import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

WAIT_TIME = 5


class PageObjects:
    def __init__(self, driver):
        self.driver = driver

    def search_input(self):
        return self.driver.find_element(by=By.NAME, value='search_query')

    def add_to_cart_button(self):
        return self.driver.find_element(by=By.XPATH,
                                        value='//*[@id="center_column"]/ul/li[1]/div/div[2]/div[2]/a[1]')

    def proceed_to_checkout(self):
        return self.driver.find_element(by=By.LINK_TEXT,
                                        value='Proceed to checkout')

    def remove_button(self):
        return self.driver.find_element(by=By.CLASS_NAME,
                                        value='cart_quantity_delete')

    def logo_button(self):
        return self.driver.find_element(by=By.XPATH,
                                        value='//*[@id="header_logo"]/a')

    def plus_button(self):
        return self.driver.find_element(by=By.XPATH,
                                        value='//*[@id="cart_quantity_up_2_7_0_0"]')

    def minus_button(self):
        return self.driver.find_element(by=By.XPATH,
                                        value='//*[@id="cart_quantity_down_2_7_0_0"]')

    def continue_shopping_button(self):
        return self.driver.find_element(by=By.XPATH,
                                        value='//*[@id="center_column"]/p[2]/a[2]')


class UITests:
    def __init__(self, driver, page_objects):
        self.driver = driver
        self.page_objects = page_objects
        self.test_search()

    def test_search(self):
        """Результаты поисковой выдачи"""
        search_input = self.page_objects.search_input()
        search_input.send_keys('blouse')
        search_input.send_keys(Keys.RETURN)

        time.sleep(WAIT_TIME)

        assert 'No results' not in self.driver.page_source

        search_input = self.page_objects.search_input()
        search_input.clear()

        search_input.send_keys('dress')
        search_input.send_keys(Keys.RETURN)

        time.sleep(WAIT_TIME)

        assert 'No results' not in self.driver.page_source

        print('Search test passed')
        self.test_add_to_cart()

    def test_add_to_cart(self):
        """Добавление в корзину"""
        add_to_cart_button = self.page_objects.add_to_cart_button()
        add_to_cart_button.click()

        time.sleep(WAIT_TIME)

        shopping_cart = self.page_objects.proceed_to_checkout()
        shopping_cart.click()

        time.sleep(WAIT_TIME)

        assert 'Shopping-cart summary' in self.driver.page_source
        assert 'Product' in self.driver.page_source
        assert 'Description' in self.driver.page_source
        assert 'Avail.' in self.driver.page_source
        assert 'Qty' in self.driver.page_source
        assert 'Total' in self.driver.page_source

        print('Add to cart test passed')
        self.test_delete_from_cart()

    def test_delete_from_cart(self):
        """Удаление из корзины"""
        remove_button = self.page_objects.remove_button()
        remove_button.click()

        time.sleep(WAIT_TIME)

        assert 'Shopping-cart summary' in self.driver.page_source
        assert 'Your shopping cart is empty.' in self.driver.page_source

        print('Del from cart test passed')
        self.test_return_after_deletion()

    def test_return_after_deletion(self):
        """Возвращение в магазин из пустой корзины"""
        continue_button = self.page_objects.logo_button()
        continue_button.click()

        time.sleep(WAIT_TIME)

        assert 'My Store' in self.driver.page_source
        assert 'Cart' in self.driver.page_source
        assert 'Search' in self.driver.page_source

        print('Return after deletion test passed')
        self.test_сhanging_quantity()

    def test_сhanging_quantity(self):
        """Изменение количества товара"""
        search_input = self.page_objects.search_input()
        search_input.send_keys('blouse')
        search_input.send_keys(Keys.RETURN)

        time.sleep(WAIT_TIME)

        add_to_cart_button = self.page_objects.add_to_cart_button()
        add_to_cart_button.click()

        time.sleep(WAIT_TIME)

        shopping_cart = self.page_objects.proceed_to_checkout()
        shopping_cart.click()

        time.sleep(WAIT_TIME)

        update_button = self.page_objects.plus_button()
        update_button.click()

        time.sleep(WAIT_TIME)

        assert '2 Products' in self.driver.page_source

        update_button = self.page_objects.minus_button()
        update_button.click()

        time.sleep(WAIT_TIME)

        assert '1 Product' in self.driver.page_source

        print('Update test passed')
        self.test_continue_shopping()

    def test_continue_shopping(self):
        """Продолжение покупок после добавления товара в корзину"""
        continue_shopping_button = self.page_objects.continue_shopping_button()
        continue_shopping_button.click()

        time.sleep(WAIT_TIME)

        assert 'My Store' in self.driver.page_source
        assert 'Cart' in self.driver.page_source
        assert 'Search' in self.driver.page_source

        print('Continue shopping test passed')
        self.final_success()

    def final_success(self):
        print('*************************')
        print('All tests passed')


if __name__ == '__main__':
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get('http://automationpractice.com/index.php')
    page_objects = PageObjects(driver)
    print('*************************')
    tests = UITests(driver, page_objects)
    driver.close()
