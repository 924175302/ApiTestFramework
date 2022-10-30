import json
import requests
import unittest
from api.login import LoginApi
from parameterized import parameterized
from tools.build_data import build_data_json


class TestLogin(unittest.TestCase):
    #前置处理
    def setUp(self):
        self.login_api = LoginApi()            #实例化接口类
        self.session = requests.session()      #创建session对象

    #后置处理
    def tearDown(self):
        if self.session:
            self.session.close()

    #测试用例
    #登录成功
    @parameterized.expand(build_data_json())
    def test01_login(self, username, password, verify_code, content_type, status_code, status, msg):
        # 调用验证码接口获取验证，并进行断言
        # 调用登录接口获取登录信息，并进行断言
        response_verify = self.login_api.get_verify_code(self.session)
        self.assertEqual(status_code, response_verify.status_code)
        self.assertIn(content_type, response_verify.headers.get("Content-Type"))

        # 传入用户名、密码和验证码
        response_login = self.login_api.Login(self, "username", "password", "verify_code")
        self.assertEqual(status_code, response_login.status_code)
        self.assertEqual(status, response_login.json().get("status"))
        self.assertIn(msg, response_login.json().get("msg"))
