# MERKware
*EECS3481 2020 Final Project*

> Don't get MERKed...

**This project is only for education and research purposes. Use at your own risk. Maintainers and contributors to this project are not liable for any outcome when using or modifying this software.**

## Algorithms 
Available cryptographic algorithms for encryption and decryption.

### Roadmap
- [x] RC4
- [x] XOR
- [x] AES
- [ ] BLOWFISH
- [ ] RSA
- [ ] ECC

### Future Extensions
To load your own configuration
- [ ] `merk.config.json`
- [ ] `auto` mode. Where you run the executable and in encrypts your files in that directory.
- [ ] Use the `Virus Total` API to automatically test AV bypass

## Installation
### Requirements
- Python 3.7+
- Conda Environment
- ```conda install pip```
- ```pip install -r requirements.txt```

### Build from source
1. Install requirements
2. Run ```python install.py```
3. Navigate to */dist* to find *MERK* 

### Releases
TODO


## Usage
### Command-line Flags
- ```--folder``` The folder that will be encrypted
- ```--type``` algorithm type selection 
- ```--secrets``` n-tuple input used for key secrets and other parameters
- ```--action``` encrypt or decrypt

### Example Commands

### To bypass AV:
- Pass the execuable `MERK` into 
`msfvenom -a x86_64 --platform linux -o MERK  -k -e x86/shikata_ga_nai -c 3 < MERK`


---
### Group Members
- [Eric Marcantonio](https://github.com/EricMarcantonio)
- [Moreka Kazemi](https://github.com/mowhamadrexa)
- [Kevin Suh](https://github.com/KevinSuh6433)
- [Reuben Ninan](https://github.com/ReubenMathew)
