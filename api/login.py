import requests


class LoginApi():
    # 初始化
    def __int__(self):
        self.url_verify = ""     # TODO
        self.url_login = ""

    # 获取验证码
    def get_verify_code(self, session):
        return session.get(self.url_verify)

    # 登录
    def Login(self, session, username, password, verify_code):
        login_data = {
            "username": "username",
            "password": "password",
            "verify_code": "verify_code"
        }
        return session.post(url=self.url_login, data=login_data)