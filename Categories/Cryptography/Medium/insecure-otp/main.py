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