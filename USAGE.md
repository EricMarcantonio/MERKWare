# Usage
## RC4
### Encryption
```.\MERK.exe -f ./spec/test_folder -a encrypt -t rc4 -s 12345```
### Decryption
```.\MERK.exe -f ./spec/test_folder.zip.merk -a decrypt -t rc4 -s 12345```

## AES
### Encryption
```.\MERK.exe -f ./spec/test_folder -a encrypt -t aes -s 12345```
### Decryption
```.\MERK.exe -f ./spec/test_folder.zip.merk -a decrypt -t aes -s 12345```

## XOR
### Encryption
```.\MERK.exe -f ./spec/test_folder -a encrypt -t xor -s 12345```
### Decryption
```.\MERK.exe -f ./spec/test_folder.zip.merk -a decrypt -t xor -s 12345```

