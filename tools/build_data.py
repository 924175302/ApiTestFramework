import json
import config
from tools.dbutil import DButil


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
    for case_data in db_data:
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
