
# page. 4 RSA slide
# encrypt C = Memodn 
def encrypt(m : str, key : tuple[int, int]):
    m = int.from_bytes(m.encode())
    e, n = key
    c: int = pow(m, e, n)
    return c.to_bytes(c.bit_length() // 8 + 1)

# decrpyt M = C^d mod n
def decrypt(c : bytes, key : tuple[int, int]):
    d, n = key
    c = int.from_bytes(c)
    m: int = pow(c, d, n)
    return m.to_bytes(m.bit_length() // 8 + 1).decode()



