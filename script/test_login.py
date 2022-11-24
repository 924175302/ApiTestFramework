import json
import logging
import requests
import unittest
import config
import random
import utils
from tools.dbutil import DButil
from api.login import LoginApi
from parameterized import parameterized


# 读取json类型的测试数据
def build_data_json():
    # 读取参数文件地址
    file = config.BASE_DIR + "/data/login.json"
    test_data = []
    with open(file, encoding="utf-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            username = case_data.get("username")
            password = case_data.get("password")
            verify_code = case_data.get("verify_code")
            content_type = case_data.get("content_type")
            status_code = case_data.get("status_code")
            status = case_data.get("status")
            msg = case_data.get("msg")
            test_data.append((username, password, verify_code, content_type, status_code, status, msg))
            print(test_data)
    return test_data


# 读取bd中的数据
def build_data_bd():
    # 需要执行的sql
    sql = "select  "
    db_data = DButil.exec_sql(sql)
    test_data = []
    # 通过bd中数据的下表获取响应的字段信息
    for case_data in db_data:  # TODO
        # username = case_data[]
        # password = case_data[]
        # verify_code = case_data[]
        # content_type = case_data[]
        # status_code = case_data[]
        # status = case_data[]
        # msg = case_data[]
        # test_data.append((username, password, verify_code, content_type, status_code, status, msg))
        print(test_data)
    return test_data


class TestLogin(unittest.TestCase):
    phone1 = ""
    password = ""
    imgCode = ""
    verifyCode = ""

    # 前置处理
    def setUp(self):
        self.login_api = LoginApi()  # 实例化接口类
        self.session = requests.session()  # 创建session对象

    # 后置处理
    def tearDown(self):
        if self.session:
            self.session.close()

    # 测试用例
    # 登录成功
    @parameterized.expand(build_data_json())
    def test01_login(self, username, password, verify_code, content_type, status_code, status, msg):
        # 调用验证码接口获取验证，并进行断言
        # 调用登录接口获取登录信息，并进行断言
        response_verify = self.login_api.get_verify_code(self.session)
        self.assertEqual(status_code, response_verify.status_code)
        self.assertIn(content_type, response_verify.headers.get("Content-Type"))

        # 传入用户名、密码和验证码
        response_login = self.login_api.Login(self, username, password, verify_code)
        self.assertEqual(status_code, response_login.status_code)
        self.assertEqual(status, response_login.json().get("status"))
        self.assertIn(msg, response_login.json().get("msg"))

        # 提取Token信息
        config.TOKEN = "Bearer " + response_login.json().get("")  # TODO
        config.headers_data["Authorization"] = config.TOKEN
        print("Token值：", config.TOKEN)

    def test_login_wrong_password(self, phone1):
        wrong_password = "error"
        response = self.login_api.Login(self.session, username=phone1, password=wrong_password)
        logging.info("login response = {}".format(response.json()))
        utils.common_assert(self, response, 200, 100, "密码错误")

    # 参数为随机小数时获取图片验证码
    def test01_get_img_code(self):
        r = random.random()
        response = self.login_api.getImgCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

    # 参数为随机整数时获取图片验证码
    def test02_get_img_code(self):
        r = random.randint(10000, 90000)
        response = self.login_api.getImgCode(self.session, str(r))
        self.assertEqual(200, response.status_code)

    # 参数为空
    def test03_get_img_code(self):
        response = self.login_api.getImgCode(self.session, "")
        self.assertEqual(404, response.status_code)

    # 参数为随机字母
    def test04_get_img_code(self):
        r = random.sample("abcdefghijklm", 8)
        # r为列表，转换为str
        r1 = ''.join(r)
        response = self.login_api.getImgCode(self.session, r1)
        self.assertEqual(200, response.status_code)

    @parameterized.expand(utils.read_imgVerify_data("imgVerify.json"))
    def test_get_img_code(self, type, status_code):
        r = ''
        if type == "float":
            r = random.random()
        elif type == "int":
            r = random.randint()
        elif type == "char":
            #  从制定序列中获取制定长度
            r = ''.join(random.sample("abcdefghijklm", 8))
            response = self.login_api.getImgCode(self.session, r)
        self.assertEqual(status_code, response.status_code)


    def test05_register_success(self, phone1):
        r = random.random()
        response = self.login_api.getImgCode(self.session, str(r))
        self.assertEqual(200, response.status_code)
        response = self.login_api.get_verify_code(self.session, phone1)
        logging.info("register response = {}".format(response.json()))
        utils.common_assert(self, response, 200, 100, "密码不能为空")

    def test06_login_wrong_password(self):
        wrong_password = "error"
        response = self.login_api.Login(self.session, self.phone1, wrong_password)
        logging.info("login response = {}".format(response.json()))
        utils.common_assert(self, response, 200, 100, "密码错误1次，达到3次将锁定账户")

        response = self.login_api.Login(self.session, self.phone1, wrong_password)
        logging.info("login response = {}".format(response.json()))
        utils.common_assert(self, response, 200, 100, "密码错误2次，达到3次将锁定账户")

        response = self.login_api.Login(self.session, self.phone1, wrong_password)
        logging.info("login response = {}".format(response.json()))
        utils.common_assert(self, response, 200, 100, "由于连续输入错误密码达到上线，账号已被锁定，请于1分钟后重试")
