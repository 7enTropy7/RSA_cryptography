[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.6](https://img.shields.io/badge/python-3.6-teal.svg)](https://www.python.org/downloads/release/python-360/) [![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Unnikrishnan-blue.svg)](https://www.linkedin.com/in/unnikrishnan-menon-aa013415a/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) [![GitHub followers](https://img.shields.io/github/followers/7enTropy7?label=Follow&style=social)](https://github.com/7enTropy7?tab=followers) [![GitHub stars](https://img.shields.io/github/stars/7enTropy7/RSA_cryptography.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/7enTropy7/RSA_cryptography/stargazers/)


# RSA_cryptography

Created in collaboration with [Awnon Bhowmik](https://github.com/awnonbhowmik)

A highly secure RSA encryption algorithm in a server-client socket framework. The client's messages are encrypted on their local machine using a public key and the encrypted data flows to the server where it is decrypted using the generated private key. This code can be used to save your passwords or other confedential data remotely to a server without any worries of it getting hacked.

This is a practical demonstration of the algorithm where every time a socket connection is set up, a new set of pubic,private keys are generated. 

The bitlength can be adjusted in the code for desired level of security.

### Cloning
```bash
$ git clone https://github.com/7enTropy7/RSA_cryptography.git
```

### Code Sample

```python
>>> import RSA_module
>>> bit_length = int(input("Enter Key Bit Length: "))
Enter Key Bit Length: 1024
>>> public, private = RSA_module.generate_keypair(bit_length)
>>> message = input("Enter Message: ")
Enter Message: 7enTropy7
>>> encrypted_message = RSA_module.encrypt(message, public)
>>> print("Encrypted Message: " + str(encrypted_message))
Encrypted Message: 15265520901766789045681821545868814376034703004383283443858782335831692583624841127618802095957607414846339799319016643181426238377954590430133852776014166473337703808061712357365793532850449253596609746717723715826478629963238513449654688284273913580466488150526170074492903279628975500904790880507264769413812987862364065420843896587486170279995843645589072737241019492706185515894078178687579161346045505997146456404050994229530060933825840964628721270923724893699880274492327619878941454150688381245180274990914412874752642685781597650532546075691196520692434858059474375046663710136885218137715696877410011081033
>>> decrypted_message = RSA_module.decrypt(encrypted_message, private)
>>> print("Decrypted Message: " + str(decrypted_message))
Decrypted Message: 7enTropy7 
```

## Demo

![ezgif com-video-to-gif](https://user-images.githubusercontent.com/36446402/85234950-d13aac00-b42e-11ea-9f17-4308a2382c35.gif)


## Authors
[![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Unnikrishnan-green.svg)](https://www.linkedin.com/in/unnikrishnan-menon-aa013415a/) [![LinkedIn-profile](https://img.shields.io/badge/LinkedIn-Awnon-orange.svg)](https://www.linkedin.com/in/awnon-bhowmik-13a5a013b/?miniProfileUrn=urn%3Ali%3Afs_miniProfile%3AACoAACIUlr4BQG5MmK7AYfJbU5Zaacunw1qLanM)
* [**Awnon Bhowmik**](https://github.com/awnonbhowmik)
* [**Unnikrishnan Menon**](https://github.com/7enTropy7)


## License

[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

