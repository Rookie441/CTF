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