# [TamilCTF2021](https://ctftime.org/event/1440)

<img align="left" width="200" height="175" src="https://user-images.githubusercontent.com/68913871/134906440-561c8c58-7cf2-4caa-aa7e-b01997b16146.png">

&nbsp; 48 hours Jeopardy-Style  
&nbsp; Sun, 26 Sept. 2021, 21:00 SGT — Tue, 28 Sept. 2021, 21:00 SGT

&nbsp; **Team Name:** *Rookie441*  
&nbsp; **Team Member(s):**  
&nbsp; 1. *Andre Lee*  

<br/><br>

| Challenge | Category |
| --- | --- |
| [Terrapin](#terrapin)	| Misc |
| [Chat with me](#chat-with-me)	| Forensic |
| [Digital play](#digital-play) | Reversing |
| [Obscure](#obscure) | Reversing |

## Terrapin

![image](https://user-images.githubusercontent.com/68913871/135071916-5fabd4f4-36b2-4b9f-ab4e-ca60754830d7.png)  
[Terrapin.pdf](https://github.com/Rookie441/CTF/files/7243169/Terrapin.pdf)

> The contents of the file is as follows:

```
Terrapin
Note: What's the challenge's name?
▷ btw I love snakes
▷ F means Forward
▷ R means ?
▷ L means?
▷ PU means Penup
▷ PD means?
▷ C means cricle
▷ Do you know one thing? Pastebin is cool
Some INSTRUCTIONS
Terrapin code
PU,L(180),F(300),PD,R(90),F(50),R(90),F(20),R(180),C(12,-180),R(
180),F(20),R(180),F(20),R(180),C(12,-180),R(180),F(20),PU,R(180)
,F(50),L(90),PD,F(50),R(90),F(30),R(180),F(30),L(90),F(20),L(90)
,F(20),PU,F(20),L(90),PD,F(20),R(90),F(20),R(180),C(10,-180),R(1
80),F(20),L(90),F(30),R(180),F(30),R(135),F(45),L(45),PU,F(20),P
D,L(90),F(30),L(180),F(15),L(45),F(25),L(180),F(25),R(90),F(25),
PU,R(45),F(10),PD,L(90),F(20),R(90),F(30),L(180),F(30),L(90),F(3
5),C(17,-270),R(180),F(17),PU,R(180),F(50),L(90),PD,F(35),R(180)
,F(12),C(11,-180),R(180),F(30),PU,L(90),F(30),PD,C(30,170),C(20,
360),PU,L(188),F(30),R(47),PD,F(35),L(98),F(35),L(180),F(35),L(4
2),F(30)
▷ Be smart :)
```

> Challenge name is `Terrapin` which is a turtle. Other keywords `Forward` and `Penup` suggests the use of [python turtle graphics](https://docs.python.org/3/library/turtle.html).

> We define our drawing functions according to hints given in the file. Then, run the Terrapin code by calling the created functions. Note: We can use notepad++ to replace PU with PU() and PD with PD()

```python
import turtle

def F(dist):
    turtle.forward(dist)
def R(degree):
    turtle.right(degree)
def L(degree):
    turtle.left(degree)
def PU():
    turtle.penup()
def PD():
    turtle.pendown()
def C(a,b):
    turtle.circle(a,b)

#Draw    
PU(),L(180),F(300),PD(),R(90),F(50),R(90),F(20),R(180),C(12,-180),R(180),F(20),R(180),F(20),R(180),C(12,-180),R(180),F(20),PU(),R(180),F(50),L(90),PD(),F(50),R(90),F(30),R(180),F(30),L(90),F(20),L(90),F(20),PU(),F(20),L(90),PD(),F(20),R(90),F(20),R(180),C(10,-180),R(180),F(20),L(90),F(30),R(180),F(30),R(135),F(45),L(45),PU(),F(20),PD(),L(90),F(30),L(180),F(15),L(45),F(25),L(180),F(25),R(90),F(25),PU(),R(45),F(10),PD(),L(90),F(20),R(90),F(30),L(180),F(30),L(90),F(35),C(17,-270),R(180),F(17),PU(),R(180),F(50),L(90),PD(),F(35),R(180),F(12),C(11,-180),R(180),F(30),PU(),L(90),F(30),PD(),C(30,170),C(20,360),PU(),L(188),F(30),R(47),PD,F(35),L(98),F(35),L(180),F(35),L(42),F(30)
```

> The output from python turtle graphics:

![image](https://user-images.githubusercontent.com/68913871/135071980-6d3eec15-8de5-41e3-b00c-18a54a91a1b8.png)

> The .pdf file hinted "Do you know one thing? Pastebin is cool". Thus, append `BFRk5n9Y` to pastebin link to get the flag: https://pastebin.com/BFRk5n9Y

![image](https://user-images.githubusercontent.com/68913871/135072380-33cd086d-6b2f-4f59-beee-5ab15f9deb4a.png)

`TamilCTF{7urtl3s_4r3_veRrrRyy_sl0ww}`

## Chat with me

![image](https://user-images.githubusercontent.com/68913871/134907906-5b6ca8d1-3f78-47f4-9b50-df80aa6bd6f3.png)  
[chatwithme.zip](https://github.com/Rookie441/CTF/files/7236195/chatwithme.zip)

> Unzip and explore the files and directories. `hiddddddeeennnnn_properlyyy.obb` seems interesting, it has a PK header suggesting it is a zip file. Embedded is a `get_password.py` file.

![image](https://user-images.githubusercontent.com/68913871/134907966-8d1005a8-b8e1-4eb6-81fc-dc97744b30c1.png)

> Change file extention from .obb to .zip and unzip

![image](https://user-images.githubusercontent.com/68913871/134907978-689121ef-5f3e-4301-92b6-d5d9a928c97c.png)

> We are blocked with a password. Try to crack it using [fcrackzip](https://mattcasmith.net/2020/09/12/cracking-password-protected-zip-file-fcrackzip) and the rockyou.txt dictionary.

![image](https://user-images.githubusercontent.com/68913871/134907990-83c98470-524f-483c-9134-5d2295a3a86b.png)

> Password is `samantha.` Proceed to unzip with the known password and cat the embedded python file.

![image](https://user-images.githubusercontent.com/68913871/134907997-2ec5b699-5df8-4dc8-b6ca-f4ab3e153972.png)

> We get another password: `p4assW0rd_1s_n0t_s3cur333`

> In our initial exploration, there is also a `whatsapp.zip.cpt` file which was interesting. The .cpt extention implies that the zip file has been encrypted using [ccrypt](https://en.wikipedia.org/wiki/Ccrypt). The file can be decrypted in Linux using ccrypt as shown [here](https://www.geeksforgeeks.org/encrypt-decrypt-files-in-linux-using-ccrypt/). Here, the decryption key used is the password we obtained earlier: `p4assW0rd_1s_n0t_s3cur333`.

![image](https://user-images.githubusercontent.com/68913871/134908020-77ba5935-50db-41f6-bf6c-15ede42e43df.png)

> Unzipping the file, we found an interesting file `STK-20210804-WA0136.webp` which has been showing up in the Whatsapp chat logs.

> Open the file in a hex editor and we can see some interesting texts at the end of the file.

![image](https://user-images.githubusercontent.com/68913871/134908077-8df02f13-9114-4ab8-b2ae-bd040bc269ef.png)

```
{"sticker-pack-id":"com.snowcorp.stickerly.android.stickercontentprovider 5661e2d0-bfcd-40e6-8fed-7f91e43735c5","sticker-pack-link":"https://sticker.ly/s/<sticker-pack-code>","sticker-pack-code":"3HCM91","sticker-pack-publisher":"Sticker.ly * jopraveen","android-app-store-link":"https:\/\/play.google.com\/store\/apps\/details?id=com.snowcorp.stickerly.android","ios-app-store-link":"https:\/\/itunes.apple.com\/app\/id1458740001?mt=8"}
```

> Append the sticker-pack-code `3HCM91` to the link, we get https://sticker.ly/s/3HCM91, which brings us to this page:

![image](https://user-images.githubusercontent.com/68913871/134908100-7ca41d0b-d3b8-4f89-bec8-b07be50c4af3.png)

> The flag looks truncated, but upon inspecting elements, we can see the full flag.

![image](https://user-images.githubusercontent.com/68913871/134908117-3680d3d1-cc30-4918-a808-daee63189b64.png)

`TamilCTF{7h4ts_4_n1c3_st1ck3r}`

## Digital play

![image](https://user-images.githubusercontent.com/68913871/134917337-78dfe6bb-78d0-4514-a8cb-563e84945340.png)  
[digital_play.zip](https://github.com/Rookie441/CTF/files/7236565/digital_play.zip)

> Open the .dig file using [Digital](https://github.com/hneemann/Digital/releases/latest/download/Digital.zip). Clone the repo and run command `java -jar Digital.jar`

> Here, we can see the key to be `0x4d415253` as well as a circuit diagram of 9 XOR gates and 5 NOT gates

![image](https://user-images.githubusercontent.com/68913871/134917360-a172ec26-1bea-4495-a980-1a1d8429fdff.png)

> The enc.txt file is in binary format, so we will need to convert them to hex and `XOR` it with the key. Before that, we need to `NOT` Ciph 1,3,5,7,9 which are the odd Ciphs.

```
00110110111111100000011000101 100001000000100000011000010101 001001111110101001110011001011 1111100000101010000110100010000 011011111011001110111011011001 1111100000101010110011100001100 010011111011001100100011110011 1100001101100001011101100110 0000010111100111100100011010001
```

> This is the code to `NOT` the odd Ciphs and convert to hex format:

```python
enc = ["00110110111111100000011000101","100001000000100000011000010101","001001111110101001110011001011","1111100000101010000110100010000","011011111011001110111011011001","1111100000101010110011100001100","010011111011001100100011110011","1100001101100001011101100110","0000010111100111100100011010001"]

def flip(text):
    binstring = ""
    for i in text:
        if i == "1":
            binstring+="0"
        elif i == "0":
            binstring+="1"
    return binstring

#flip 1,3,5,7,9
enc_new = []
for i in range(len(enc)):
    if i%2 == 0:
        enc_new.append(flip(enc[i]))
    else:
        enc_new.append(enc[i])

#convert to hex strings        
enc_hex = []
for binary in enc_new:
    enc_hex.append((hex(int(binary, 2))))
print(enc_hex)
```

> The output is a list of hexadecimal strings.

```
['0x19203f3a', '0x21020615', '0x36056334', '0x7c150d10', '0x24131126', '0x7c15670c', '0x2c13370c', '0xc361766', '0x7d0c372e']
```

> Store them in a list of hexadecimal numbers and `XOR` with the key to get the flag.

```python
key = 0x4d415253
c = [0x19203f3a, 0x21020615, 0x36056334, 0x7c150d10, 0x24131126, 0x7c15670c, 0x2c13370c, 0xc361766, 0x7d0c372e]
print(b"".join(bytes.fromhex(hex(key ^ i)[2:]) for i in c).decode("utf-8"))
```

`TamilCTF{D1g1T_CiRCu1T5_aRe_AwE50Me}`

## Obscure

![image](https://user-images.githubusercontent.com/68913871/134920839-ce673ebb-d011-43c7-8d97-806fd1e9a55c.png)  
[obscure.zip](https://github.com/Rookie441/CTF/files/7236690/obscure.zip)

> The file is a python byte-compiled file.

![image](https://user-images.githubusercontent.com/68913871/134920971-3626bf13-7371-4dbe-ab73-9937c7783b64.png)

> To decompile, rename as `.pyc` and run [uncompyle6](https://pypi.org/project/uncompyle6/) and we get the following:

```python
# uncompyle6 version 3.7.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)]
# Embedded file name: reverseme.py
# Compiled at: 2021-09-04 17:21:21
import numpy as np
flag = 'TamilCTF{this_one_is_a_liability_dont_fall_for_it}'
np.random.seed(369)
data = np.array([ ord(c) for c in flag ])
extra = np.random.randint(1, 5, len(flag))
product = np.multiply(data, extra)
temp1 = [ x for x in data ]
temp2 = [ ord(x) for x in 'dondaVSclb' * 5 ]
c = [ temp1[i] ^ temp2[i] for i in range(len(temp1)) ]
flagdata = ('').join(hex(x)[2:].zfill(2) for x in c)
real_flag = '300e030d0d1507251700361a3a0127662120093d551c311029330c53022e1d3028541315363c5e3d063d0b250a090c52021f'
# okay decompiling reverseme.pyc
```

> In the above code, we can see an encryption algorithm running on a sample flag `TamilCTF{this_one_is_a_liability_dont_fall_for_it}`. If we were to `print(flagdata)`, we get:

```
300e030d0d15072517160c061d3b0e38363c05113b0e31080837310a000b101631000e38273c0a03080331020e240c0a181f
```

> This format is the same as that of `real_flag`, but the values differ. We need to reverse the encryption algorithm and pass in the flagdata of `real_flag` to get the actual flag.

> We can adopt a bruteforce approach whereby we pass every printable ascii character through the algorithm and get the output, then compare it with the ciphertext to map out the ascii flag.

> But first, we should explore the encryption algorithm. In the example below, encrypting the letter `T` gives us `30` which corresponds to the first 2 digits of the flagdata of `real_flag`. Since we know the flag format is `TamilCTF{}`, we can proceed to encrypt the next letter `a`, and we should expect `0e`, which is the next 2 digits of flagdata. However, we are given `05` instead. Strange.

```
real_flag = '300e030d0d1507251700361a3a0127662120093d551c311029330c53022e1d3028541315363c5e3d063d0b250a090c52021f'
"T" : 30
"a" : 05
```

> Upon further exploration, I realised that the characters has to be in the correct index before encryption will tally. Here, the letter `a` is at the 2nd position and the result is `0e` as expected.

```
"Ta" : 300e
"TamilCTF{" : 300e030d0d15072517
```

> Thus, we create a string called `flag_decrypted`. We append a printable ascii character and compare it with the algorithm. If output matches with `real_flag`(truncated), continue with the next position, else, revert back to the original string and try a different ascii character. Since we know the flag format, we can start off with `TamilCTF{`. This is the final code:

```python
import numpy as np
def algo(flag):
    np.random.seed(369)
    data = np.array([ ord(c) for c in flag ])
    extra = np.random.randint(1, 5, len(flag))
    product = np.multiply(data, extra)
    temp1 = [ x for x in data ]
    temp2 = [ ord(x) for x in 'dondaVSclb' * 5 ]
    c = [ temp1[i] ^ temp2[i] for i in range(len(temp1)) ]
    flagdata = ('').join(hex(x)[2:].zfill(2) for x in c)
    return flagdata

flag = 'TamilCTF{this_one_is_a_liability_dont_fall_for_it}'
flag_length = len(flag)
real_flag = '300e030d0d1507251700361a3a0127662120093d551c311029330c53022e1d3028541315363c5e3d063d0b250a090c52021f'

import string
ascii_list = string.printable

flag_decrypted = "TamilCTF{"

for y in range(len(flag_decrypted),flag_length):
    temp_flag = flag_decrypted
    for sym in ascii_list:
        temp_flag+=sym #try ascii char
        if algo(temp_flag) == real_flag[:2*y]: #check against truncated real_flag
            flag_decrypted = temp_flag #append correct char
        else:
            temp_flag = flag_decrypted #go back to original
            continue
    print(flag_decrypted)

flag_decrypted+="}"
print(flag_decrypted)
```

> We get the following output:

```
TamilCTF{
TamilCTF{b
TamilCTF{bR
TamilCTF{bRu
TamilCTF{bRuT
TamilCTF{bRuTe
TamilCTF{bRuTeF
TamilCTF{bRuTeF0
TamilCTF{bRuTeF0r
TamilCTF{bRuTeF0rC
TamilCTF{bRuTeF0rCe
TamilCTF{bRuTeF0rCe_
TamilCTF{bRuTeF0rCe_1
TamilCTF{bRuTeF0rCe_1s
TamilCTF{bRuTeF0rCe_1s_
TamilCTF{bRuTeF0rCe_1s_t
TamilCTF{bRuTeF0rCe_1s_tH
TamilCTF{bRuTeF0rCe_1s_tHe
TamilCTF{bRuTeF0rCe_1s_tHe_
TamilCTF{bRuTeF0rCe_1s_tHe_0
TamilCTF{bRuTeF0rCe_1s_tHe_0n
TamilCTF{bRuTeF0rCe_1s_tHe_0nL
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0r
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rC
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_2
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_2_
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_2_b
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_2_bR
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_2_bRe
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_2_bReA
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_2_bReAk
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_2_bReAk_
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_2_bReAk__
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_2_bReAk__1
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_2_bReAk__1n
TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_2_bReAk__1n}
```

`TamilCTF{bRuTeF0rCe_1s_tHe_0nLy_F0rCe_2_bReAk__1n}`

## [Go to Top](#tamilctf2021)
