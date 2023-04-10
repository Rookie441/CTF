## Insecure OTP

[main.py](https://github.com/Rookie441/CTF/blob/main/Categories/Cryptography/Medium/insecure-otp/main.py)  
[encrypted.txt](https://github.com/Rookie441/CTF/blob/main/Categories/Cryptography/Medium/insecure-otp/encrypted.txt)

> The output of main.py is as follows:

```python
import os

FLAG = <REDACTED>

# xor 2 byte strings
def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


def encrypt(msg) :
    otp = os.urandom(20)
    res = b""
    for i in range(0, len(msg), 20):
        res += xor(otp, msg[i:i+20])
    return res

msg = f"Hey Grandma Susan'oo, I have told you not to play with my Photoshop! \
Why did you crop your head on the dragon... {FLAG}".encode()

print("encrypted : " + encrypt(msg).hex())
```

> Here, we can see that the message is split into multiple sets of 20 bytes, each undergoing an [XOR encryption](https://en.wikipedia.org/wiki/XOR_cipher).

> The unique aspect of XOR encryption is that the decryption process is identical to the encryption process, and both use the same key.

```
Encryption ---> plaintext ^ key = ciphertext
Decryption ---> ciphertext ^ key = plaintext
```

> And to extend the above, using properties of XOR, we can deduce that `ciphertext ^ plaintext = key`. This will be useful in solving this challenge because we can note that encryption is done on every 20 bytes of the message (ciphertext), and we have the first 20 bytes of plaintext in the msg variable. Thus, we can perform the XOR encryption to obtain the key, which we will then use to decrypt the remaining set of 20 bytes, which includes the FLAG.

> The following is the exploit script, which can be found in [decrypt.py](https://github.com/Rookie441/CTF/blob/main/Categories/Cryptography/Medium/insecure-otp/decrypt.py).

```python
# Extract ciphertext from encrypted.txt
with open("encrypted.txt", "r") as f:
    full_ct_str = f.readline()[12:]
f.close()

FLAG = ""

msg = f"Hey Grandma Susan'oo, I have told you not to play with my Photoshop! \
Why did you crop your head on the dragon... {FLAG}".encode()

# xor 2 byte strings
def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

full_ct = bytes.fromhex(full_ct_str) #In bytes. Same as binascii.unhexlify()

# key = ciphertext ^ plaintext
otp = xor(full_ct[:20],msg[:20])

# plaintext = ciphertext ^ key
flag = ""
for i in range(0, len(full_ct), 20):
    ct = full_ct[i:20+i] # Get the next set of 20 bytes
    flag += xor(ct,otp).decode("utf-8")

print(flag)
```

`CS2107{OTPOTP_0tp0tp_R3p3at_k3y_15_vuln3rable}`
