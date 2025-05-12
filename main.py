from Crypto.Util import number
from Crypto.PublicKey import RSA


def next_prime(p):
    candidate = p + 1
    while not number.isPrime(candidate):
        candidate += 1
    return candidate


p = number.getPrime(1024)
q = next_prime(p)
print(p)
print(q)

N = p * q
phi_N = (p - 1) * (q - 1)
e = 65537
d = pow(e, -1, phi_N)

# Private key would be (d,N)     And Public key would be (e,N)

key = RSA.construct((N, e, d, p, q))

pub_key = key.publickey()
pub_pem = pub_key.export_key(format="PEM")
print(pub_pem.decode())

plaintext = number.bytes_to_long(
    b"IF you found the answer pm me something funny about flying cows :) Blah Blah Blaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
)
print("Plaintext: ", plaintext)

encrypted = pow(plaintext, e, N)
print("Ciphertext: ", encrypted)

decrypted = pow(encrypted, d, N)
print("Decrypted: ", decrypted)
