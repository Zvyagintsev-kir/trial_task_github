import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Firefox", help="use webdriver for browser")
    parser.addoption("--start_url", action="store", default="http://www.github.com/join", help="this is start url")


@pytest.fixture(scope="session")
def selenium_driver(request):
    if request.config.getoption("--browser") == 'Chrome':
        driver = webdriver.Chrome()
    elif request.config.getoption("--browser") == 'Firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Ie()

    driver.maximize_window()
    driver.get(request.config.getoption("--start_url"))
    yield driver
    driver.quit()

