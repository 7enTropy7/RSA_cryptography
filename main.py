import RSA_module
import time

bit_length = int(input("Enter Key Bit Length: "))

public, private = RSA_module.generate_keypair(bit_length)

msg = input("Write msg: ")

t1 = time.time()
encrypted_msg = RSA_module.encrypt(msg, public)
print("Encrypted msg: " + str(encrypted_msg))

decrypted_msg = RSA_module.decrypt(encrypted_msg, private)
print("Decrypted msg: " + str(decrypted_msg))
print('Runtime : ' + str(time.time()-t1) + ' seconds')