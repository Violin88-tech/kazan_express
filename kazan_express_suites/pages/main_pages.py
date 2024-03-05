from selene import browser, be, have
from kazan_express_suites.data.data_cards import Texts

import allure
import time


class MainPage:
    def __init__(self):
        self.search_input = browser.element('.default-input') #сделала
        self.basket = browser.element('#cart-button') #сделала

    def open_url(self):
        with allure.step("Открываем главную страницу"):
            browser.open('/')
        time.sleep(2)

    def search(self, value):
        with allure.step(f"Ищем товар {value}"):
            self.search_input.type(value).press_enter()

    def result_by_name(self, card_name, brand_name, card_price):
        with allure.step(f"Отображается товар с наименованием {card_name}"):
            browser.element().should(
                have.attribute( f'{card_name} {brand_name}'))

    def result_by_article(self, card_article):
        with allure.step(f"Отображается товар с артикулом {card_article}"):
            browser.element().should(have.text(card_article))

    def no_result(self):
        with allure.step(f"Отображается строка {Texts.nothing_found}"):
            browser.element().should(have.text(Texts.nothing_found))

    def add_item_to_cart(self, card_article):
        with allure.step("Наводим курсор на товар"):
            browser.element().hover()
        with allure.step("Нажимаем 'Добавить в корзину'"):
            browser.element().click()
        with allure.step("Счётчик корзины увеличился"):
            browser.element().should(be.visible)

    def open_basket(self):
        with allure.step("Нажимаем 'Корзина'"):
            self.basket.click()

    def check_cart(self, card_name, brand_name):
        self.open_basket()
        with allure.step(f"В корзине отображается товар с наименованием {card_name} {brand_name}"):
            browser.all('').should(have.texts(card_name, brand_name))

    def remove_from_cart(self):
        self.open_basket()
        with allure.step("Удаляем товар"):
            browser.element('').click()
        with allure.step():
            browser.element().should(have.text(Texts.empty_cart))