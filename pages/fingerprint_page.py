from pages.base_page import BasePage

class FingerPrintPage(BasePage):
    FINGERPRINT_TAB = ("css selector", """a[href="#fingerprint"]""")
    RETAKE_FINGERPRINT_LINK = ("xpath", """//*[@class = "btn-retake"]""")

    def go_to_fingerprint_tab(self):
        self.click(self.FINGERPRINT_TAB)

    def retake_fingerprint(self):
        self.click(self.RETAKE_FINGERPRINT_LINK)


