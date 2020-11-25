# Usage

## Commandline Arguments
### RC4
#### Encryption
```MERK.exe -f <target folder/file> -a encrypt -t rc4 -s <key>```
#### Decryption
```MERK.exe -f <target folder/file> -a decrypt -t rc4 -s <key>```

### AES
#### Encryption
```MERK.exe -f <target folder/file> -a encrypt -t aes -s <key>```
#### Decryption
```MERK.exe -f <target folder/file> -a decrypt -t aes -s <key>```

### XOR
#### Encryption
```MERK.exe -f <target folder/file> -a encrypt -t xor -s <key>```
#### Decryption
```MERK.exe -f <target folder/file> -a decrypt -t xor -s <key>```

### RSA
#### Encryption
```MERK.exe -f <target folder/file> -a encrypt -t rsa -s <key_file_name>```
#### Decryption
```MERK.exe -f <target folder/file> -a decrypt -t rsa -s <key_file_name>```

### ECC
#### Elliptic Curve Options
- brainpoolP160r1
- brainpoolP192r1
- brainpoolP224r1
- brainpoolP256r1
- brainpoolP320r1
- brainpoolP384r1
- brainpoolP512r1
- secp192r1
- secp224r1
- secp256r1
- secp384r1
- secp521r1
#### Encryption
```MERK.exe -f <target folder/file> -a encrypt -t ecc -s <elliptic curve>```
#### Decryption
```MERK.exe -f <target folder/file> -a decrypt -t ecc -s <elliptic curve>```


---

## Config file usage
```.\MERK.exe -c <path_to_config_file> ```
