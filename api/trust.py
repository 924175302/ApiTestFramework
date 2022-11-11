import config


class TrustAPI():
    def __int__(self):
        self.trust_register_url = config.BASE_URL + ''

    def trust_register(self, session):
        return session.post(self.trust_register_url)
