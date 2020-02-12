from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Choose language")


@pytest.fixture
def browser(request):    
    browser = webdriver.Chrome()    
    yield browser
    browser.delete_all_cookies()
    browser.quit()
