import pytest

from python_sample.app.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, url=url)
    return fixture


@pytest.fixture(scope="module", autouse=True)
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store")
