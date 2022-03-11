
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action = 'store', default = 'en',
                     help="Choose language: ru or en")

# only for chrome browser
@pytest.fixture(scope = 'function')
def browser(request):
    user_language = request.config.getoption('language')
    tuning = Options()
    tuning.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # turn off notifications DevTools
    tuning.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options = tuning)
    yield browser
    browser.quit()

# empty line