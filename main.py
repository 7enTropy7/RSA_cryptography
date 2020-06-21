import RSA_module
import time

bit_length = int(input("Enter Key Bit Length: "))

public, private = RSA_module.generate_keypair(bit_length)

message = input("Enter Message: ")

t1 = time.time()
encrypted_message = RSA_module.encrypt(message, public)
print("Encrypted Message: " + str(encrypted_message))

decrypted_message = RSA_module.decrypt(encrypted_message, private)
print("Decrypted Message: " + str(decrypted_message))
print('Runtime : ' + str(time.time()-t1) + ' seconds')