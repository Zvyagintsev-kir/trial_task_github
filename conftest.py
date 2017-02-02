import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Firefox", help="use webdriver for browser")
    parser.addoption("--start_url", action="store", default="http://www.github.com/join", help="this is start url")


def pytest_runtest_makereport(__multicall__, item):
    _driver = item.funcargs['test_driver']
    browser_type = _driver.capabilities['browserName']
    pytest_html = item.config.pluginmanager.getplugin('html')
    report = __multicall__.execute()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        url = _driver.current_url
        extra.append(pytest_html.extras.url(url))
        screenshot = _driver.get_screenshot_as_base64()
        extra.append(pytest_html.extras.image(screenshot, ''))
        report.extra = extra
    return report


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
    request.node._driver = driver
    yield driver
    driver.quit()

