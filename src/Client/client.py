import socket
from time import sleep


class client:
    def __init__(self,nickname:str):
        self.nickname :str = "test"

    def connect(self,ip,port):
        sc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        print("WAIT")
        sc.connect((ip,port))
        print("\n\nConnected")
        while(True):
            sc.send(f"{self.nickname}".encode())
            date = sc.recv(1024)
            print(date)
            sleep(5)
client("test").connect("127.0.0.1",9090)