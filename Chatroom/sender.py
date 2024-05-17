import socket, RSA
from cryptography.fernet import Fernet

class Sender:
    # initialize an encrypted chatroom sender
    def __init__(self, ip: str, port: int, recipient: str) -> None:
        self.dest = (ip, port)
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        name, d, n = RSA.get_private_config()
        self.name = name
        self.priv_key = (d, n)
        self.recipient_key = RSA.get_public_key(recipient)
        sssk = Fernet.generate_key()
        self.fernet = Fernet(sssk)
        cipher_sssk = RSA.encrypt(sssk, self.priv_key)
        self.cipher_sssk = RSA.encrypt(cipher_sssk, self.recipient_key)

    def __enter__(self): return self
    def __exit__(self, t, v, tb): self.conn.close()

    # encrypts and sends a message
    def send_message(self, message: bytes):
        # S -> R: S, {{SSSK}PRs}PUr, {m}SSSK
        cipher_text = self.fernet.encrypt(message)
        if len(cipher_text) >= 65536:
            raise Exception("message too big")
        self.conn.sendto(self.name.encode(), self.dest)
        self.conn.sendto(self.cipher_sssk, self.dest)
        self.conn.sendto(cipher_text, self.dest)