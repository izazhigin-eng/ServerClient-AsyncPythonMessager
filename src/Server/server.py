from time import sleep

from user import user

import socket,asyncio

class server:
    def __init__(self,name, maxConnections:int = 10, authenticate:bool=True, manualAllowedConnections:bool=True):
        self.users = []
        self.name = name

    def run(self, port):
        asyncio.run(self._run(port))

    async def _getConnect(self,sc:socket.socket):
        print("Waiting for connection...")
        con = await sc.accept()
        print("+ Succseful connected")
        return con

    async def _run(self, port:int):
        sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sc.bind(('localhost', port))
        sc.listen(1)
        clsc = None
        #sc.setblocking(False)

        while (True):
            if clsc is None:
                l = []
                for i in range(10):
                    t = asyncio.create_task(self._getConnect(sc))
                    #asyncio.
                    t.add_done_callback(lambda a: self.users.append(a.result()))
                    l.append(t)
                asyncio.gather(l)
                clsc = 1

            print("Loop",self.users)
            sleep(1)

    def _getAllActiveUsers(self)->list:
        pass

    def _authenticate(self)->bool:
        pass

    def _userHasConnected(self): pass
    def _userHasDisconnected(self): pass


    def registration(self)->bool:
        pass
if __name__ == '__main__':
    s = server("Test")
    s.run(9090)