import unittest
from api.empolyee import EmployeeAPI
import logging


class TestEmployee(unittest.TestCase):
    employee_id = None

    # 前置处理
    def setUp(self):
        self.employee_api = EmployeeAPI()

    def test_add_employee(self):
        add_employee_data = {
            "username": "",         # 唯一
            "mobile": "",           # 唯一
            "TimeOfEntry": "",
            "WorkNumber": ""
        }
        response = self.employee_api.add_employee(add_employee_data=add_employee_data)

        # 添加日志信息
        logging.info("添加员工接口返回的信息为：{}".format(response.json()))

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertIn("操作成功", response.json().get("message"))

        TestEmployee.employee_id = response.json().get("data").get("id")
        print("提取员工的id为：", TestEmployee.employee_id)

    def test_update_employee(self):
        update_data = {
            "username": ""
        }
        response = self.employee_api.update_employee(TestEmployee.employee_id, update_data=update_data)
        print(response.json())

        # 断言
        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertIn("操作成功", response.json().get("message"))

    def test_get_employee(self):
        response = self.employee_api.get_employee(TestEmployee.employee_id)
        print(response.json())

        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertIn("操作成功", response.json().get("message"))

    def test_delete_employee(self):
        response = self.employee_api.delete_employee(TestEmployee.employee_id)
        print(response.json())

        self.assertEqual(200, response.status_code)
        self.assertEqual(True, response.json().get("success"))
        self.assertIn("操作成功", response.json().get("message"))