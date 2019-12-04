import RSA_module

bit_length = int(input("Enter bit_length: "))

public, private = RSA_module.generate_keypair(2**bit_length)

msg = input("Write msg: ")
encrypted_msg, encryption_obj = RSA_module.encrypt(msg, public)
print("Encrypted msg: " + encrypted_msg)

decrypted_msg = RSA_module.decrypt(encryption_obj, private)
print("Decrypted msg: " + decrypted_msg)
