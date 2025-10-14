import pytest
import json
from pathlib import Path
from appium import webdriver
from appium.options.common.base import AppiumOptions
from selenium.common.exceptions import InvalidSessionIdException

# FIXTURE: DRIVER (SETUP + TEARDOWN)
@pytest.fixture(scope="function")
def driver():
    """Inicializa e encerra a sessão Appium para cada teste."""
    options = AppiumOptions()
    options.load_capabilities({
        "platformName": "Android",
        "appium:deviceName": "emulator-5554",
        "appium:automationName": "UiAutomator2",
        "appium:appPackage": "com.automationmodule",
        "appium:appActivity": "com.automationmodule/.MainActivity"
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver