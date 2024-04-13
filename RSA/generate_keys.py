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

print(generate_random_primenumber(1024))
