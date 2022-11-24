import random
import unittest
import requests
import logging
from api.login import LoginApi
from api.trust import TrustAPI
import utils
from bs4 import BeautifulSoup


class test_trust(unittest.TestCase):
    def setUp(self):
        self.login_api = LoginApi()
        self.trust_api = TrustAPI()
        self.session = requests.Session()

    def tearDown(self):
        if self.session:
            self.session.close()

    def test01_trust(self):
        # 1、登陆
        response = self.login_api.Login(self.session)
        logging.info("login response = {}".format(response.json()))
        utils.common_assert(self, response, 200, 200, "登陆成功")

        # 2、请求trust接口
        response = self.trust_api.trust_register(self.session)
        self.assertEqual(200, response.status_code)
        self.assertEqual(200, response.json().get('status'))

        # 3、发送第三方请求
        form_data = response.json().get('form')
        logging.info('form response = {}'.format(form_data))

        # 解析form表单数据，提取第三方参数
        soup = BeautifulSoup(form_data, 'html.parser')
        third_url = soup.form['action']  # 获取该字段的url
        logging.info("third request url = {}".format(third_url))

        data = {}
        for input in soup.find_all('input'):
            data.setdefault(input['name'], input['value'])
        logging.info("third request data = {}".format(data))

        response = requests.post(third_url, data)
        utils.common_assert('UserRegister OK', response.text)

    def test_recharge(self):
        response = self.login_api.Login(self.session)
        logging.info("login response = {}".format(response.json()))
        utils.common_assert(self, response, 200, 200, "登陆成功")

        r = random.random()
        response = self.trust_api.get_recharge_verify_code_url(self.session, str(r))
        self.assertEqual(200, response.status_code)

        response = self.trust_api.recharge(self.session, 10000)
        logging.info("recharge response = {}".format(response.json()))
        self.assertEqual(200, response.status_code)

        form_data = response.json().get("description").get("form")
        logging.info('form response={}'.format(form_data))
        soup = BeautifulSoup(form_data, "html.parser")
        third_url = soup.form['action']    # 标签名
        data = {}
        for input in soup.find_all('input'):
            data.setdefault(input['name'], input['value'])
        logging.info("third request data = {}".format(form_data))
        response = requests.post(third_url, data=data)
        logging.info('third trust response={}'.format(form_data))
        return response


