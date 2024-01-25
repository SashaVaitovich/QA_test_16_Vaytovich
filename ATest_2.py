import time

import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from selenium import webdriver


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()


# def test_by_name(driver_chrome):
#     driver_chrome.get('https://ozon.by/')
#     name = "yandex-tableau-widget"
#     assert driver_chrome.find_element(By.NAME, name)
#
#
# def test_by_tag_name(driver_chrome):
#     driver_chrome.get('https://habr.com/ru/articles/667238/')
#     tag = 'span'
#     assert driver_chrome.find_element(By.TAG_NAME, tag)
#
#
# def test_by_link_id(driver_chrome):
#     driver_chrome.get('https://habr.com/ru/articles/667238/')
#     text = 'Моя лента'
#     assert driver_chrome.find_element(By.LINK_TEXT, text)
#
#
# def test_by_class_name(driver_chrome):
#     driver_chrome.get('https://habr.com/ru/articles/667238/')
#     class_name = 'tm-adfox-banner__container'
#     elements = driver_chrome.find_elements(By.CLASS_NAME, class_name)
#     assert len(elements) == 4

def test_by_name_css(driver_chrome):
    driver_chrome.get('https://demo.guru99.com/test/newtours/register.php')
    css = "__uspapiLocator"
    assert driver_chrome.find_element(By.CSS_SELECTOR, css)


def test_by_tag_name(driver_chrome):
    driver_chrome.get('https://habr.com/ru/articles/667238/')
    tag = 'span'
    assert driver_chrome.find_element(By.TAG_NAME, tag)


def test_by_link_id(driver_chrome):
    driver_chrome.get('https://habr.com/ru/articles/667238/')
    text = 'Моя лента'
    assert driver_chrome.find_element(By.LINK_TEXT, text)


def test_by_id_css(driver_chrome):
    driver_chrome.get('https://habr.com/ru/articles/667238/')
    css_id = '#site-name'
    time.sleep(5)
    assert driver_chrome.find_element(By.CSS_SELECTOR, css_id)


def test_by_class_name_css(driver_chrome):
    driver_chrome.get('https://www.wildberries.by/')
    class_name = '[class="recommendations__container main-container"]' # или '.recommendations__container.main-container'
    time.sleep(5)
    assert driver_chrome.find_element(By.CSS_SELECTOR, class_name)


def test_by_xpath_id(driver_chrome):
    driver_chrome.get('https://ozon.by/')
    xpath_id = '//form/button/div' # или //div[@class='ag15-a'] или //*[@class='ag15-a']
    time.sleep(5)
    assert driver_chrome.find_element(By.XPATH, xpath_id)


def test_by_xpath_id_text(driver_chrome):
    driver_chrome.get('https://ozon.by/')
    xpath_text = '//*[text()= "Детские товары"]' # или //div[@class='ag15-a'] или //*[contains(text(), "Детские товары")]
    time.sleep(5)
    assert driver_chrome.find_element(By.XPATH, xpath_text)
# find_element(By.ID, "id")
# find_element(By.NAME, "name")
# find_element(By.XPATH, "xpath")
# find_element(By.LINK_TEXT, "link text")
# find_element(By.PARTIAL_LINK_TEXT, "partial link text")
# find_element(By.TAG_NAME, "tag name")
# find_element(By.CLASS_NAME, "class name")
# find_element(By.CSS_SELECTOR, "css selector")
