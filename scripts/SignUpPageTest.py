import time
import unittest

import util.Logger as cl
import logging

from pages.HomePage import HomePage
from pages.ProfilePage import ProfilePage


class SignUpPageTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    def setUp(self):
        self.homePage = HomePage()
        self.driver = self.homePage.driver
        prop = self.homePage.dic_prop
        self.signUpPage = self.homePage.clickToSignUp()
        self.longMessage = False
        self.log.debug(self.id())

    def test_signUpPageTitleTest(self):
        title = self.signUpPage.validateSignUpPageTitle()
        self.assertEqual(title, "Sign Up - Udacity", msg="test_signUpPageTitleTest Failed")

    def test_verifySignUpToUdacity(self):
        profile_obj = self.signUpPage.signUpToUdacity()
        time.sleep(10)
        self.assertIsInstance(profile_obj, ProfilePage, msg="test_validateSignUpToUdacity Failed")

    def tearDown(self):
        self.driver.quit()
