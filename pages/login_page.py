from pages.base_page import BasePage

class LoginPage(BasePage):
    URL = "https://prezent-uatstaging.myprezent.com/signin"
    EMAIL_INPUT = ("css selector", "input[id='username']")
    PASSWORD_INPUT = ("css selector", "input[id='password']")
    CONTINUE_BUTTON = ("css selector", "button[id='continue']")
    LOGIN_BUTTON = ("css selector", "button[id='submit']")


    def is_email_input_field_visible(self):
        return self.find_element(self.EMAIL_INPUT)

    def login(self, email, password):
        self.open(self.URL)
        self.type_text(self.EMAIL_INPUT, email)
        self.click(self.CONTINUE_BUTTON)
        self.type_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
