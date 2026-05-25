import pytest
from selenium import webdriver

from data import URLs

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(URLs.MAIN_PAGE)
    yield driver
    
    driver.quit()

    