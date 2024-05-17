import socket, RSA
from cryptography.fernet import Fernet

class Receiver:
    # initialize an encrypted TCP chatroom receiver
    def __init__(self, ip: str, port: int) -> None:
        self.host = (ip, port)
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.conn.bind(self.host)

    def __enter__(self): return self
    def __exit__(self, t, v, tb): self.conn.close()

    # receive and return bytes data
    def get_message(self) -> bytes:
        sssk, _ = self.conn.recvfrom(1024)
        data, _ = self.conn.recvfrom(1024)
        return Fernet(sssk).decrypt(data)


