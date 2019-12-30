[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

# RSA_cryptography

This project is in collaboration with [Awnon Bhowmik](https://github.com/awnonbhowmik)

### Code Sample

```python
>>> import RSA_module

>>> bit_length = int(input("Enter bit_length: "))
Enter bit_length: 4

>>> public, private = RSA_module.generate_keypair(2**bit_length)
467 137

>>> msg = input("Write msg: ")
Write msg: 7enTropy7

>>> encrypted_msg, encryption_obj = RSA_module.encrypt(msg, public)

>>> print("Encrypted msg: " + encrypted_msg)
Encrypted msg: 1283254245233922667063899175674025153412832

>>> decrypted_msg = RSA_module.decrypt(encryption_obj, private)

>>> print("Decrypted msg: " + decrypted_msg)
Decrypted msg: 7enTropy7 
```


![Screenshot from 2019-05-31 04-10-03](https://user-images.githubusercontent.com/36446402/58669503-15599b00-835a-11e9-8dee-2eebd99b79b3.png)



We have implemented a highly secure RSA cryptography algorithm in a server-client socket framework. The client's messages are encrypted on their local machine using a public key and the encrypted data flows to the server where it is decrypted using the generated private key. 

This is a practical demonstration of the algorithm where every time a socket connection is set up, a new set of pubic,private keys are generated. 

The bitlength can be adjusted in the code for desired level of security.

This code can be used to save your passwords or other confedential data remotely to a server without any worries of it getting hacked.

## Authors

* [**Unnikrishnan Menon**](https://github.com/7enTropy7)
* [**Awnon Bhowmik**](https://github.com/awnonbhowmik)
