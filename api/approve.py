import config


class ApproveAPI():
    def __int__(self):
        self.approve_url = config.BASE_URL + ""
        self.get_approve_url = config.BASE_URL + ""

    def approve(self, session, realname, card_Id):
        data = {
            "realname": realname,
            "card_id": card_Id
        }
        # files为multi-part构造的多消息体格式
        response = session.post(self.approve_url, data=data, files={'x': 'y'})
        return response

    def getApprove(self, session):
        response = session.post(self.approve_url)
        return response
