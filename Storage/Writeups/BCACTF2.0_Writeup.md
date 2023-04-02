# [BCACTF 2.0](https://ctftime.org/event/1369)<a name="bcactf-2"></a>

<img align="left" width="200" height="175" src="https://user-images.githubusercontent.com/68913871/123500036-9f75aa00-d66d-11eb-9b3d-e05bb173b405.png">

&nbsp; Start time: 2021-06-10 20:00:00 EDT  
&nbsp; End time: 2021-06-13 20:00:00 EDT  

&nbsp; 72 hours Jeopardy-Style  
&nbsp; SGT: 11 June 2021 0800 - 14 June 2021 0800  

&nbsp; [CTFtime.org_BCACTF_2.0.pdf](https://github.com/Rookie441/CTF/files/6719951/CTFtime.org._.BCACTF.2.0.pdf)  
&nbsp; [Rookie441_BCACTF_2.0.pdf](https://github.com/Rookie441/CTF/files/6719952/Rookie441.BCACTF.2.0.pdf)
<br/>

**Team Name:** *Rookie441*  
**Team Member(s):**
1. *Andre Lee*

**Final Position:** *134/841*

| Category | Challenges Solved |
| --- | --- |
| [Miscellaneous](#miscellaneous)	| 4/8 |
| [Binary](#binary) | 3/8 |
| [Crypto](#crypto) | 6/16 |
| [Forensics](#forensics) |	6/10 |
| [Reverse](#reverse)	| 3/11 |
| [Web](#web)	| 7/13 |
| | Total: 29/66 |  

# Challenges
## Miscellaneous

![image](https://user-images.githubusercontent.com/68913871/123500119-46f2dc80-d66e-11eb-8542-06871e7d5b69.png)

> This is an example problem. The flag is given in the problem description. Hints are for trolling purposes.  

`bcactf{this_is_a_flag}`


![image](https://user-images.githubusercontent.com/68913871/123503145-968fd300-d683-11eb-948c-b75cc0b72be7.png)

> This problem requires navigation to their discord server to find the flag.

![image](https://user-images.githubusercontent.com/68913871/123503264-7280c180-d684-11eb-8433-9228508cfe58.png)

`bcactf{is_too_sanity_checks_two_much?}`

![image](https://user-images.githubusercontent.com/68913871/123503966-de652900-d688-11eb-99a3-5adf46b05de6.png)

> This problem requires the netcat command which I had installed on my Linux Virtual Machine. Simply copy the command into the terminal. The flag is obtained upon scrolling to the bottom.

![image](https://user-images.githubusercontent.com/68913871/123503998-14a2a880-d689-11eb-887f-eafe98acb5c4.png)

`bcactf{r41nb0w_P0p_t4rT5_g0_nY4_s3Dy0Bqd6u}`

![image](https://user-images.githubusercontent.com/68913871/123504024-4b78be80-d689-11eb-9a71-de5210c30bef.png)

> This challenge was released towards the end of the competition to gather feedback from participants. A free flag is given upon completion of the survey.

`bcactf{so_long_and_thanks_for_all_the_flags}`

## Binary
## BCA Mart

![image](https://user-images.githubusercontent.com/68913871/123504089-c9d56080-d689-11eb-9960-2600704f1ec0.png)  

> In this challenge, we are given $10 as well as a list of items to purchase at the BCA mart. Of course, we want to purchase option 6: Flag. However, the price of the flag is $100 and we do not have enough money.

> This binary exploitation challenge requires knowledge about [2’s complement representation of negative numbers](https://www.networkworld.com/article/3010974/whats-so-special-about-2147483648.html) and the idea is to trick the mart into selling the flag for a negative price which we can afford.

> Input greater than 2,147,483,647 will be detected as prankster and having too small a value will make the cost to be too large to afford.

![image](https://user-images.githubusercontent.com/68913871/123504251-a3fc8b80-d68a-11eb-9eed-8aa603f9d679.png)

> Using 2,147,483,647 gives the flag.

![image](https://user-images.githubusercontent.com/68913871/123504269-b37bd480-d68a-11eb-9fb8-5ddf0097584f.png)

`bcactf{bca_store??_wdym_ive_never_heard_of_that_one_before}`

## Honors ABCs
![image](https://user-images.githubusercontent.com/68913871/123504301-ea51ea80-d68a-11eb-8708-fcc583d21c4c.png)  

> In this challenge, we are expected to recite the ABCs and a score will be given to us depending on how accurate it is. Open the .c file to note the control flow and anything interesting.

```c
if (grade < 60)
    puts("An F? I'm sorry, but you clearly need to study harder.");
else if (grade < 70)
    puts ("You didn't fail, but you could do better than a D.");
else if (grade < 80)
    puts("Not terrible, but a C's nothing to write home about.");
else if (grade < 90)
    puts("Alright, a B's not bad, I guess.");
else if (grade < 100)
    puts("Ayyy, nice job on getting an A!");
else if (grade == 100) {
    puts("Perfect score!");
    puts("You are an model BCA student.");
} else {
    puts("How did you end up here?");
    sleep(2);
    puts("You must have cheated!");
    sleep(2);
    puts("Let me recite the BCA plagarism policy.");
    sleep(2);

    FILE *fp = fopen("flag.txt", "r");
```

> Else clause is interesting as it contains the flag.txt. But the only way to get there is to mess with the grade assignment statement such that it is >100.

```c
char *correct = "abcdefghijklmnopqrstuvwxyz";
```

```c
for (int i = 0; i < 26; ++i) {
    if (response[i] == 0)
        break;
    if (response[i] != correct[i])
        break;
    grade = i * 4;
}
```

> It seems that grade is determined by the variable i, which is a counter from 0 to 25. It can be noted that 25*4 = 100, which is not what we hope to achieve. We need grade > 100. Have a look at other segments of the code, such as the variable declaration.

```c
int main() {
    int grade = 0;
    char response[50];
```

> Variable response is a char array of fixed size 50, which is far more than the total number of alphabets required for a response, which is exactly 26. This suggests a possible buffer overflow to mess with the contents of the array. However, having a correct sequence will terminate the program prematurely.

![image](https://user-images.githubusercontent.com/68913871/123504579-d4452980-d68c-11eb-9462-cce36235e7e2.png)

> Solution: try adding many spaces or having a wrong sequence

![image](https://user-images.githubusercontent.com/68913871/123504633-39008400-d68d-11eb-96ee-cf82973ca9fa.png)  

![image](https://user-images.githubusercontent.com/68913871/123504636-3dc53800-d68d-11eb-9ee0-24295d78155c.png)

> Flag is obtained after reciting the Cheating and Plagiarism Policy.

`bcactf{now_i_know_my_A_B_Cs!!_next_time_wont_you_cheat_with_me??}`

## AP ABCs
![image](https://user-images.githubusercontent.com/68913871/123504871-6699fd00-d68e-11eb-8cf4-13207aa513d8.png)  

> This challenge is a sequel to the Honours ABCs challenge, with a twist. Again, we open the .c file to note anything interesting.

```c
for (int i = 0; i < 26; ++i) {
    if (response[i] == 0)
        break;
    if (response[i] != correct[i])
        break;

    if (i == 0)
        score = 1;
    if (i == 7 || i == 14 || i == 20 || i == 24)
        ++score;
}
```
> Likewise, we have a loop involving variable i, which determines what score we get. It can be noted that the possible values of score are 1,2,3,4 and 5.

```c
if (score == 1)
    puts("Ouch. That hurts.");
else if (score == 2)
    puts("At least that's not a 1...");
else if (score == 3)
    puts("You are \"qualified\".");
else if (score == 4)
    puts("You are \"very well qualified\".");
else if (score == 5)
    puts("Nice job!");
else if (score == 0x73434241) {
    puts("Tsk tsk tsk.");
    sleep(2);
    puts("Cheating on the AP® tests is really bad!");
    sleep(2);
    puts("Let me read you the College Board policies:");
    sleep(2);

    FILE *fp = fopen("flag.txt", "r");
```
> We need to obtain the score as exactly 0x73434241. Converting this [hexadecimal to ASCII](https://www.rapidtables.com/convert/number/hex-to-ascii.html), we get sCBA. Most processors have little endian format which means the least significant byte is stored at the lowest address in memory. Thus, in memory, sCBA will look like ABCs, which is more relevant for this question.

>  Keep repeating ABCs until the char response array overflows and score variable is altered.

![image](https://user-images.githubusercontent.com/68913871/123505256-9f3ad600-d690-11eb-8bd5-a086b3b12d43.png)

> Flag is obtained after reciting the College Board Policies.

`bcactf{bca_is_taking_APs_in_june_aaaaaaaa_wish_past_me_luck}`

## Crypto
## Easy RSA

![image](https://user-images.githubusercontent.com/68913871/123505353-20926880-d691-11eb-9767-2f8cedaf06a0.png)  

> This challenge tests on the RSA encryption. [Integer Factorization Calculator](https://www.alpertron.com.ar/ECM.HTM) is a very handy website to solve RSA as it has powerful functions such as Modpow and Modinv and supports large digits as well.

> phi(n) = (p-1)(q-1):  
8042203610790038807880567941309789150150900450372853468256556629646193403108  
Modinv(e,phi(n)) = d:  
4895611838388522487150697438371515909261488525071715048233750808546849654653  
Modpow(ct,d,n):  
2652540753558987928135559621775165718420934450124971589287668131581053 (plaintext in decimal)

> Use `long_to_bytes` to convert plaintext to ascii
```python
from Crypto.Util.number import long_to_bytes
print(long_to_bytes(2652540753558987928135559621775165718420934450124971589287668131581053).decode())
```

`bcactf{RSA_IS_EASY_AFTER_ALL}`

## Slightly Harder RSA
![image](https://user-images.githubusercontent.com/68913871/123505650-df9b5380-d692-11eb-8961-19951df4f601.png)  

> This challenge is a sequel to Easy RSA. The only difference is that now we are not given the values of p and q. However, it can be noted that since n is a small value, we can [brute force its factorization](https://asecuritysite.com/encryption/crackrsa).

> After brute-forcing, we get:  
p=884666943491340899394244376743  
q=1070864180718820651198166458463

> Run a simple RSA solving script below to obtain the plaintext in decimal, using p,q,e,ct as inputs.

```python
import math

def getModInverse(a, m):
    if math.gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m

    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def main():

    # take input string and convert to integer
    p1 = input('Value of P in decimal: ')
    q1 = input('Value of Q in decimal: ')
    e1 = input('Value of E in decimal: ')
    c1 = input('Ciphertext in decimal: ')
    p = int(p1)
    q = int(q1)
    e = int(e1)
    ct = int(c1)

    # compute n
    n = p * q

    # Compute phi(n)
    phi = (p - 1) * (q - 1)

     # Compute modular inverse of e
    d = getModInverse(e, phi)


    # Compute modualr inverse of e
    print( "\n## Result ##")
    print( "Modulus N         : " + str(n) )
    print( "Euler's PHi       : " + str(phi) )
    print( "Private Exponent D: " + str(d) )

    # Decrypt ciphertext
    pt = pow(ct, d, n)
    print("Plaintext in decimal: " + str(pt))

if __name__ == "__main__":
    main()
```
> Plaintext in decimal:  
143794522380749587603817933677936428593350769010557

> Use `long_to_bytes` to convert plaintext to ascii
```python
from Crypto.Util.number import long_to_bytes
print(long_to_bytes(143794522380749587603817933677936428593350769010557).decode())
```

`bcactf{rsa_factoring}`

## Little e
![image](https://user-images.githubusercontent.com/68913871/123506047-bed3fd80-d694-11eb-864a-6c43b3b25183.png)  

> This challenge is also related to RSA encryption. This time, the value of n given is too large for us to brute-force factorization. However, it can be noted that the value of e is very small, which poses a vulnerability.

> We know that encryption in RSA is `m**e mod n`. If e=3 and m is small enough that the result is smaller than n then encryption is just `m**3`. Thus, the decryption will be the reverse which is cube root. [This](https://www.dcode.fr/cube-root) is a useful tool to handle cube root involving many digits.

> Cube root of ct gives:  
10361487318589796594107970141401777269621804259847073873440233698173 (plaintext in decimal)

> Use `long_to_bytes` to convert plaintext to ascii
```python
from Crypto.Util.number import long_to_bytes
print(long_to_bytes(10361487318589796594107970141401777269621804259847073873440233698173).decode())
```

`bcactf{R54_N0T_50_S3CUR3_33}`

## Cryptogram Puzzle
![image](https://user-images.githubusercontent.com/68913871/123506302-0eff8f80-d696-11eb-8e5e-382f9a0d3af9.png)  

> Open the file with notepad. We can see that this is a standard Cryptogram puzzle. We will be editing with notepad++ and replacing the unknown characters to readable alphabets.

```html
"􇺟􊸉􊶬􊸉􃗁 􋄚􆖓􇺟􇺟􄧻 􋄚􆆗􊶬􊸉 􉯓􆖓􌲔 􌲔􃄏" 􆆗􁫞 􇽛􉂫􊸉 􉗽􊸉􆞎􌲔􇽛 􁫞􆆗􇺟􋄚􋐝􊸉 􃗁􊸉􄺷􆖓􃗁􉗽􊸉􉗽 􆞎􉯓 􊸉􇺟􋄚􋐝􆆗􁫞􉂫 􁫞􆆗􇺟􋄚􊸉􃗁 􄧻􇺟􉗽 􁫞􆖓􇺟􋄚􏕈􃗁􆆗􇽛􊸉􃗁 􃗁􆆗􄺷􏟟 􄧻􁫞􇽛􋐝􊸉􉯓, 􃗁􊸉􋐝􊸉􄧻􁫞􊸉􉗽 􆖓􇺟 27 􀴠􌲔􋐝􉯓 1987. 􆆗􇽛 􏕈􄧻􁫞 􏕈􃗁􆆗􇽛􇽛􊸉􇺟 􄧻􇺟􉗽 􃄏􃗁􆖓􉗽􌲔􄺷􊸉􉗽 􆞎􉯓 􁫞􇽛􆖓􄺷􏟟 􄧻􆆗􇽛􏟟􊸉􇺟 􏕈􄧻􇽛􊸉􃗁􌘗􄧻􇺟, 􄧻􇺟􉗽 􏕈􄧻􁫞 􃗁􊸉􋐝􊸉􄧻􁫞􊸉􉗽 􄧻􁫞 􇽛􉂫􊸉 􌶴􆆗􃗁􁫞􇽛 􁫞􆆗􇺟􋄚􋐝􊸉 􌶴􃗁􆖓􌘗 􄧻􁫞􇽛􋐝􊸉􉯓'􁫞 􉗽􊸉􆞎􌲔􇽛 􄧻􋐝􆞎􌲔􌘗, 􏕈􉂫􊸉􇺟􊸉􊶬􊸉􃗁 􉯓􆖓􌲔 􇺟􊸉􊸉􉗽 􁫞􆖓􌘗􊸉􆞎􆖓􉗽􉯓 (1987). 􇽛􉂫􊸉 􁫞􆖓􇺟􋄚 􏕈􄧻􁫞 􄧻 􏕈􆖓􃗁􋐝􉗽􏕈􆆗􉗽􊸉 􇺟􌲔􌘗􆞎􊸉􃗁-􆖓􇺟􊸉 􉂫􆆗􇽛, 􆆗􇺟􆆗􇽛􆆗􄧻􋐝􋐝􉯓 􆆗􇺟 􇽛􉂫􊸉 􌲔􇺟􆆗􇽛􊸉􉗽 􏟟􆆗􇺟􋄚􉗽􆖓􌘗 􆆗􇺟 1987, 􏕈􉂫􊸉􃗁􊸉 􆆗􇽛 􁫞􇽛􄧻􉯓􊸉􉗽 􄧻􇽛 􇽛􉂫􊸉 􇽛􆖓􃄏 􆖓􌶴 􇽛􉂫􊸉 􄺷􉂫􄧻􃗁􇽛 􌶴􆖓􃗁 􌶴􆆗􊶬􊸉 􏕈􊸉􊸉􏟟􁫞 􄧻􇺟􉗽 􏕈􄧻􁫞 􇽛􉂫􊸉 􆞎􊸉􁫞􇽛-􁫞􊸉􋐝􋐝􆆗􇺟􋄚 􁫞􆆗􇺟􋄚􋐝􊸉 􆖓􌶴 􇽛􉂫􄧻􇽛 􉯓􊸉􄧻􃗁. 􆆗􇽛 􊸉􊶬􊸉􇺟􇽛􌲔􄧻􋐝􋐝􉯓 􇽛􆖓􃄏􃄏􊸉􉗽 􇽛􉂫􊸉 􄺷􉂫􄧻􃗁􇽛􁫞 􆆗􇺟 25 􄺷􆖓􌲔􇺟􇽛􃗁􆆗􊸉􁫞, 􆆗􇺟􄺷􋐝􌲔􉗽􆆗􇺟􋄚 􇽛􉂫􊸉 􌲔􇺟􆆗􇽛􊸉􉗽 􁫞􇽛􄧻􇽛􊸉􁫞 􄧻􇺟􉗽 􏕈􊸉􁫞􇽛 􋄚􊸉􃗁􌘗􄧻􇺟􉯓.[6] 􇽛􉂫􊸉 􁫞􆖓􇺟􋄚 􏕈􆖓􇺟 􆞎􊸉􁫞􇽛 􆞎􃗁􆆗􇽛􆆗􁫞􉂫 􁫞􆆗􇺟􋄚􋐝􊸉 􄧻􇽛 􇽛􉂫􊸉 1988 􆞎􃗁􆆗􇽛 􄧻􏕈􄧻􃗁􉗽􁫞.

􇽛􉂫􊸉 􌘗􌲔􁫞􆆗􄺷 􊶬􆆗􉗽􊸉􆖓 􌶴􆖓􃗁 􇽛􉂫􊸉 􁫞􆖓􇺟􋄚 􉂫􄧻􁫞 􆞎􊸉􄺷􆖓􌘗􊸉 􇽛􉂫􊸉 􆞎􄧻􁫞􆆗􁫞 􌶴􆖓􃗁 􇽛􉂫􊸉 "􃗁􆆗􄺷􏟟􃗁􆖓􋐝􋐝􆆗􇺟􋄚" 􆆗􇺟􇽛􊸉􃗁􇺟􊸉􇽛 􌘗􊸉􌘗􊸉. 􆆗􇺟 2008, 􄧻􁫞􇽛􋐝􊸉􉯓 􏕈􆖓􇺟 􇽛􉂫􊸉 􌘗􇽛􊶬 􊸉􌲔􃗁􆖓􃄏􊸉 􌘗􌲔􁫞􆆗􄺷 􄧻􏕈􄧻􃗁􉗽 􌶴􆖓􃗁 􆞎􊸉􁫞􇽛 􄧻􄺷􇽛 􊸉􊶬􊸉􃗁 􏕈􆆗􇽛􉂫 􇽛􉂫􊸉 􁫞􆖓􇺟􋄚, 􄧻􁫞 􄧻 􃗁􊸉􁫞􌲔􋐝􇽛 􆖓􌶴 􄺷􆖓􋐝􋐝􊸉􄺷􇽛􆆗􊶬􊸉 􊶬􆖓􇽛􆆗􇺟􋄚 􌶴􃗁􆖓􌘗 􇽛􉂫􆖓􌲔􁫞􄧻􇺟􉗽􁫞 􆖓􌶴 􃄏􊸉􆖓􃄏􋐝􊸉 􆖓􇺟 􇽛􉂫􊸉 􆆗􇺟􇽛􊸉􃗁􇺟􊸉􇽛, 􉗽􌲔􊸉 􇽛􆖓 􇽛􉂫􊸉 􃄏􆖓􃄏􌲔􋐝􄧻􃗁 􃄏􉂫􊸉􇺟􆖓􌘗􊸉􇺟􆖓􇺟 􆖓􌶴 􃗁􆆗􄺷􏟟􃗁􆖓􋐝􋐝􆆗􇺟􋄚.[7] 􇽛􉂫􊸉 􁫞􆖓􇺟􋄚 􆆗􁫞 􄺷􆖓􇺟􁫞􆆗􉗽􊸉􃗁􊸉􉗽 􄧻􁫞􇽛􋐝􊸉􉯓'􁫞 􁫞􆆗􋄚􇺟􄧻􇽛􌲔􃗁􊸉 􁫞􆖓􇺟􋄚 􄧻􇺟􉗽 􆆗􇽛 􆆗􁫞 􆖓􌶴􇽛􊸉􇺟 􃄏􋐝􄧻􉯓􊸉􉗽 􄧻􇽛 􇽛􉂫􊸉 􊸉􇺟􉗽 􆖓􌶴 􉂫􆆗􁫞 􋐝􆆗􊶬􊸉 􄺷􆖓􇺟􄺷􊸉􃗁􇽛􁫞.

􆆗􇺟 2019, 􄧻􁫞􇽛􋐝􊸉􉯓 􃗁􊸉􄺷􆖓􃗁􉗽􊸉􉗽 􄧻􇺟􉗽 􃗁􊸉􋐝􊸉􄧻􁫞􊸉􉗽 􄧻 '􃄏􆆗􄧻􇺟􆖓􌶴􆖓􃗁􇽛􊸉' 􊶬􊸉􃗁􁫞􆆗􆖓􇺟 􆖓􌶴 􇽛􉂫􊸉 􁫞􆖓􇺟􋄚 􌶴􆖓􃗁 􉂫􆆗􁫞 􄧻􋐝􆞎􌲔􌘗 􇽛􉂫􊸉 􆞎􊸉􁫞􇽛 􆖓􌶴 􌘗􊸉, 􏕈􉂫􆆗􄺷􉂫 􌶴􊸉􄧻􇽛􌲔􃗁􊸉􁫞 􄧻 􇺟􊸉􏕈 􃄏􆆗􄧻􇺟􆖓 􄧻􃗁􃗁􄧻􇺟􋄚􊸉􌘗􊸉􇺟􇽛.[8]

􁫞􉂫􄧻􌘗􊸉􋐝􊸉􁫞􁫞􋐝􉯓 􄺷􆖓􃄏􆆗􊸉􉗽 􌶴􃗁􆖓􌘗 [􏕈􆆗􏟟􆆗􃄏􊸉􉗽􆆗􄧻'􁫞 􄧻􃗁􇽛􆆗􄺷􋐝􊸉 􆖓􇺟 􇽛􉂫􊸉 􁫞􌲔􆞎􀴠􊸉􄺷􇽛](􉂫􇽛􇽛􃄏􁫞://􊸉􇺟.􏕈􆆗􏟟􆆗􃄏􊸉􉗽􆆗􄧻.􆖓􃗁􋄚/􏕈􆆗􏟟􆆗/􇺟􊸉􊶬􊸉􃗁_􋄚􆖓􇺟􇺟􄧻_􋄚􆆗􊶬􊸉_􉯓􆖓􌲔_􌲔􃄏)

􆞎􄺷􄧻􄺷􇽛􌶴{􁫞􆖓􃗁􃗁􉯓_􏕈􊸉_􃗁􄧻􇺟_􆖓􌲔􇽛_􆖓􌶴_􃗁􌲔􇺟􊸉􁫞_􁫞􀴠􃗁􉂫􏕈􆞎􋄚}
```

> This [cryptogram tutorial](https://cryptograms.puzzlebaron.com/tutorial.php) provides useful strategies to tackle the puzzle.

> First, we can see the `://` so the characters in front will be https. Also, as we know the flag format is `bcactf{}`, we can then proceed to do the relevant substitution.

![image](https://user-images.githubusercontent.com/68913871/123506551-4de21500-d697-11eb-8de4-532c3845ea71.png)

> Follow on to guess other characters:  
1.  .org
2.  27 xxxx 1987 likely to be june/july
3. Use ETAION frequency analysis
4. Found the quote "never gonna give you up" which directs us to this [wikipedia page](https://en.wikipedia.org/wiki/Never_Gonna_Give_You_Up) where we can easily find the rest of the characters.

`bcactf{sorry_we_ran_out_of_runes_sjrhwbg}`

## Sailing Thru Decryption
![image](https://user-images.githubusercontent.com/68913871/123506646-eaa4b280-d697-11eb-8c19-ed448767f018.png)  

> The country flags at the bottom of the picture is an encryption signal used by the Navy. It can be [decoded](http://skysailtraining.co.uk/international_flag_signals_and_morse_code.htm) to give us `thekeyisfhskdn`.

> The main portion of the picture is an image "Binary" where:
```python
five blue crosses -> 0  
red-yellow-red flag -> 1
```

> We get the following binary:
```python
01100111 01101010 01110011 01101101 01110111 01110011 01111011 00110001 01111000 01011111 01101111 00110001 01101011 01011111 01111000 00110100 01110000 01110010 01011111 01101100 00110011 01111001 00110100 01101010 01101110 00111111 01111101
```

> Convert from binary to ascii using [CyberChef ‘From Binary – 8 bits’](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)&input=MDExMDAxMTEgMDExMDEwMTAgMDExMTAwMTEgMDExMDExMDEgMDExMTAxMTEgMDExMTAwMTEgMDExMTEwMTEgMDAxMTAwMDEgMDExMTEwMDAgMDEwMTExMTEgMDExMDExMTEgMDAxMTAwMDEgMDExMDEwMTEgMDEwMTExMTEgMDExMTEwMDAgMDAxMTAxMDAgMDExMTAwMDAgMDExMTAwMTAgMDEwMTExMTEgMDExMDExMDAgMDAxMTAwMTEgMDExMTEwMDEgMDAxMTAxMDAgMDExMDEwMTAgMDExMDExMTAgMDAxMTExMTEgMDExMTExMDE). We get `gjsmws{1x_o1k_x4pr_l3y4jn?}`, which seems like a flag format. Since we have obtained a key earlier, this could be a vigenere-cipher which can be [decoded](https://www.dcode.fr/vigenere-cipher) using the key `fhskdn`.

`bcactf{1s_h1s_n4me_g3r4rd?}`

## Cipher Mishap
![image](https://user-images.githubusercontent.com/68913871/123506941-66ebc580-d699-11eb-8645-1f66b7111cca.png)  

> Numbers seem to be in octal format.
Convert it to ascii readable characters using [CyberChef “From Octal”](https://gchq.github.io/CyberChef/#recipe=From_Octal('Space')&input=MTI2LVksIDExMy1OLCAxMjItTiwgMTMwLU4sIDExNy1OLCAxMDctTiwgMTM3LCAxMTQtTiwgMTI3LVksIDEzNywgMTEzLVksIDEwNC1OLCAxMzEtTiwgMTEwLU4sIDEzNywgMTA1LVksIDExMC1OLCAxMTAtTiwgMTIxLVksIDEzNywgMTMxLVksIDExNC1OLCAxMTItTiwgMTEwLU4sIDEyMS1OLCAxMTAtTiwgMTI1LU4sIDExMC1OLCAxMzcsIDExNC1ZLCAxMjEtTiwgMTI2LU4sIDEyNy1OLCAxMTAtTiwgMTA0LU4sIDEwNy1O). We get `VKRXOG_LW_KDYH_EHHQ_YLJHQHUH_LQVWHDG`.

> As the challenge description suggests, it is probably a caeser-cipher, which can be [brute-forced](https://www.dcode.fr/caesar-cipher). The top result is: `SHOULD_IT_HAVE_BEEN_VIGENERE_INSTEAD`.

> Also in the text file is -Y and -N appended at the end of each octal number. As the challenge description suggests, it has something to do with Caps Lock. Hence, we assume that Y refers to Caps-Lock ON and N refers to Caps-Lock OFF. And indeed, that is the correct assumption.

`bcactf{Should_iT_Have_BeeN_Vigenere_Instead}`

## Forensics
## Infinite Zip
![image](https://user-images.githubusercontent.com/68913871/123507361-7ff57600-d69b-11eb-92bc-a191c87ed85b.png)  

> This challenge is about unzipping a file. As the name of the challenge suggests, there are many zip files inside the given zip file. My solution was the following:  
7Zip-> open archive-> Ctrl + Pg-down-> to 0.zip -> flag.png

> The intended solution should be to create a script of some sort to traverse the directories. However, since there are only 999 zip files embedded, I decided to do it manually and still got my result in less than a minute.

> However, this is not the end of the challenge as we are trolled with a fake flag.

![image](https://user-images.githubusercontent.com/68913871/123507600-f5ae1180-d69c-11eb-985e-8df79df08c56.png)

> Navigating to the [link](https://tinyurl.com/DefinitelyTheFlag) also got us trolled with a Windows XP ERROR Song. However, looking back at the challenge category: Forensics, my first instinct is to open the image with notepad.

![image](https://user-images.githubusercontent.com/68913871/123507700-69e8b500-d69d-11eb-9680-aa0967e25e2d.png)

> Without much scrolling, we found our flag!

`bcactf{z1p_1n51d3_4_z1p_4_3v3r}`

## Secure Zip
![image](https://user-images.githubusercontent.com/68913871/123507717-8edd2800-d69d-11eb-9bda-8c3924808837.png)  

> This challenge provides us with a zip file containing a flag.txt and homework.txt. However, they are both protected with a password.

> There must be some way to brute-force the password. The first hint directed me to the [fcrackzip](https://mattcasmith.net/2020/09/12/cracking-password-protected-zip-file-fcrackzip) package, while the second hint provided the [rockyou wordlist](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt) used to brute-force common passwords. We then run the command, following the documentation.

![image](https://user-images.githubusercontent.com/68913871/123507820-34909700-d69e-11eb-860e-a9a28509d36e.png)

> Now we just have to unzip the file with the password `dogedoge` to find our flag.

`bcactf{cr4ck1ng_z1p_p455w0rd5_15_fun_a12ca37bdacef7}`

## Zstegosaurus
![image](https://user-images.githubusercontent.com/68913871/123507848-67d32600-d69e-11eb-83f7-5b7cd99695bf.png)  

> This is a steganography challenge where the flag is hidden in the image. The name of the challenge suggests using the zsteg package. But there is this handy [steganography tool](https://aperisolve.fr/) that does a complete analysis using many packages such as strings, binwalk, exiftool and more. Uploading the image gave us the flag.

![image](https://user-images.githubusercontent.com/68913871/123507897-d0220780-d69e-11eb-94d0-d824670f9241.png)

`bcactf{h15_n@m3_i5nt_g3rard}`

## Gerald New Job
![image](https://user-images.githubusercontent.com/68913871/123507924-f47de400-d69e-11eb-87a2-eac64c4a3c42.png)  

> Opening the pdf file gave us a fake flag.

![image](https://user-images.githubusercontent.com/68913871/123507954-2c852700-d69f-11eb-9fa7-9e40a152034c.png)

> So, I proceeded to analyze the pdf file using a Hex Editor.

![image](https://user-images.githubusercontent.com/68913871/123507934-0cedfe80-d69f-11eb-8e34-a70e4332238d.png)

> Note there is a GeraldFlag.png embedded in a PK header with signature 50 4B 03 04, which points to a ZIP file.

> Delete the front few bytes such that the file starts with the PK header and save it as a zip file. Then, open the zip file as archive using 7-Zip.

![image](https://user-images.githubusercontent.com/68913871/123508081-c3ea7a00-d69f-11eb-8d2a-a52377d7d2ba.png)

> Opening GeraldFlag.png gave me the flag.

`bcactf{g3ra1d_15_a_ma5ter_p01yg1ot_0769348}`

## More Than Meets The Eye
![image](https://user-images.githubusercontent.com/68913871/123508132-1a57b880-d6a0-11eb-8c62-96e5b9e8cb77.png)  

> The text document looks empty, but it actually contain hidden messages called [Zero-Width Spaces](https://en.wikipedia.org/wiki/Zero-width_space) (zwsp), as the name of the file suggests.

> Open the file using vim editor.

![image](https://user-images.githubusercontent.com/68913871/123508186-6f93ca00-d6a0-11eb-9702-d82d5e66b559.png)

> It can be observed that <200b> and <200c> repeating: Zero-width space (U+200B) Zero-width non-joiner (U+200C). This suggests a binary style where <200b> can be mapped to 0 and <200c> is mapped to 1.

> Decoding it gives:
```python
011000100110001101100001011000110111010001100110011110110111101000110011011100100011000001011111011101110011000101100100011101000110100001011111011010100111010101101110011001110110110000110011010111110110101000111000001100100110000101111000010010000011010001111101
```

> Running [CyberChef ‘From Binary – 8 bits’](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)&input=MDExMDAwMTAwMTEwMDAxMTAxMTAwMDAxMDExMDAwMTEwMTExMDEwMDAxMTAwMTEwMDExMTEwMTEwMTExMTAxMDAwMTEwMDExMDExMTAwMTAwMDExMDAwMDAxMDExMTExMDExMTAxMTEwMDExMDAwMTAxMTAwMTAwMDExMTAxMDAwMTEwMTAwMDAxMDExMTExMDExMDEwMTAwMTExMDEwMTAxMTAxMTEwMDExMDAxMTEwMTEwMTEwMDAwMTEwMDExMDEwMTExMTEwMTEwMTAxMDAwMTExMDAwMDAxMTAwMTAwMTEwMDAwMTAxMTExMDAwMDEwMDEwMDAwMDExMDEwMDAxMTExMTAx) gave the flag.

`bcactf{z3r0_w1dth_jungl3_j82axH4}`

## Java Winter Wonderland
![image](https://user-images.githubusercontent.com/68913871/123508253-d9ac6f00-d6a0-11eb-9055-1281aeb23b46.png)  

> I first pasted the code into an [online Java compiler](https://www.tutorialspoint.com/compile_java_online.php), which provided me with the following binary output:
```python
11000100110001101100001011000110111010001100110011110110110011001100001011010110110010101011111011001100110110001100001011001110101111101101100011011110110110001011111001110010110001101110010011001000111010100111000001110010011011100110000011001000110101101111001011011110111010100111000001101100011010101111101
```

> I did some simple crypto analysis such as finding for the flag indicator - deleting bits before 01111011 and then running [CyberChef ‘From Binary – 8 bits’](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)&input=MDExMTEwMTEwMTEwMDExMDAxMTAwMDAxMDExMDEwMTEwMTEwMDEwMTAxMDExMTExMDExMDAxMTAwMTEwMTEwMDAxMTAwMDAxMDExMDAxMTEwMTAxMTExMTAxMTAxMTAwMDExMDExMTEwMTEwMTEwMDAxMDExMTExMDAxMTEwMDEwMTEwMDAxMTAxMTEwMDEwMDExMDAxMDAwMTExMDEwMTAwMTExMDAwMDAxMTEwMDEwMDExMDExMTAwMTEwMDAwMDExMDAxMDAwMTEwMTAxMTAxMTExMDAxMDExMDExMTEwMTExMDEwMTAwMTExMDAwMDAxMTAxMTAwMDExMDEwMTAxMTExMTAx). However, it was a fake flag `{fake_flag_lol_9crdu8970dkyou865}`.

> The category of this question is forensic and not crypto thus suggesting a different approach. Upon viewing the java file, there are some unusual whitespaces at the end of some lines of code.

![image](https://user-images.githubusercontent.com/68913871/123508475-512ece00-d6a2-11eb-9d55-e50f617c6c44.png)

> The challenge title and description have words like 'winter' and 'snow', and after some research, I stumbled upon a package called stegsnow. Upon exploration of the documentation, I then ran some commands but it didn't give me the flag.

![image](https://user-images.githubusercontent.com/68913871/123508493-6c014280-d6a2-11eb-89b9-182ad596ad15.png)

> Opening the man page gave me some more options. What caught my attention was Quiet mode (-Q).

![image](https://user-images.githubusercontent.com/68913871/123508575-d4e8ba80-d6a2-11eb-8dd4-dd1aa01f4135.png)

> Running the option -Q gave the flag.

![image](https://user-images.githubusercontent.com/68913871/123508600-fc3f8780-d6a2-11eb-88dd-5d66e0c5cf03.png)

`bcactf{its_whitespace_not_java_smh}`

## Reverse
## Digitally Encrypted 1
![image](https://user-images.githubusercontent.com/68913871/123508667-50e30280-d6a3-11eb-948d-6091b393bb3c.png)  

> The idea is to use the [Digital](https://github.com/hneemann/Digital/releases/latest/download/Digital.zip) program available on GitHub.
 Use the command `java -jar Digital.jar` to run it. Open the circuit_1.dig file.

 ![image](https://user-images.githubusercontent.com/68913871/123508724-ac14f500-d6a3-11eb-8e6b-64fd8a6f061b.png)

> It shows an XOR logic gate with the key and currently the inputs are 0. Change the inputs to those of the encrypted.txt file and observe the different corresponding outputs. (double-click the blue circles)

![image](https://user-images.githubusercontent.com/68913871/123508740-c2bb4c00-d6a3-11eb-9136-a3723b7f8a18.png)

> After completing, this is the output:
```html
6263616374667B74
6861745F7761735F
7072657474795F73
696D706C65313233
393135323733357D
```

> After separation, it corresponds to:
```html
62 63 61 63 74 66 7B 74 68 61 74 5F 77 61 73 5F 70 72 65 74 74 79 5F 73 69 6D 70 6C 65 31 32 33 39 31 35 32 37 33 35 7D
```

> This is of hex format and when [converted to ascii](https://www.rapidtables.com/convert/number/hex-to-ascii.html) gives the flag.

`bcactf{that_was_pretty_simple1239152735}`

## The Opening Gambit
![image](https://user-images.githubusercontent.com/68913871/123508816-3eb59400-d6a4-11eb-97ef-192d3f038bd2.png)  

> Open the file in notepad. We can observe that it has an ELF header. Upon further scrolling, we can see the contents of the code where the flag is embedded.

![image](https://user-images.githubusercontent.com/68913871/123508872-9522d280-d6a4-11eb-8ad3-623044de9bee.png)

`bcactf{w0ol_m4k3s_str1ng_ziv4mk3ca91b}`

## A Fun Game
![image](https://user-images.githubusercontent.com/68913871/123508908-dfa44f00-d6a4-11eb-847f-83d2bb1d3693.png)  

> Extract the exe file using 7Zip and then open the .text file in notepad.

![image](https://user-images.githubusercontent.com/68913871/123508960-40338c00-d6a5-11eb-98b3-271e7905650b.png)

> We can see the string "Here's your flag". Tracing that, we get something that looks like a flag format  
`} s r 3 t t e 1 _ 0 0 0 1 _ e p Y t _ y l 1 a U t c a _ t N d 1 d _ U 0 y _ y l 1 u f 3 p 0 h { f t c a c b`

> Reversing the string, we get the flag.

`bcactf{h0p3fu1ly_y0U_d1dNt_actUa1ly_tYpe_1000_1ett3rs}`

## Web
## Countdown Timer
![image](https://user-images.githubusercontent.com/68913871/123509013-ab7d5e00-d6a5-11eb-85bd-71d6cd7450e9.png)

> This challenge provides us with a countdown timer which claims to give us the flag after 100 days. Clearly, we are not going to wait that long. So, let's go ahead and inspect element.

![image](https://user-images.githubusercontent.com/68913871/123509022-bafca700-d6a5-11eb-9ac4-11d52e4f1307.png)

> We can see that the variable = time, and setting time = 1 will return the flag in 1 second.

![image](https://user-images.githubusercontent.com/68913871/123509030-c5b73c00-d6a5-11eb-8320-7e0e22aff087.png)

`bcactf{1_tH1nK_tH3_CtF_w0u1D_b3_0v3r_bY_1O0_dAy5}`

## Home Automation
![image](https://user-images.githubusercontent.com/68913871/123509041-de275680-d6a5-11eb-872c-48dd14c951c2.png)

> In this challenge, we need to turn off the lights. However, we are currently "vampire", and only "admin" has the permission to do so. This suggests changing cookie, so firstly, inspect element and navigate to the cookie page to see our current cookie name and value.

![image](https://user-images.githubusercontent.com/68913871/123509049-e8495500-d6a5-11eb-83b9-4d36677c5d20.png)

> We can then change the cookie value to “admin” and refresh the page to get the flag.

![image](https://user-images.githubusercontent.com/68913871/123509059-f7c89e00-d6a5-11eb-82ea-02c8b64cbc0d.png)

`bcactf{c00k13s_s3rved_fr3sh_fr0m_th3_smart_0ven_cD7EE09kQ}`

## Wasm Protected Site 1
![image](https://user-images.githubusercontent.com/68913871/123509082-13cc3f80-d6a6-11eb-9269-e628594d07a9.png)

> We start by inspecting element and navigating to the main.js. Here, we can see a wasm library of some sort that contains the code to check for password validity.

![image](https://user-images.githubusercontent.com/68913871/123509088-19298a00-d6a6-11eb-8703-bd0c40fb9701.png)

> Indeed, it is found at the sidebar, and the flag is located at the bottom of the code.

![image](https://user-images.githubusercontent.com/68913871/123509092-23e41f00-d6a6-11eb-9e9f-d450fa07525f.png)

`bcactf{w4sm-m4g1c-xRz5}`

## Agent Gerald
![image](https://user-images.githubusercontent.com/68913871/123509102-35c5c200-d6a6-11eb-9a83-96cd141e3d71.png)

> In this challenge, we are refused entry because we are not Agent Gerald. Webpages know what kind of browser we’re using through “User agent”. Typing `navigator.userAgent` on the console shows the current user, which is selected automatically.

![image](https://user-images.githubusercontent.com/68913871/123509115-4f670980-d6a6-11eb-978f-2ff91f324494.png)

> It can also be found under Network > Headers > Request headers > User-Agent.

![image](https://user-images.githubusercontent.com/68913871/123509123-5c83f880-d6a6-11eb-8bfa-ec952018f436.png)

> To [edit the user agent](https://www.searchenginejournal.com/change-user-agent/368448/#close), click the Triple dot > More tools > Network conditions.

![image](https://user-images.githubusercontent.com/68913871/123509131-686fba80-d6a6-11eb-828c-3d0cebb7c73c.png)

> Untick browser default and key in Agent Gerald as the User agent.

![image](https://user-images.githubusercontent.com/68913871/123509143-71f92280-d6a6-11eb-85c7-e664b64f3faf.png)

> Refresh the page to get the flag.

`bcactf{y0u_h@ck3d_5tegos@urus_1nt3lligence}`

## Movie Login 1
![image](https://user-images.githubusercontent.com/68913871/123509190-95bc6880-d6a6-11eb-855f-09737dbe269c.png)

>Inputs not sanitized suggests login bypass through [SQL injection](https://portswigger.net/support/using-sql-injection-to-bypass-authentication). Enter some appropriate syntax to modify the SQL query into the "Username" input. Input `' or 1=1-- ` into the username field causes the site to perform the query:  
`SELECT * FROM users WHERE username = '' OR 1=1-- ' AND password = 'foo'`

> Because the comment sequence (--) causes the remainder of the query to be ignored, this is equivalent to:  
`SELECT * FROM users WHERE username = ' ' OR 1=1`

`bcactf{s0_y0u_f04nd_th3_fl13r?}`

## Movie Login 2
![image](https://user-images.githubusercontent.com/68913871/123509265-fe0b4a00-d6a6-11eb-833b-3cb0f3e7b384.png)  

> This challenge is a sequel to Movie-Login-1. However, this time, we are also provided with a denylist.json file. From the file, we know that the following characters are rejected in the input field and will yield an error message:  
`"1", "0", "/", "="`

![image](https://user-images.githubusercontent.com/68913871/123509288-21ce9000-d6a7-11eb-89ff-95529055f1e3.png)

> Since the standard `' or 1=1-- ` command is not working because of the presence of `1` and `=`, change the 1=1 to `True` as True is not in the denylist.  
`' or True-- `

`bcactf{h0w_d1d_y0u_g3t_h3r3_th1s_t1m3?!?}`

## Movie Login 3
![image](https://user-images.githubusercontent.com/68913871/123509319-5b070000-d6a7-11eb-9b37-006d1136f1e7.png)  

> This challenge is a sequel to Movie-Login-2. This time, our denylist.json file has more characters:  
`"and", "1", "0", "true", "false", "/", "*", "=", "xor", "null", "is", "<", ">"`

> It is noted that the denylist does not contain `or`, which means it can still be used for the input. Also, although `True` and `1` are forbidden, there are still other values like `2`, `3` which will be recognized as True. So, editing the SQL injection command to `' or 2 or 2-- ` will work just fine.

`bcactf{gu3ss_th3r3s_n0_st0pp1ng_y0u!}`

## [Go to Top](#bcactf-2)
