# RSA_cryptography

This project is in collaboration with [Awnon Bhowmik](https://github.com/awnonbhowmik)


![Screenshot from 2019-05-31 04-10-03](https://user-images.githubusercontent.com/36446402/58669503-15599b00-835a-11e9-8dee-2eebd99b79b3.png)



We have implemented a highly secure RSA cryptography algorithm in a server-client socket framework. The client's messages are encrypted on their local machine using a public key and the encrypted data flows to the server where it is decrypted using the generated private key. 

This is a practical demonstration of the algorithm where every time a socket connection is set up, a new set of pubic,private keys are generated. 

The bitlength can be adjusted in the code for desired level of security.

This code can be used to save your passwords or other confedential data remotely to a server without any worries of it getting hacked.
