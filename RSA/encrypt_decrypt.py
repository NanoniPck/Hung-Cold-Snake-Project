
# page. 4 RSA slide
# encrypt C = Memodn 
def encrypt(m : str, key : tuple[int, int]):
    e, n = key
    c = pow(m, e, n)
    return c 

# decrpyt M = C^d mod n
def decrypt(c : str, key : tuple[int, int]):
    d, n = key
    m = pow(c, d, n)
    return m 



