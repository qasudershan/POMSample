from pages.base_page import BasePage
import time

class ProfilePage(BasePage):
    BASICS_TAB = ("css selector", """a[href="#basics"]""")
    PROFILE_ICON = ("css selector", "div.right-nav-item.profile-link")
    LOGOUT_BUTTON = ("css selector", "div>button.edit-profile-btn.log-out-button")

    def go_to_profile(self):
        self.click(self.PROFILE_ICON)

    def logout(self):
        self.click(self.BASICS_TAB)
        time.sleep(2)
        self.click(self.LOGOUT_BUTTON)
