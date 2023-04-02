# [HSCTF 8](https://ctftime.org/event/1264)

<img align="left" width="200" height="175" src="https://user-images.githubusercontent.com/68913871/123514325-0d998b80-d6c5-11eb-971b-1f57a422681e.png">

&nbsp; 108 hours Jeopardy-Style  
&nbsp; Mon, 14 June 2021, 20:00 SGT — Sat, 19 June 2021, 08:00 SGT  

&nbsp; **Team Name:** *Rookie441*  
&nbsp; **Team Member(s):**  
&nbsp; 1. *Lee Wen Bin Andre*  

<br/><br>  

| Challenge | Category |
| --- | --- |
| [queen-of-the-hill](#queen-of-the-hill)	| Crypto |
| [aptenodytes-forsteri](#aptenodytes-forsteri)	| Crypto |
| [opisthocomus-hoazin](#opisthocomus-hoazin) | Crypto |
| [glass-windows](#glass-windows) | Misc |

## queen-of-the-hill

![image](https://user-images.githubusercontent.com/68913871/123515213-fd83ab00-d6c8-11eb-8401-4dc442e796de.png)

> In this challenge, we are given a cipher text which we must decipher. Queen-of-the-hill suggest a [hill cipher](https://www.dcode.fr/hill-cipher), which is applicable in this case as we have a=0 and a 3x3 matrix. Proceed to decode it to obtain the flag.

![image](https://user-images.githubusercontent.com/68913871/123515256-2a37c280-d6c9-11eb-8705-8c054d464129.png)  
![image](https://user-images.githubusercontent.com/68913871/123515257-328ffd80-d6c9-11eb-9f43-ea18d80a42dd.png)

`flag{climb_your_way_to_the_top}`

## aptenodytes-forsteri

![image](https://user-images.githubusercontent.com/68913871/123515299-68cd7d00-d6c9-11eb-9d26-5b43c7d1b1c7.png)

> This is the contents of `aptenodytes-forsteri.py`

```python
flag = open('flag.txt','r').read() #open the flag
assert flag[0:5]=="flag{" and flag[-1]=="}" #flag follows standard flag format
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encoded = ""
for character in flag[5:-1]:
    encoded+=letters[(letters.index(character)+18)%26] #encode each character
print(encoded)
```
> This is the contents of `output.txt`

```txt
IOWJLQMAGH
```
> We can observe that the python script encodes a string using `+18 % 26` to produce the output we see in output.txt  
Thus, if we can reverse the algorithm, we should be able to obtain the flag text from the given output.

> With knowledge about modulus operations, I was able to successfully write a small python code to reverse the function.

```python
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
decoded = ""
for character in "IOWJLQMAGH":
    if letters.index(character) <= 17:
        decoded+=letters[letters.index(character)+8]
    else:
        decoded+=letters[letters.index(character)-18]
print(decoded)
```

> This gave us the output `QWERTYUIOP`. We can double-check against the original script by setting the flag as such.

```python
flag = "flag{QWERTYUIOP}"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
encoded = ""
for character in flag[5:-1]:
    encoded+=letters[(letters.index(character)+18)%26] #encode each character
print(encoded)
```
> This gave us the output `IOWJLQMAGH`, which is the same as that of output.txt. This means that our reverse script works, which verifies our answer.

`flag{QWERTYUIOP}`

## opisthocomus-hoazin

![image](https://user-images.githubusercontent.com/68913871/123516212-843a8700-d6cd-11eb-9ce9-489a56c56ca5.png)

> This is the contents of `opisthocomus-hoazin.py`

```python
import time
from Crypto.Util.number import *
flag = open('flag.txt','r').read()
p = getPrime(1024)
q = getPrime(1024)
e = 2**16+1
n=p*q
ct=[]
for ch in flag:
    ct.append((ord(ch)^e)%n)
print(n)
print(e)
print(ct)
```

> This is the contents of `output.txt`

```txt
15888457769674642859708800597310299725338251830976423740469342107745469667544014118426981955901595652146093596535042454720088489883832573612094938281276141337632202496209218136026441342435018861975571842724577501821204305185018320446993699281538507826943542962060000957702417455609633977888711896513101590291125131953317446916178315755142103529251195112400643488422928729091341969985567240235775120515891920824933965514217511971572242643456664322913133669621953247121022723513660621629349743664178128863766441389213302642916070154272811871674136669061719947615578346412919910075334517952880722801011983182804339339643
65537
[65639, 65645, 65632, 65638, 65658, 65653, 65609, 65584, 65650, 65630, 65640, 65634, 65586, 65630, 65634, 65651, 65586, 65589, 65644, 65630, 65640, 65588, 65630, 65618, 65646, 65630, 65607, 65651, 65646, 65627, 65586, 65647, 65630, 65640, 65571, 65612, 65630, 65649, 65651, 65586, 65653, 65621, 65656, 65630, 65618, 65652, 65651, 65636, 65630, 65640, 65621, 65574, 65650, 65630, 65589, 65634, 65653, 65652, 65632, 65584, 65645, 65656, 65630, 65635, 65586, 65647, 65605, 65640, 65647, 65606, 65630, 65644, 65624, 65630, 65588, 65649, 65585, 65614, 65647, 65660]
```

> From the python file, it can be seen that the output printed is n,e,ct separated by newline.  
Comparing with the output.txt, gives the values of n, e, and ct.

> Further exploration of the .py code revealed that there is a mapping algorithm that maps ever character in the flag to a number that we see in the ct list.

```python
for ch in flag:
    ct.append((ord(ch)^e)%n)
```

> The function ord takes in a single ascii character and output its corresponding numerical value.  
Since I know the algorithm, I can create a list of values corresponding to the printable ascii characters by using the string library.  
Using the list, I can then do a python list comparison on ct using .index to find the corresponding character.

> This is the script I created.

```python
n = 15888457769674642859708800597310299725338251830976423740469342107745469667544014118426981955901595652146093596535042454720088489883832573612094938281276141337632202496209218136026441342435018861975571842724577501821204305185018320446993699281538507826943542962060000957702417455609633977888711896513101590291125131953317446916178315755142103529251195112400643488422928729091341969985567240235775120515891920824933965514217511971572242643456664322913133669621953247121022723513660621629349743664178128863766441389213302642916070154272811871674136669061719947615578346412919910075334517952880722801011983182804339339643
import string
alphabet_list = string.printable

code_store = []

for i in alphabet_list:
    signature = (ord(i)^65537)%n
    print(i, signature, end = '\t')
    code_store.append(signature)

ct = [65639, 65645, 65632, 65638, 65658, 65653, 65609, 65584, 65650, 65630, 65640, 65634, 65586, 65630, 65634, 65651, 65586, 65589, 65644, 65630, 65640, 65588, 65630, 65618, 65646, 65630, 65607, 65651, 65646, 65627, 65586, 65647, 65630, 65640, 65571, 65612, 65630, 65649, 65651, 65586, 65653, 65621, 65656, 65630, 65618, 65652, 65651, 65636, 65630, 65640, 65621, 65574, 65650, 65630, 65589, 65634, 65653, 65652, 65632, 65584, 65645, 65656, 65630, 65635, 65586, 65647, 65605, 65640, 65647, 65606, 65630, 65644, 65624, 65630, 65588, 65649, 65585, 65614, 65647, 65660]

print()
for ch in ct:
    if ch in code_store:
        print(alphabet_list[code_store.index(ch)],end='')
    else:
        print("Non-printable character found!")
        break
```

> This is the output.

![image](https://user-images.githubusercontent.com/68913871/123516377-5c97ee80-d6ce-11eb-9956-d7ae8493e25e.png)

`flag{tH1s_ic3_cr34m_i5_So_FroZ3n_i"M_pr3tTy_Sure_iT's_4ctua1ly_b3nDinG_mY_5p0On}`

## glass-windows

![image](https://user-images.githubusercontent.com/68913871/123517076-d2ea2000-d6d1-11eb-87ae-763eee1ee054.png)  
[pallets-of-gold.png](https://user-images.githubusercontent.com/68913871/123516948-48a1bc00-d6d1-11eb-891a-24130cff2100.png)

> Looks like static, maybe change the planes using this [steganography tool](https://aperisolve.fr/) to see a hidden flag.

![image](https://user-images.githubusercontent.com/68913871/123517123-f3b27580-d6d1-11eb-8a51-065ceedab964.png)

`flag{plte_chunks_remind_me_of_gifs}`  

## [Go to Top](#hsctf-8)
