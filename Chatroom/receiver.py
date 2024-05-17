import socket, RSA
from cryptography.fernet import Fernet

class Receiver:
    # initialize an encrypted TCP chatroom receiver
    def __init__(self, ip: str, port: int) -> None:
        self.host = (ip, port)
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.conn.bind(self.host)
        name, d, n = RSA.get_private_config()
        self.name = name
        self.priv_key = (d, n)

    def __enter__(self): return self
    def __exit__(self, t, v, tb): self.conn.close()

    # receive and decryptes message
    def get_message(self) -> bytes:
        self.sender, _ = self.conn.recvfrom(1024)
        self.sender = self.sender.decode()
        sender_key = RSA.get_public_key(self.sender)
        cipher_sssk, _ = self.conn.recvfrom(1024)
        cipher_text, _ = self.conn.recvfrom(1024)
        cipher_sssk = RSA.decrypt(cipher_sssk, self.priv_key)
        sssk = RSA.decrypt(cipher_sssk, sender_key)
        try: message = Fernet(sssk).decrypt(cipher_text)
        except ValueError: raise Exception('Cannot decrypt; message compromised')
        return message


