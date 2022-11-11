import logging
import unittest
from api.approve import ApproveAPI
import requests
from api.login import LoginApi
import utils


class Test_Approve(unittest.TestCase):
    realname = "張三"
    card_Id = ""    # TODO
    phone1 = ""
    password = ""


    def setUp(self):
        self.login_api = LoginApi()
        self.approve_api = ApproveAPI()
        self.session = requests.Session()

    def tearDown(self):
        if self.session:
            self.session.close()

    # 认证成功
    def test01_approve_success(self, session):
        # 1、首先登录
        response = self.login_api.Login(self.session, )
        logging.info("login response={}".format(response.json()))
        utils.common_assert(self, response, 200, 100, "登录成功")

        # 2、发送认证请求
        # 调用接口请求
        response = self.approve_api.approve(self.session, self.realname, self.card_Id)
        logging.info("approve response={}".format(response.json()))
        utils.common_assert(self, response, 200, 100, "提交成功")

    # 认证失败 姓名为空
    def test02_approve_realname_is_null(self):
        # 1、首先登录
        response = self.login_api.Login(self.session, self.phone1)
        logging.info("approve response={}".format(response.json()))
        utils.common_assert(self, response, 200, 100, "登录成功")

        # 2、发送认证请求
        # 调用接口请求
        response = self.approve_api.approve(self.session, "", self.card_Id)
        logging.info("approve response={}".format(response.json()))
        utils.common_assert(self, response, 200, 100, "姓名不能为空")

    # 认证失败 card_Id为空
    def test03_approve_cardId_is_null(self):
        # 1、首先登录
        response = self.login_api.Login(self.session, self.phone1)
        logging.info("approve response={}".format(response.json()))
        utils.common_assert(self, response, 200, 100, "登录成功")

        # 2、发送认证请求
        # 调用接口请求
        response = self.approve_api.approve(self.session, self.realname, "")
        logging.info("approve response={}".format(response.json()))
        utils.common_assert(self, response, 200, 100, "身份证号不能为空")

    def test04_get_approve(self):
        # 1、首先登录
        response = self.login_api.Login(self.session, self.phone1)
        logging.info("approve response={}".format(response.json()))
        utils.common_assert(self, response, 200, 100, "登录成功")

        response = self.approve_api.getApprove(self.session)
        logging.info("approve response={}".format(response.json()))
        self.assertEqual(200, response.status_code)
