import pytest
from pytest_html import extras
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    else:
        driver=webdriver.Ie()
        print("Launching default IE browser.........")
    return driver

def pytest_addoption(parser):    # get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # return the Browser value to setup method
    return request.config.getoption("--browser")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        # always add url to report
        extra.append(pytest_html.extras.url('http://www.example.com/'))
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            extra.append(pytest_html.extras.html('<div>Additional HTML</div>'))
        report.extra = extra

def pytest_html_report_title(report):
    report.title = "Automation Test Report"

#hook for Adding Environment info to HTML Report
# def pytest_configure(config):
#     config._metadata = {
#         "Tester": "Suprabha",
#         "Project Name": "Framework Practice",
#         "Module Name": "Customers"
#     }
#
# #hook for delete/Modify Environment info to HTML Report
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)