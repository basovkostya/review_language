from selenium.webdriver.common.by import By
import pytest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestRegistration():
    def test_open_stepik(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        time.sleep(30)
        button = WebDriverWait(browser, 12).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-add-to-basket')))
        assert button.text == 'Ajouter au panier' or button.text == 'Añadir al carrito', 'Кнопка не доступна'
