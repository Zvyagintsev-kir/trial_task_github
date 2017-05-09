import pytest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def pytest_addoption(parser):
    parser.addoption("--selenium_host", action="store", default="http://localhost:4444/wd/hub", help="use webdriver for browser")
    parser.addoption("--browser", action="store", default="Firefox", help="use webdriver for browser")
    parser.addoption("--start_url", action="store", default="http://www.github.com/join", help="this is start url")


# def pytest_runtest_makereport(__multicall__, item):
#     _driver = item.funcargs['test_driver']
#     browser_type = _driver.capabilities['browserName']
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     report = __multicall__.execute()
#     extra = getattr(report, 'extra', [])
#     if report.when == 'call':
#         url = _driver.current_url
#         extra.append(pytest_html.extras.url(url))
#         screenshot = _driver.get_screenshot_as_base64()
#         extra.append(pytest_html.extras.image(screenshot, ''))
#         report.extra = extra
#     return report


@pytest.fixture(scope="session")
def selenium_driver(request):
    executor = request.config.getoption("--selenium_host")
    if request.config.getoption("--browser") == 'Chrome':
        driver = webdriver.Remote(command_executor=executor,
                                  desired_capabilities=DesiredCapabilities.CHROME)
    elif request.config.getoption("--browser") == 'Firefox':
        driver = webdriver.Remote(command_executor=executor,
                                  desired_capabilities=DesiredCapabilities.FIREFOX)
    else:
        driver = webdriver.Remote(command_executor=executor,
                                  desired_capabilities=DesiredCapabilities.HTMLUNITWITHJS)

    driver.maximize_window()
    driver.get(request.config.getoption("--start_url"))
    request.node._driver = driver
    yield driver
    driver.quit()

