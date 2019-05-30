from __future__ import unicode_literals
import socket
from math import sqrt
import random
from random import randint as rand
import pickle

host = socket.gethostname()
port = 5000

s = socket.socket()
s.connect((host, port))


def encrypt(msg_plaintext, package):
    #unpack key value pair
    e, n = package
    msg_ciphertext = [pow(ord(c), e, n) for c in msg_plaintext]
    return msg_ciphertext

e = int(s.recv(1024).decode())
n = int(s.recv(1024).decode())

public = (e, n)

print("Public Key: ",public)

message = input(" -> ")
encrypted_msg = encrypt(message, public)
#encoded_message = ''.join(map(lambda x: str(x), encrypted_msg))
encoded_data = pickle.dumps(encrypted_msg)
while True:
    s.send(encoded_data)
    message = input(" -> ")
    encrypted_msg = encrypt(message, public)
    #encoded_message = ''.join(map(lambda x: str(x), encrypted_msg))
    encoded_data = pickle.dumps(encrypted_msg)
s.close()
