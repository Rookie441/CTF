import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from hashlib import sha512


with open("encrypted.txt", "r") as f:
    data = f.readlines()
    for line in data:
        if line.startswith("iv :"):
            iv = line.strip()[5:]
        elif line.startswith("ct :"):
            ct = line.strip()[5:]
        
f.close()
ct_bytes = bytes.fromhex(ct)

##decrypted = ""
### Bruteforcing the 3 bytes in os.urandom(20)[:3]
##for i in range(2**24):
##    if i % 100000 == 0:
##        print("counter is now", i)
##    rand_3bytes = i.to_bytes(3, byteorder='big')
##    # Hashing the 3 bytes obtained to get a 16 byte key
##    currKey = sha512(rand_3bytes).digest()[:16]
##    currCipher = AES.new(currKey, AES.MODE_CBC, bytes.fromhex(iv))
##    try:
##        decrypted = unpad(currCipher.decrypt(ct_bytes), AES.block_size)
##    except:
##        pass
##    if decrypted != "":
##        try:
##            print(i, decrypted.decode("utf-8"))
##            break
##        except:
##          pass

i = 6123409
rand_3bytes = i.to_bytes(3, byteorder='big')
currKey = sha512(rand_3bytes).digest()[:16]
currCipher = AES.new(currKey, AES.MODE_CBC, bytes.fromhex(iv))
decrypted = unpad(currCipher.decrypt(ct_bytes), AES.block_size)
print(decrypted.decode("utf-8"))


