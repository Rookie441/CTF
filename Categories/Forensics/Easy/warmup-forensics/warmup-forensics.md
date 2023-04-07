## Warmup Forensics

[broken](https://github.com/Rookie441/CTF/blob/main/Categories/Forensics/Easy/warmup-forensics/broken)  

> We are given a strange file. Opening it in a hex editor, we can see that it has the header `Standcon22`  

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Forensics/Easy/warmup-forensics/StandconHeader.png)  

> In addition, there are also `IHDR` and `IDAT` which suggests that it could have been a png. Thus, we modify the header from Standcon22 to the file signature of a png header `89 50 4e 47 0d 0a 1a 0a`  

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Forensics/Easy/warmup-forensics/PngHeader.png)  

> After saving it as png and trying to open using the Linux eog command, we are faced with a CRC error.  

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Forensics/Easy/warmup-forensics/CRCerror.png)  

> We can breakdown the IHDR chunk as follows:

```
89 50 4e 47 0d 0a 1a 0a: File signature of png.
00 00 00 0d: IHDR length.
49 48 44 52: Chunk type, which in this case specifies IHDR.
00 00 00 00: Width
00 00 00 00: Height
08: Bit depth.
06: Colour type.
00: Compression type.
00: Filter type.
00: Interval type.
e8 d3 c1 43: CRC checksum.
```

> Now that we know  the image dimensions are invalid, we can choose to either bruteforce the width and height or to make use of the CRC checksum to obtain the correct dimension values. We shall adopt the latter approach.

> We can write a python script that keeps searching until the calculated crc checksum of the IHDR checksum matches our target checksum and if so, prints the dimensions that meet this criteria. The following script is taken from [this similar writeup](http://society.cyber.warwick.ac.uk/intakectfmissingbytes/), but the crc value is modified to `0xe8d3c143` to match our example.

```python
from zlib import crc32
data = open("broken.png",'rb').read()
index = 12

ihdr = bytearray(data[index:index+17]) #ihdr
width_index = 7 #width
height_index = 11 #height

for x in range (1,2000):
    height = bytearray(x.to_bytes(2,'big'))
    for y in range(1,2000):
        width = bytearray(y.to_bytes(2,'big'))
        for h in range(len(height)):
            ihdr[height_index - h] = height[-h -1]
        for w in range(len(width)):
            ihdr[width_index - w] = width[-w -1]
        if hex(crc32(ihdr)) == '0xe8d3c143': #crc
            print("width: {} height: {}".format(width.hex(),height.hex()))
        for i in range(len(width)):
            ihdr[width_index - i] = bytearray(b'\x00')[0]
```

> The output is as follows:

```
width: 0780 height: 0438
```

> Now, apply these new values to the broken.png file using a hexeditor, we get the following:

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Forensics/Easy/warmup-forensics/FixedHeader.png)  

> We are now able to open the png file to get the flag.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Forensics/Easy/warmup-forensics/fixed.png)    

> This challenge was first blooded by me during the event.  

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Forensics/Easy/warmup-forensics/FirstBlood.png)   

`STANDCON22{W@RMUP_lia00000}`
