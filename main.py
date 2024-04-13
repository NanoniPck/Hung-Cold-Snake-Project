import RSA

public_key, private_key = RSA.generate_key(1024)
m = "Gappi good cat"
encrypted = RSA.encrypt(m, public_key)
decrypted = RSA.decrypt(encrypted, private_key)

print(m, decrypted)

