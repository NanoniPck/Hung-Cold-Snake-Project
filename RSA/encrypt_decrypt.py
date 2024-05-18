from math import ceil


# page. 4 RSA slide
# encrypt C = M^e mod n 
def encrypt(m : bytes, key : tuple[int, int]):
    e, n = key
    if len(m) > n.bit_length() // 8: 
        m1, m2 = m[:len(m)//2], m[len(m)//2:]
        c1 = encrypt(m1, key)
        c2 = encrypt(m2, key)
        return c1 + c2
    
    m = int.from_bytes(m)
    c: int = pow(m, e, n)
    return c.to_bytes(n.bit_length() // 8 + 1)

# decrpyt M = C^d mod n
def decrypt(c : bytes, key : tuple[int, int]):
    d, n = key

    if len(c) > n.bit_length() // 8 + 1: 
        c1, c2 = c[:len(c)//2], c[len(c)//2:]
        # TODO technically this is still wrong
        # I should solve this problem using padding instead of 
        # bytes-rounding
        m1 = decrypt(c1, key)
        m2 = decrypt(c2, key)
        return m1 + m2
    
    c = int.from_bytes(c)
    m: int = pow(c, d, n)
    return m.to_bytes(ceil(m.bit_length() / 8))
