from pytest import fixture

from selenium  import webdriver

from webdriver_manager.chrome import ChromeDriverManager # For Chrome

@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome(ChromeDriverManager().install())
    # browser = webdriver.Chrome("/usr/local/bin/chromedriver")
    # return browser
    yield browser

    # Teardown
    print("I am tearing down this browser")



# import pytest


# def pytest_addoption(parser):
#     parser.addoption(
#         "-E",
#         action="store",
#         metavar="NAME",
#         help="only run tests matching the environment NAME.",
#     )


# def pytest_configure(config):
#     # register an additional marker
#     config.addinivalue_line(
#         "markers", "env(name): mark test to run only on named environment"
#     )


# def pytest_runtest_setup(item):
#     envnames = [mark.args[0] for mark in item.iter_markers(name="env")]
#     if envnames:
#         if item.config.getoption("-E") not in envnames:
#             pytest.skip(f"test requires env in {envnames!r}")

# import sys


# def pytest_runtest_setup(item):
#     for marker in item.iter_markers(name="my_marker"):
#         print(marker)
#         sys.stdout.flush()

# import sys


# def pytest_runtest_setup(item):
#     for mark in item.iter_markers(name="glob"):
#         print(f"glob args={mark.args} kwargs={mark.kwargs}")
#         sys.stdout.flush()

# import sys

# import pytest

# ALL = set("darwin linux win32".split())


# def pytest_runtest_setup(item):
#     supported_platforms = ALL.intersection(mark.name for mark in item.iter_markers())
#     plat = sys.platform
#     if supported_platforms and plat not in supported_platforms:
#         pytest.skip(f"cannot run on platform {plat}")

# import pytest


# def pytest_collection_modifyitems(items):
#     for item in items:
#         if "interface" in item.nodeid:
#             item.add_marker(pytest.mark.interface)
#         elif "event" in item.nodeid:
#             item.add_marker(pytest.mark.event)
