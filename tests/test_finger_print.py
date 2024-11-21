import logging
import pytest

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from pages.templates_page import TemplatesPage
from pages.fingerprint_page import FingerPrintPage
from tests.base_test import BaseTest

logger = logging.getLogger(__name__)

class TestFingerPrint(BaseTest):

    @pytest.mark.xfail
    def test_finger_print(self):
        login = LoginPage(self.driver)
        profile = ProfilePage(self.driver)
        templates = TemplatesPage(self.driver)
        fingerprint = FingerPrintPage(self.driver)

        logger.info("Logging in with valid credentials.")
        login.login("engg_user.noreply@prezent.ai", "kiqjemkh")

        logger.info("Navigating to profile")
        profile.go_to_profile()

        logger.info("Click fingerprint tab")
        fingerprint.go_to_fingerprint_tab()

        logger.info("Click on Re-take Fingerprint and complete the steps.")
        fingerprint.retake_fingerprint()

        #TODO:Step: At each step, print all available options and indicate which option was selected.

        #TODO:Step: Click Go Back to Prezent and then go to Profile and log out.