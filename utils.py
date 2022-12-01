# unitest公共断言方法
import json
import logging
import os.path
import config
from logging import handlers


def common_assert(self, response, status_code, success, message):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertIn(message, response.json().get("message"))


def init_logging():
    # 1、创建一个日志器
    logger = logging.getLogger()

    # 2、设置日志的等级,如果日志级别低于这是的级别，则不会打印日志
    logger.setLevel(logging.INFO)

    # 3、设置处理器
    # 控制台处理器：控制把日志输出到控制台
    sf = logging.StreamHandler()

    # 文件处理器：控制把日志输出到外部文件当中，需提前定义文件的路径和文件名
    log_name = os.path.dirname(os.path.abspath(__file__)) + "/log/"  # TODO日志位置
    fh = logging.handlers.TimedRotatingFileHandler(log_name, when="M", interval=1, backupCount=7, encoding="utf-8")

    # 4、设置格式化器：指定打印日志时的格式内容
    fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d] -%(message)s"
    formatter = logging.Formatter(fmt)

    # 5、将格式化器添加到处理器当中（文件处理器和控制台处理器都需要添加）
    sf.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 6、 将处理器添加到日志器当中
    logger.addHandler(sf)
    logger.addHandler(fh)


init_logging()
logging.info("")


def read_imgVerify_data(file_name):
    file = config.BASE_URL + "/data/" + file_name
    test_case_data = []
    with open(file, encoding="utf-8") as f:
        verify_data = json.load(f)
        test_data_list = verify_data.get("test_get_img_verify_code")
        for test_data in test_data_list:
            test_case_data.append((test_data.get("type"), test_data.get()))
    return test_case_data


def read_register_data(filename):
    file = config.BASE_URL + "/data" + filename
    test_case_data = []
    with open(file, encoding="utf-8") as f:
        # json 转化为字典
        register_data = json.load(f)
        test_data_list = register_data.get("test_register")
        for test_data in test_data_list:
            test_case_data.append((test_data.get("phone"), test_data.get("pwd"), test_data.get("")))
    return test_case_data


# 统一读取所有参数数据文件的方法
def read_param_data(filename, method_name, param_names,):
    # filename：参数数据文件名
    # method_name: 参数数据文件中定义的测试数据列表名称，如rest_register
    # param_name: 参数数据文件中一组测试数据中所有的参数组成的字符串

    file = config.BASE_URL + "/data/" + filename
    test_case_data = []
    with open(file, encoding="utf-8") as f:
        file_data = json.load(f)
        test_data_list = file_data.get(method_name)
        for test_data in test_data_list:
            test_params = []
            for param in param_names.split(","):
                test_params.append(test_data.get(param))
            test_case_data.append(test_params)
    return test_case_data

