import socket, RSA
from cryptography.fernet import Fernet

class Sender:
    # initialize an encrypted chatroom sender
    def __init__(self, ip: str, port: int, recipient: str) -> None:
        self.dest = (ip, port)
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        name, d, n = RSA.get_private_config()
        self.name = name
        self.priv_key = (d, n)
        self.recipient_key = RSA.get_public_key(recipient)

    # sssk exchange S -> R: S, {{SSSK}PRs}PUr
    def __enter__(self): 
        self.conn.connect(self.dest)
        sssk = Fernet.generate_key()
        self.fernet = Fernet(sssk)
        cipher_sssk = RSA.encrypt(sssk, self.priv_key)
        cipher_sssk = RSA.encrypt(cipher_sssk, self.recipient_key)
        self.conn.sendall(self.name.encode())
        self.conn.sendall(cipher_sssk)
        return self

    def __exit__(self, t, v, tb): 
        self.conn.close()

    # encrypts and sends a message S -> R: S, {m}SSSK
    def send_message(self, message: bytes):
        cipher_text = self.fernet.encrypt(message)
        length = len(cipher_text)
        if length >= 65536:
            self.send_message(message[:len(message)//2])
            self.send_message(message[len(message)//2:])
            return
        self.conn.sendall(length.to_bytes(length=2))
        self.conn.sendall(cipher_text)