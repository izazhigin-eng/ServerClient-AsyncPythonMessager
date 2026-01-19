STATUS_ONLINE = 0
STATUS_OFFLINE = 1

import cryptography

class user:
    def __init__(self,login, passwd, lastIP, nickname, dateRegister):
        self._login = login
        self._password = passwd
        self.lastIP = lastIP
        self.nickname = nickname
        self.status = STATUS_OFFLINE
        self._dateRegister = dateRegister

    def __dict__(self):
        return {
            "login"         :   self._login,
            "password"      :   self._password,
            "lastIP"        :   self.lastIP,
            "nickname"      :   self.nickname,
            "status"        :   self.status,
            "dateRegister"  :   self._dateRegister
        }
