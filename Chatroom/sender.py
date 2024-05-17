import socket, RSA
from cryptography.fernet import Fernet

class Sender:
    # initialize an encrypted chatroom sender
    def __init__(self, ip: str, port: int, e: int = 65537) -> None:
        self.dest = (ip, port)
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def __enter__(self): return self
    def __exit__(self, t, v, tb): 
        self.send_message(b'')
        self.conn.close()

    # encrypts and sends a message
    def send_message(self, message: bytes):
        cipher_text = self.fernet.encrypt(message)
        self.conn.sendto(self.key, self.dest)
        self.conn.sendto(cipher_text, self.dest)