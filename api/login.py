import requests
import config

class LoginApi():
    # 初始化
    def __int__(self):
        self.url_verify = config.BASE_URL + ""     # TODO
        self.url_login = config.BASE_URL + ""
        self.url_getImgCode = config.BASE_URL + ""
        self.url_register = config.BASE_URL + ""
        self.url_forget_password = config.BASE_URL + ""

    # 获取验证码
    def get_verify_code(self, session, phone):
        data = {
            "phone": phone
        }
        return session.post(self.url_verify, data=data)

    # 登录
    def Login(self, session, username, password, verify_code):
        login_data = {
            "username": username,
            "password": password,
            "verify_code": verify_code
        }
        return session.post(url=self.url_login, data=login_data)

    def getImgCode(self, session, r):
        url = self.url_getImgCode + r
        return session.get(url=url)

    def register(self, session, phone, password, imgVerifyCode="8888", phoneCode="6666", dyServer="on", invitePhone=""):
        register_data = {
            "phone": phone,
            "password": password,
            "imgVerifyCode": imgVerifyCode,
            "phoneCode": phoneCode,
            "dyServer": dyServer,
            "invitePhone": invitePhone
        }
        return session.post(url=self.url_register, data=register_data)
