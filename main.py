from Crypto.Util import number

p = number.getPrime(1024)
q = number.getPrime(1024)
N = p * q
phi_N = (p - 1) * (q - 1)
e = 65537
d = pow(e, -1, phi_N)

# Private key would be (d,N)     And Public key would be (e,N)

plaintext = number.bytes_to_long(b"This is a secret message")
print("Plaintext: ", plaintext)

encrypted = pow(plaintext, e, N)
print("Ciphertext: ", encrypted)

decrypted = pow(encrypted, d, N)
print("Decrypted: ", decrypted)
