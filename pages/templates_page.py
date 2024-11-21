from pages.base_page import BasePage

class TemplatesPage(BasePage):
    TEMPLATES_TAB = ("css selector", """a[href="#templates"]""")
    TEMPLATE_NAME = ("xpath", """//div[@class="templateNameAndShare__content"]/div""")
    ACTIVE_TEMPLATE = ("xpath", """//*[@id="templates"]//button[@class="v-btn v-btn--text theme--light v-size--default select-theme active"]/preceding-sibling::div//div[@class="templateNameAndShare__content"]/div""")

    def get_5template_names(self):
        self.click(self.TEMPLATES_TAB)
        template_elements = self.find_elements(self.TEMPLATE_NAME)
        template_names = [template_element.text for template_element in template_elements]
        return sorted(template_names)[:5]

    def get_active_template(self):
        return self.get_text(self.ACTIVE_TEMPLATE)
