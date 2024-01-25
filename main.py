# import time
#
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.service import Service
#
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager
#
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get('https://yandex.by/')
# time.sleep(10)
#
#
# def driver_Edge():
#     driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
#     yield driver
#     driver.close()
#     driver.quit()
#
# def driver_Chrom():
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#     yield driver
#     driver.close()
#     driver.quit()


import time

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By


@pytest.fixture
def driver_Edge():
    driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    yield driver
    driver.close()
    driver.quit()


@pytest.fixture
def driver_chrome():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.close()
    driver.quit()
#
#
# def test_chrome(driver_chrome):
#     driver_chrome.get('https://pypi.org/project/pytest/')
#     cookie = {'name': 'test', 'value': 'value'}
#     driver_chrome.add_cookie(cookie)
#     test_cookie = driver_chrome.get_cookie('test')
#     driver_chrome.delete_cookie(cookie)
#
#     assert cookie['name'] == test_cookie['name']
#
#
# def test_firefox(driver_Edge):
#     driver_Edge.get('https://pypi.org/project/pytest/')


# def test_navigate_yo_shop_menu(driver_chrome):
#     driver_chrome.get('https://www.onliner.by/')
#     xpath = '//*[@id="widget-9-1"]/div/a[1]'
#     element = driver_chrome.find_element(By.XPATH, xpath)
#
#     element.click()
#
#     assert driver_chrome.title == 'Как сильно снижаются цены? Посмотрели на виртуальные полки интернет-магазинов'
#     assert driver_chrome.current_url == 'https://money.onliner.by/2024/01/09/skidki-yanvarya'


# def test_navigate_yo_shop_menu_2(driver_Edge):
#     driver_Edge.get('https://money.onliner.by/2024/01/09/skidki-yanvarya')
#     xpath = '//*[@id="container"]/div/div/div/div/div[3]/div[1]/div[1]/div/div[2]/div/div[1]/div[2]/h3[1]/a'
#     element = driver_Edge.find_element(By.XPATH, xpath)
#
#     element.click()
#
#     assert driver_Edge.title == 'Игровая мышь Logitech G102 Lightsync (черный)'
#     assert driver_Edge.current_url == 'https://catalog.onliner.by/mouse/logitech/910005823'

def test_get_attribute(driver_chrome):
    driver_chrome.get('https://www.onliner.by/')
    xpath = '//*[@id="widget-9-1"]/div/a[1]'
    element = driver_chrome.find_element(By.XPATH, xpath)

    element.click()

    assert element.get_attribute('href') in 'https://money.onliner.by/2024/01/09/skidki-yanvarya'
