# MERKware
*EECS3481 2020 Final Project*

> Don't get MERKed...

**This project is only for education and research purposes. Use at your own risk. Maintainers and contributors to this project are not liable for any outcome when using or modifying this software.**

## Installation
### Download latest executable (Windows only)
Get the latest release [here](https://github.com/EricMarcantonio/EECS3481-Project/releases)
### Requirements
- Python 3.7+
- Conda Environment
- ```conda install pip```
- ```pip install -r requirements.txt```

### Build from source
1. Install requirements
2. Run ```python build.py```
3. Navigate to newly generated `/dist` to find `MERK.exe `

## Usage
See [USAGE.md](https://github.com/EricMarcantonio/EECS3481-Project/blob/master/USAGE.md) for more detailed documentation
### Command-line Flags
- ```--folder``` `-f` The folder that will be encrypted
- ```--type``` `-t` algorithm type selection 
- ```--secrets``` `-s` n-tuple input used for key secrets and other parameters
- ```--action``` `-a` encrypt or decrypt



## Algorithms 
Available cryptographic algorithms for encryption and decryption.

### Roadmap
- [x] RC4
- [x] XOR
- [x] AES
- [ ] BLOWFISH (coming soon...)
- [x] RSA
- [x] ECC

### Future Extensions
To load your own configuration
- [x] `merk.config.json`
- [ ] `auto` mode. Where you run the executable and in encrypts your files in that directory.
- [ ] Use the `Virus Total` API to automatically test AV bypass


---
### Group Members
- [Eric Marcantonio](https://github.com/EricMarcantonio)
- [Moreka Kazemi](https://github.com/mowhamadrexa)
- [Kevin Suh](https://github.com/KevinSuh6433)
- [Reuben Ninan](https://github.com/ReubenMathew)
