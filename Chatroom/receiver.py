import socket, RSA

class Receiver:
    # initialize an encrypted TCP chatroom receiver
    def __init__(self, ip: str, port: int, key: tuple[int, int]) -> None:
        self.host = (ip, port)
        self.key = key

    # creates a receiver server, waits for client connection, and exchange keys
    def __enter__(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(self.host)
        sock.listen()
        self.conn, self.addr = sock.accept()
        _, modulus = self.key
        self.conn.sendall(modulus.to_bytes(modulus.bit_length()))
        return self
    
    # once the receiver is exited, close connection
    def __exit__(self):
        self.conn.close()

    # try getting some data, if so decrypts
    def get_message(self) -> str:
        try: data = self.conn.recv(1024)
        except ConnectionError: return None
        if not data:            return None
        return RSA.decrypt(data, self.key)


