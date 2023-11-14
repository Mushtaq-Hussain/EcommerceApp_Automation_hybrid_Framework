from selenium import webdriver
import pytest


@pytest.fixture()
def setUp(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("************launching chrome browser***********")
    elif browser == "firefox":
        driver = webdriver.Firefox()
        print("**********launching firefox browser**********")
    else:
        driver = webdriver.Edge()
        print("**********launching Edge Explorer browser**********")
    return driver


def pytest_addoption(parser):  # this method will get the value from CLI
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # this will get the browser value to setUp method
    return request.config.getoption("--browser")


####################Pytest Html Reports###########################

# It is hook for adding environment info to html report
def pytest_configure(config):
    config._metadata['Project Name'] = 'NOP Commerce Application'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester Name'] = 'Mushtaq Hussain'


def pytest_html_report_title(report):
    report.title = "NOP Commerce Application"


