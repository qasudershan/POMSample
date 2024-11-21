import logging
import time

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.templates_page import TemplatesPage
from tests.base_test import BaseTest

logger = logging.getLogger(__name__)

class TestLoginProfile(BaseTest):
    def test_login_and_fetch_templates(self):
        login = LoginPage(self.driver)
        profile = ProfilePage(self.driver)
        templates = TemplatesPage(self.driver)

        logger.info("Logging in with valid credentials.")
        login.login("engg_user.noreply@prezent.ai", "kiqjemkh")

        logger.info("Navigating to profile.")
        profile.go_to_profile()

        template_names = templates.get_5template_names()
        logger.info(f"First five templates: {template_names}")
        assert len(template_names) == 5

        logger.info("Fetching active template.")
        active_template = templates.get_active_template()
        logger.info(f"Active template: {active_template}")

        logger.info("Logging out from Basics tab")
        profile.logout()
        assert login.is_email_input_field_visible()
