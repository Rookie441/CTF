# [HSCTF 8](https://ctf.hsctf.com/)

<img align="left" width="200" height="175" src="https://user-images.githubusercontent.com/68913871/123514325-0d998b80-d6c5-11eb-971b-1f57a422681e.png">

&nbsp; 108 hours Jeopardy-Style  
&nbsp; Mon, 14 June 2021, 20:00 SGT — Sat, 19 June 2021, 08:00 SGT  

&nbsp; [CTFtime.org_HSCTF 8.pdf](https://github.com/Rookie441/CTF/files/6720168/CTFtime.org_HSCTF.8.pdf)  

<br/><br/><br/>

**Team Name:** *Rookie441*  
**Team Member(s):**
1. *Lee Wen Bin Andre*

**Final Position:** *396/1164*

| Category | Challenges Solved |
| --- | --- |
| [Crypto](#crypto)	| 3/12 |
| [Web](#web) | 1/6 |
| [Miscellaneous](#miscellaneous) | 8/14 |
| Pwn |	0/4 |
| Reverse	| 0/7 |
| Algo	| 0/7 |
| | Total: 12/50 |  

**About:** HSCTF8 is my 2nd CTF which I decided to do right after BCACTF2.0 to have a gauge of the difficulty level as this was a more established CTF. Interestingly, HSCTF8 adopts a dynamic scoring system, where the more solves a challenge had, the less points it awards. In addition, the challenge started off with 29 challenges and more were added to the pool as time passed. I took a look at most challenges, but only committed for half a day. The pwn and reverse challenges left me clueless and instead of googling, I decided to end my progress prematurely to continue with the intermediate courses in CDDC to get better.      

**Disclaimer:** This is not a professional writeup. Its core purpose is to serve as memory and/or personal education.  

# Challenges
## Crypto

![image](https://user-images.githubusercontent.com/68913871/123515213-fd83ab00-d6c8-11eb-8401-4dc442e796de.png)

> In this challenge, we are given a cipher text which we must decipher. Queen-of-the-hill suggest a [hill cipher](https://www.dcode.fr/hill-cipher), which is applicable in this case as we have a=0 and a 3x3 matrix. Proceed to decode it to obtain the flag.

![image](https://user-images.githubusercontent.com/68913871/123515256-2a37c280-d6c9-11eb-8705-8c054d464129.png)  
![image](https://user-images.githubusercontent.com/68913871/123515257-328ffd80-d6c9-11eb-9f43-ea18d80a42dd.png)

`flag{climb_your_way_to_the_top}`

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

## Web

![image](https://user-images.githubusercontent.com/68913871/123516402-7df8da80-d6ce-11eb-80ba-810c86aa98cd.png)

> In this challenge, we are given a website. The website does not allow us to right-click inspect. However, there is a work around.  
Use tripledot > more tools > developer tools.

![image](https://user-images.githubusercontent.com/68913871/123516440-a84a9800-d6ce-11eb-9a57-f06535414d57.png)

> We can then navigate to the scripts section and find the flag.

![image](https://user-images.githubusercontent.com/68913871/123516446-ae407900-d6ce-11eb-8b7a-c5367c18aac4.png)

`flag{keyboard_shortcuts_or_taskbar}`

## Miscellaneous

![image](https://user-images.githubusercontent.com/68913871/123516580-6706b800-d6cf-11eb-974d-82f648cca0ad.png)

> This challenge requires us to connect to the target port using netcat. Upon connection, we are prompted for a solution, and was given a command to run a solver to obtain a solution.

![image](https://user-images.githubusercontent.com/68913871/123516627-a46b4580-d6cf-11eb-91fb-9a5917388442.png)

> So, I interrupted the process and run the code provided to give us a solution. Now that I have the solution, I can then proceed to netcat again and paste the solution in. However, they returned a Proof-of-work failpow fail error.

> I later found out that the solution keeps changing per request. So I created a separate terminal for the solution and connection.

![image](https://user-images.githubusercontent.com/68913871/123516755-42f7a680-d6d0-11eb-8ac6-c5866da541a6.png)

![image](https://user-images.githubusercontent.com/68913871/123516821-9ff35c80-d6d0-11eb-8050-41492406b3f1.png)

> Now, pasting the solution gives us the flag.

`flag{the_cat_says_meow}`

![image](https://user-images.githubusercontent.com/68913871/123516852-d92bcc80-d6d0-11eb-8b57-2962b5278aa8.png)  
[lsblue.png](https://user-images.githubusercontent.com/68913871/123516891-05474d80-d6d1-11eb-9052-b5d4fa6cf4af.png)

> LSBlue suggest LSB (least significant bit) steganography, which can be decoded using this [steganography tool](https://aperisolve.fr/)

![image](https://user-images.githubusercontent.com/68913871/123517042-b3eb8e00-d6d1-11eb-9228-e8ad342b118f.png)

`flag{0rc45_4r3nt_6lu3_s1lly_4895131}`

![image](https://user-images.githubusercontent.com/68913871/123517076-d2ea2000-d6d1-11eb-87ae-763eee1ee054.png)  
[pallets-of-gold.png](https://user-images.githubusercontent.com/68913871/123516948-48a1bc00-d6d1-11eb-891a-24130cff2100.png)

> Looks like static, maybe change the planes using this [steganography tool](https://aperisolve.fr/) to see a hidden flag.

![image](https://user-images.githubusercontent.com/68913871/123517123-f3b27580-d6d1-11eb-8a51-065ceedab964.png)

`flag{plte_chunks_remind_me_of_gifs}`

![image](https://user-images.githubusercontent.com/68913871/123517270-b00c3b80-d6d2-11eb-9c54-26d94653ce02.png)

> A very similar challenge which uses the same approach as the previous challenge.

![image](https://user-images.githubusercontent.com/68913871/123517312-d9c56280-d6d2-11eb-8d6b-98060b03c012.png)

`flag{this_is_why_i_use_premultiplied_alpha}`

> The rest of the Miscellaneous challenges are self explanatory. They are posted for the sake of completion.

![image](https://user-images.githubusercontent.com/68913871/123517248-8e12b900-d6d2-11eb-9bdc-3ae517db5f63.png)

`flag{1m_g0in6_1ns@ne_1m_g0in6_1ns@ne_1m_g0in6_1ns@ne}`

![image](https://user-images.githubusercontent.com/68913871/123517256-9c60d500-d6d2-11eb-9299-4eae6bd82352.png)

`flag{we1c0me_t0_hsctf!}`

![image](https://user-images.githubusercontent.com/68913871/123517377-2315b200-d6d3-11eb-9fbd-7c129748a5d6.png)

`flag{thank_you_digitalocean!}`

![image](https://user-images.githubusercontent.com/68913871/123517384-2e68dd80-d6d3-11eb-952c-26a77ca47deb.png)

`flag{thanks_for_participating_in_hsctf!}`

**Summary:** The challenges in this CTF are way above my current skill level. The only challenges I was able to solve were simple one-command or one-tool type problems. I only found the crypto challenges interesting as I was tested on python knowledge.   

## [Go to Top](#hsctf-8)
