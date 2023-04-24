import io
import base64
from PIL import Image
    
def bbb(d, k):
    length1 = len(d)
    length2 = len(k)
    numArray = bytearray(length1)
    for index in range(length1):
        numArray[index] = d[index] ^ ord(k[index % length2])
    return bytes(numArray)

def cc():
    k = ""
    for num in range(1, 11):
        filename = f"RabbitHole.Resources.{num}.txt"
        with open(filename, "r") as f:
            content = f.read()
        startIndex = num * 5 * 7 // 9
        k += content[startIndex:startIndex+4]
    return k

with open("RabbitHole.Resources.aa.txt", "rb") as f:
    encrypted_data = base64.b64decode(f.read())
    
decrypted_data = bbb(encrypted_data, cc())

img_stream = io.BytesIO(decrypted_data)
image = Image.open(img_stream)
image.show()
image.save("flag.png")


