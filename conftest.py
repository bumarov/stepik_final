from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="Choose language")


@pytest.fixture
def browser(request):
    # language = request.config.getoption("language")
    # link = f"http://selenium1py.pythonanywhere.com/"\
    #   "{language}/catalogue/coders-at-work_207/"
    browser = webdriver.Chrome()
    # browser.get(link)
    yield browser
    browser.quit()
