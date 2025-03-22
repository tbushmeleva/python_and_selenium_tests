import selenium.webdriver
from selenium import webdriver
import time
from pages.main_page import MainPage
from pages.login_page import LoginPage

def test_login_link_should_be_correct(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url()

def test_login_form_should_be_visible(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()

def test_register_form_should_be_visible(browser):
    link = "http://selenium1py.pythonanywhere.com/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()