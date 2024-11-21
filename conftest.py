import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.safari.service import Service as SafariService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def create_driver(browser_name):
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Chrome(service=ChromeService(), options=options)
    elif browser_name == "edge":
        options = EdgeOptions()
        options.add_argument("--start-maximized")
        return webdriver.Edge(service=EdgeService(), options=options)
    elif browser_name == "safari":
        return webdriver.Safari(service=SafariService())
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on: chrome, edge, safari.",
    )

@pytest.fixture(scope="class")
def browser_setup(request):
    browser_name = request.config.getoption("--browser").lower()
    driver = create_driver(browser_name)
    request.cls.driver = driver
    yield
    driver.quit()
