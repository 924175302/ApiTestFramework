import config


class TrustAPI:
    def __int__(self):
        self.trust_register_url = config.BASE_URL + ''
        self.get_recharge_verify_code_url = config.BASE_URL + ''
        self.recharge_url = config.BASE_URL + ''

    def trust_register(self, session):
        return session.post(self.trust_register_url)

    def get_recharge_verify_code(self, session, r):
        url = self.get_recharge_verify_code_url + r
        return session.get(url)

    def recharge(self, session, amount='1000', code='8888'):
        data = {
            "paymentType": "chinapnrTrust",
            "formStr": "reForm",
            "amount": amount,
            "valicode": code
        }
        return session.post(self.recharge_url, data=data)
