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

