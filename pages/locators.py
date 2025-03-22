from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, '[value="Add to basket"]')
    PRODUCT_NAME = (By.XPATH,'//div[@class="col-sm-6 product_main"]//h1')
    PRODUCT_IS_ADDED_TO_THE_BASKET_NAME_MESSAGE = (By.XPATH,'(//div[@class="alertinner "]//strong)[1]')
    PRODUCT_IS_ADDED_TO_THE_BASKET_PRICE_MESSAGE = (By.XPATH,'(//div[@class="alertinner "]//strong)[3]')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '[class="price_color"]')
