import socket, RSA

class Sender:
    # initialize an encrypted chatroom sender
    def __init__(self, ip: str, port: int, e: int = 65537) -> None:
        self.dest = (ip, port)

    # connects to a chatroom receiver, receive key exchange, and awaits send
    def __enter__(self):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect(self.dest)
        modulus = int.from_bytes(self.conn.recv(1024))
        self.key = (65537, modulus)
        return self
    
    # once the receiver is exited, close connection
    def __exit__(self, e_type, e_val, traceback):
        self.conn.close()

    # encrypts and sends a message
    def send_message(self, message: str):
        cipher_text = RSA.encrypt(message, self.key)
        self.conn.sendall(cipher_text)