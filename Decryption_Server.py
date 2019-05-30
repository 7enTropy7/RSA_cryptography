from __future__ import unicode_literals
import socket
from math import sqrt
import random
from random import randint as rand
import pickle


host = socket.gethostname()
port = 5000

s = socket.socket()
s.bind((host, port))
s.listen(2)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return -1


def isprime(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
    return True


#initial two random numbers p,q
p = rand(1, 1000)
q = rand(1, 1000)


def generate_keypair(p, q,keysize):
    # keysize is the bit length of n so it must be in range(nMin,nMax+1).
    # << is bitwise operator
    # x << y is same as multiplying x by 2**y
    # i am doing this so that p and q values have similar bit-length.
    # this will generate an n value that's hard to factorize into p and q.


    nMin = 1<<(keysize-1)
    nMax = (1<<keysize) - 1
    primes=[2]
    # we choose two prime numbers in range(start, stop) so that the difference of bit lengths is at most 2.
    start = 1<<(keysize//2-1)
    stop = 1<<(keysize//2+1)

    if start >= stop:
        return []

    for i in range(3, stop + 1, 2):
        for p in primes:
            if i % p == 0:
                break
        else:
            primes.append(i)

    while(primes and primes[0] < start):
        del primes[0]

    #choosing p and q from the generated prime numbers.
    while primes:
        p = random.choice(primes)
        primes.remove(p)
        q_values = [q for q in primes if nMin <= p * q <= nMax]
        if q_values:
            q = random.choice(q_values)
            break

    n = p * q
    phi = (p - 1) * (q - 1)

    #generate public key 1<e<phi(n)
    e = random.randrange(1, phi)
    g = gcd(e, phi)

    #as long as gcd(1,phi(n)) is not 1, keep generating e
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #generate private key
    d = mod_inverse(e, phi)

    #public key (e,n)
    #private key (d,n)

    return ((e, n), (d, n))

def decrypt(msg_ciphertext, package):
    d, n = package
    msg_plaintext = [chr(pow(c, d, n)) for c in msg_ciphertext]
    # No need to use ord() since c is now a number
    # After decryption, we cast it back to character
    # to be joined in a string for the final result
    return (''.join(msg_plaintext))

public, private = generate_keypair(p, q, 8)


print(host)
conn, address = s.accept()
print("Connected to: " + str(address))


conn.send(str(public[0]).encode())
conn.send(str(public[1]).encode())
print("Public Key: ",public)

while True:
    encoded_data = pickle.loads(conn.recv(1024*4))
    for i in range(len(encoded_data)):
        encoded_data[i]=int(encoded_data[i])
    if not encoded_data:
        break
    #print(''.join(map(lambda x: str(x), encoded_data)))
    decoded_data = decrypt(encoded_data, private)
    print("Client : " + str(decoded_data))
conn.close()