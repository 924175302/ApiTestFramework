import unittest
import requests
import logging
from api.login import LoginApi
from api.trust import TrustAPI


class test_trust(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()
        self.trust_api = TrustAPI()
        self.session = requests.Session()


    def tearDown(self):
        pass

    def test01_trust(self):
