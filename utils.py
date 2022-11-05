# unitest公共断言方法
import logging
import os.path
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
