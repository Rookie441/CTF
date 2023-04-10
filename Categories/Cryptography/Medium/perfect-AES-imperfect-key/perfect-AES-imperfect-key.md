## Perfect AES Imperfect Key

[main.py](https://github.com/Rookie441/CTF/blob/main/Categories/Cryptography/Medium/perfect-AES-imperfect-key/main.py)  
[encrypted.txt](https://github.com/Rookie441/CTF/blob/main/Categories/Cryptography/Medium/perfect-AES-imperfect-key/encrypted.txt)

> The contents of main.py is as follows:

```python
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from hashlib import sha512

FLAG = <REDACTED>

key = sha512(os.urandom(20)[:3]).digest()[:16]
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(FLAG, AES.block_size))
iv, ct = cipher.iv, ct_bytes
print(f'iv : {iv.hex()}\nct : {ct.hex()}')
```

> Here, we can see that the FLAG is being encrypted using AES encryption in the CBC mode. The iv and ct values are being output to encrypted.txt which we have access to. However, to decrypt the ciphertext, we not only need the iv provided, but we would also need the key that was used during encryption.

```
key = sha512(os.urandom(20)[:3]).digest()[:16]
```

> The key used is vulnerable because the input to the SHA-512 hash function is only 3 random bytes (as denoted by the stripping [:3]), which means that there are only 2^24 possible inputs. Thus, we can adopt a bruteforce approach to find this specific 3 bytes which allows us to get the key and eventually decrypt the ciphertext.

> For the purpose of this challenge, we will just use the python libraries to help us in decryption. You can read more about AES-CBC encryption [here](https://www.educative.io/answers/what-is-cbc).

> The following is the solver script, which can be found in [decrypt.py](https://github.com/Rookie441/CTF/blob/main/Categories/Cryptography/Medium/perfect-AES-imperfect-key/decrypt.py).

```python
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from hashlib import sha512

# Extract iv and ct values from encrypted.txt
with open("encrypted.txt", "r") as f:
    data = f.readlines()
    for line in data:
        if line.startswith("iv :"):
            iv = line.strip()[5:]
        elif line.startswith("ct :"):
            ct = line.strip()[5:]

f.close()
ct_bytes = bytes.fromhex(ct)

# Bruteforcing the 3 bytes in os.urandom(20)[:3]
decrypted = ""
for i in range(2**24):
    if i % 100000 == 0:
        print("counter is now", i)
    rand_3bytes = i.to_bytes(3, byteorder='big')
    # Hashing the 3 bytes obtained to get a 16 byte key
    currKey = sha512(rand_3bytes).digest()[:16]
    currCipher = AES.new(currKey, AES.MODE_CBC, bytes.fromhex(iv))
    try:
        decrypted = unpad(currCipher.decrypt(ct_bytes), AES.block_size)
    except:
        pass
    if decrypted != "":
        try:
            print(i, decrypted.decode("utf-8"))
            break
        except:
          pass

```

> The output is as follows: (some parts are truncated)

```
counter is now 100000
...
...
counter is now 5000000
counter is now 6000000
6123409 CS2107{Alway5_us3_Ur@nd0m_f0r_r@nd0m_s33d}
```

> And we got the flag! To add on, now that we have the specific value of i, we can simply just hardcode it as follows to spit out the flag immediately.

```python
i = 6123409
rand_3bytes = i.to_bytes(3, byteorder='big')
currKey = sha512(rand_3bytes).digest()[:16]
currCipher = AES.new(currKey, AES.MODE_CBC, bytes.fromhex(iv))
decrypted = unpad(currCipher.decrypt(ct_bytes), AES.block_size)
print(decrypted.decode("utf-8"))
```

`CS2107{Alway5_us3_Ur@nd0m_f0r_r@nd0m_s33d}`
