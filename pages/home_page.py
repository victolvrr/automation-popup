from pages.base_page import BasePage
from appium.webdriver.common.appiumby import AppiumBy

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.show_pop_up = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(0)')
        self.confirm_button = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(1)')
        self.notification = (AppiumBy.XPATH, "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[2]/android.widget.Button")
        self.allow = (AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button")
        self.automation_module = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").instance(2)')

    def select_pop_up(self):
        self.click_element(*self.show_pop_up)

    def select_accept(self):
        self.click_element(*self.confirm_button)

    def select_notification(self):
        self.click_element(*self.notification)
    
    def select_allow(self):
        self.click_element(*self.allow)
    
    def select_automation_module(self):
        self.click_element(*self.automation_module)