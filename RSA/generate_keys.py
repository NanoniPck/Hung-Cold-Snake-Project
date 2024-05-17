import random 

# Miller-Rabin primality test using 15 iterations
def is_probably_prime(n, iter = 15) -> bool:
	r, s = 0, n - 1
	while s % 2 == 0:
		r += 1
		s //= 2
	for _ in range(iter):
		a = random.randrange(2, n - 1)
		x = pow(a, s, n)
		if x == 1 or x == n - 1: continue
		for _ in range(r - 1):
			x = pow(x, 2, n)
			if x == n - 1: break
		else: return False
	return True

def generate_random_primenumber(size: int) -> int:
    random_odd = random.randint(2**size, 2**(2*size))
    
    if (random_odd % 2 == 0):
        random_odd += 1

    while True:
        if is_probably_prime(random_odd):
            return random_odd
        else:
            random_odd += 2


def generate_key(size: int = 1024, e: int = 65537) -> tuple[int, int, int]:
    # 1 Privately choose two prime numbers p, q. These two numbers are
    p = generate_random_primenumber(size / 2)
    q = generate_random_primenumber(size / 2)

    # 2 Calculate n = pq. n is made public
    n = p*q

    # 3 Choose e < φ(n) such that gcd(e, φ(n)) = 1. e is public
    # GRAPS: e is providede in the argument as a default 65537

    # 4 Privately calculate d ≡ e−1mod φ(n). d is kept secret. -> φ(pq) = φ(p) ∗ φ(q) = (p − 1)(q − 1)
    d = pow(e, -1, (p-1)*(q-1)) 
    return (e, d, n) 

    

