from .base_page import BasePage
from  .locators import ProductPageLocators
from  .locators import MainPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def click_add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET).click()

    def should_be_success_message_with_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IS_ADDED_TO_THE_BASKET_NAME_MESSAGE), \
            'Success message with product name is not presented'

    def should_be_success_message_with_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_IS_ADDED_TO_THE_BASKET_PRICE_MESSAGE), \
            'Success message with product price is not presented'

    def get_original_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_original_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def get_product_name_in_success_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_IS_ADDED_TO_THE_BASKET_NAME_MESSAGE).text

    def get_product_price_in_success_message(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_IS_ADDED_TO_THE_BASKET_PRICE_MESSAGE).text

    def add_product_to_the_basket_with_solve(self):
        self.get_original_product_name()
        self.get_original_product_price()
        self.click_add_to_cart()
        self.solve_quiz_and_get_code()
        self.should_be_success_message_with_product_name()
        self.get_product_name_in_success_message()
        self.should_be_success_message_with_price()
        self.get_product_price_in_success_message()
        assert self.get_original_product_name() == self.get_product_name_in_success_message(), 'Product names are different'
        assert self.get_original_product_price() == self.get_product_price_in_success_message(), 'Product prices are different'

    def add_product_to_the_basket(self):
        self.get_original_product_name()
        self.get_original_product_price()
        self.click_add_to_cart()
        self.should_be_success_message_with_product_name()
        self.get_product_name_in_success_message()
        self.should_be_success_message_with_price()
        self.get_product_price_in_success_message()
        assert self.get_original_product_name() == self.get_product_name_in_success_message(), 'Product names are different'
        assert self.get_original_product_price() == self.get_product_price_in_success_message(), 'Product prices are different'





