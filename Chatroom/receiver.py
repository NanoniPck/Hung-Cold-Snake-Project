import socket, RSA
from cryptography.fernet import Fernet

class Receiver:
    # initialize an encrypted TCP chatroom receiver
    def __init__(self, ip: str, port: int) -> None:
        self.host = (ip, port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(self.host)
        name, d, n = RSA.get_private_config()
        self.name = name
        self.priv_key = (d, n)

    # receive sssk exchange
    def __enter__(self): 
        self.sock.listen()
        self.conn, _ = self.sock.accept()
        self.sender = self.conn.recv(1024).decode()
        cipher_sssk = self.conn.recv(1024)
        sender_key = RSA.get_public_key(self.sender)
        cipher_sssk = RSA.decrypt(cipher_sssk, self.priv_key)
        sssk = RSA.decrypt(cipher_sssk, sender_key)
        self.fernet = Fernet(sssk)
        return self

    def __exit__(self, t, v, tb): self.conn.close()

    # receive and decryptes message
    def get_message(self) -> bytes:
        size = int.from_bytes(self.conn.recv(2))
        cipher_text = self.conn.recv(size)
        try: message = self.fernet.decrypt(cipher_text)
        except ValueError: raise Exception('Cannot decrypt; message compromised')
        return message


