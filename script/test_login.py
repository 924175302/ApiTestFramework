import json
import requests
import unittest
import config
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
    for case_data in db_data:             # TODO
        # username = case_data[]
        # password = case_data[]
        # verify_code = case_data[]
        # content_type = case_data[]
        # status_code = case_data[]
        # status = case_data[]
        # msg = case_data[]
        #test_data.append((username, password, verify_code, content_type, status_code, status, msg))
        print(test_data)
    return test_data


class TestLogin(unittest.TestCase):
    # 前置处理
    def setUp(self):
        self.login_api = LoginApi()            # 实例化接口类
        self.session = requests.session()      # 创建session对象

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
        response_login = self.login_api.Login(self, "username", "password", "verify_code")
        self.assertEqual(status_code, response_login.status_code)
        self.assertEqual(status, response_login.json().get("status"))
        self.assertIn(msg, response_login.json().get("msg"))

        # 提取Token信息
        config.TOKEN = "Bearer " + response_login.json().get("")    # TODO
        config.headers_data["Authorization"] = config.TOKEN
        print("Token值：", config.TOKEN)
