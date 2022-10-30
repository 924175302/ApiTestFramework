import utils
import config
import json
import requests


class EmployeeAPI():
    def __int__(self):             # TODO
        self.url_add_employee =  config.BASE_URL + ""
        self.url_update_employee = config.BASE_URL + ""  # id用{}占位
        self.url_delete_employee = config.BASE_URL + ""

    def add_employee(self, add_employee_data):
        return requests.post(url=self.url_add_employee, json=add_employee_data, headers=config.headers_data)

    def update_employee(self,  employee_id, update_data):
        url = self.url_update_employee.format(employee_id)
        return requests.put(url=url, json=update_data, headers=config.headers_data)

    def get_employee(self, employee_id):
        url = self.url_update_employee.format(employee_id)
        return requests.get(url=url, headers=config.headers_data)

    def delete_employee(self, employee_id):
        url = self.url_update_employee.format(employee_id)
        return requests.delete(url=url, headers=config.headers_data)