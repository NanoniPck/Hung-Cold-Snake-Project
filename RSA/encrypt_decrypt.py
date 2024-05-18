from math import ceil


# page. 4 RSA slide
# encrypt C = M^e mod n 
def encrypt(m : bytes, key : tuple[int, int]):
    e, n = key
    block_size = n.bit_length() // 8
    cipher_size = n.bit_length() // 8 + 1

    if len(m) >= block_size: 
        m1, m2 = m[:len(m)//2], m[len(m)//2:]
        c1 = encrypt(m1, key)
        c2 = encrypt(m2, key)
        return c1 + c2
    
    m += b'1' + b'0' * (block_size - len(m) - 1)
    m = int.from_bytes(m)
    c: int = pow(m, e, n)
    return c.to_bytes(cipher_size)

# decrpyt M = C^d mod n
def decrypt(c : bytes, key : tuple[int, int]):
    d, n = key
    block_size = n.bit_length() // 8
    cipher_size = n.bit_length() // 8 + 1

    if len(c) > cipher_size: 
        c1, c2 = c[:len(c)//2], c[len(c)//2:]
        m1 = decrypt(c1, key)
        m2 = decrypt(c2, key)
        return m1 + m2
    
    c = int.from_bytes(c)
    m: int = pow(c, d, n)
    return m.to_bytes(block_size).rsplit(b'1', 1)[0]
