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

    def __enter__(self): return self
    def __exit__(self, t, v, tb): self.conn.close()

    # encrypts and sends a message
    def send_message(self, message: bytes):
        # TODO: S -> R: S, {{SSSK}PRs}PUr, {m}SSSK
        sssk = Fernet.generate_key()
        cipher_text = Fernet(sssk).encrypt(message)
        cipher_sssk = RSA.encrypt(sssk, self.priv_key)
        cipher_sssk = RSA.encrypt(cipher_sssk, self.recipient_key)
        self.conn.sendto(self.name.encode(), self.dest)
        self.conn.sendto(cipher_sssk, self.dest)
        self.conn.sendto(cipher_text, self.dest)