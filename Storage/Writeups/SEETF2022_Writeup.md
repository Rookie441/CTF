# [SEETF2022](https://ctftime.org/event/1543)

<img align="left" width="200" height="175" src="https://user-images.githubusercontent.com/68913871/172054851-29e8b490-a0cf-481c-a0c0-5a994cf09518.png">

&nbsp; 48 hours Jeopardy-Style  
&nbsp; Sat, 04 June 2022, 00:00 SGT — Mon, 06 June 2022, 00:00 SGT

&nbsp; **Team Name:** *HiddenMeat*  
&nbsp; **Team Member(s):**  
&nbsp; 1. *Rookie441*  
&nbsp; 2. ~~*Tqhreal*~~  
&nbsp; 3. ~~*TCK97*~~  

| Challenge | Category |
| --- | --- |
| [Wayyang](#wayyang)	| Pwn |
| [babyreeee](#babyreeee)	| Rev |
| [BestSoftware](#bestsoftware) | Rev |
| [Sourceless Guessy Web Baby Flag](#sourceless-guessy-web-baby-flag) | Web |
| [Close Enough](#close-enough) | Crypto |
| [Everyone Needs a Break](#everyone-needs-a-break) | Osint |
| [Regex101](#regex101) | Misc |

## Wayyang

![image](https://user-images.githubusercontent.com/68913871/172056907-c2ecd825-dc28-4462-9d7f-810aace19aa5.png)

```python
#!/usr/local/bin/python
import os

FLAG_FILE = "FLAG"

def get_input() -> int:
    print('''                 ,#####,
                 #_   _#
                 |a` `a|
                 |  u  |            ________________________
                 \  =  /           |        WAYYANG         |
                 |\___/|           <     TERMINAL  v1.0     |
        ___ ____/:     :\____ ___  |________________________|
      .'   `.-===-\   /-===-.`   '.
     /      .-"""""-.-"""""-.      \
    /'             =:=             '\
  .'  ' .:    o   -=:=-   o    :. '  `.
  (.'   /'. '-.....-'-.....-' .'\   '.)
  /' ._/   ".     --:--     ."   \_. '\
 |  .'|      ".  ---:---  ."      |'.  |
 |  : |       |  ---:---  |       | :  |
  \ : |       |_____._____|       | : /
  /   (       |----|------|       )   \
 /... .|      |    |      |      |. ...\
|::::/'' jgs /     |       \     ''\::::|
'""""       /'    .L_      `\       """"'
           /'-.,__/` `\__..-'\
          ;      /     \      ;
          :     /       \     |
          |    /         \.   |
          |`../           |  ,/
          ( _ )           |  _)
          |   |           |   |
          |___|           \___|
          :===|            |==|
           \  /            |__|
           /\/\           /"""`8.__
           |oo|           \__.//___)
           |==|
           \__/''')
    print("What would you like to do today?")
    print("1. Weather")
    print("2. Time")
    print("3. Tiktok of the day")
    print("4. Read straits times")
    print("5. Get flag")
    print("6. Exit")

    choice = int(input(">> "))

    return choice


if __name__ == '__main__':
    choice = get_input()

    if choice == 1:
        print("CLEAR SKIES FOR HANDSOME MEN")
    elif choice == 2:
        print("IT'S ALWAYS SEXY TIME")
    elif choice == 3:
        print("https://www.tiktok.com/@benawad/video/7039054021797252399")
    elif choice == 4:
        filename = input("which news article you want babe :)   ")
        not_allowed = [char for char in FLAG_FILE]

        for char in filename:
            if char in not_allowed:
                print("NICE TRY. WAYYANG SEE YOU!!!!!")
                os.system(f"cat news.txt")
                exit()

        try:
            os.system(f"cat {eval(filename)}")
        except:
            pass
    elif choice == 5:
        print("NOT READY YET. MAYBE AFTER CTF????")

```

> It can be noted that the flag file we need to read is named "FLAG". In addition, option 4 looks interesting. It asks for user input and stores it into the variable `filename`. Then, for every character in `filename`, it checks against a list of not_allowed characters (characters of the flag file: F", "L", "A", and "G"). Entering any of them will cause the server to print out news.txt and exit the program, which is not what we want.

![image](https://user-images.githubusercontent.com/68913871/172057249-6c50bb02-0576-4514-a345-5d0c73fd450c.png)

> Also in option 4, there is a try statement `os.system(f"cat {eval(filename)}")`. Thus, we need to get `eval(filename)` to be `FLAG` so that we can run `os.system(cat FLAG)` to get the flag. But our input must not contain "F", "L", "A", or "G" or else the program will terminate prematurely and we are unable to reach the try block.

> Not sure what eval does? Read the [python documentation.](https://python-reference.readthedocs.io/en/latest/docs/functions/eval.html) `eval()` returns a result of the evaluation of a Python expression. It takes in a required expression argument which is a Unicode or Latin-1 encoded `string` and two optional arguments globals and locals. For example:

```
>>> x = 1
>>> print eval('x+1')
2
>>> eval('2*2')
4
>>> eval("len('bamf')")
4
```

> Thus, we can make use of python [ord()](https://www.programiz.com/python-programming/methods/built-in/ord) and [chr()](https://www.programiz.com/python-programming/methods/built-in/chr) to evaluate "FLAG" without using those characters. The `ord()` function returns an integer representing the Unicode character. The `chr()` method converts an integer to its unicode character and returns it.

```
>>> ord("F")
70
>>> ord("L")
76
>>> ord("A")
65
>>> ord("G")
71
>>> eval(chr(70)+chr(76)+chr(65)+chr(71))
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    eval(chr(70)+chr(76)+chr(65)+chr(71))
  File "<string>", line 1, in <module>
NameError: name 'FLAG' is not defined     # This confirms that FLAG is evaluated
```

> Now, netcat to the server and select option 4, followed by entering our payload `chr(70)+chr(76)+chr(65)+chr(71)`

![image](https://user-images.githubusercontent.com/68913871/172057915-026231be-89c4-4ade-b4d0-d18e5a4fb24c.png)

> This should be the intended solution because the challenge title, `wayyang` (or "sucking up") is commonly associated with the Singapore Armed Forces (SAF) where some recruits will strive to act upz in order to get Best Recruit. In the ASCII art, we can also see `WAYYANG TERMINAL 1.0` which points to the popular SAF Ferry Terminal. And we all know that after your service in the SAF, you will be operationally ready and this date is known as `ORD`, thus hinting the use of `ord()`.

> Nevertheless, there are many other ways to solve this challenge. For example, we can use `"flag".upper()` which also evaluates to FLAG

![image](https://user-images.githubusercontent.com/68913871/172057316-9224ce79-b997-4952-be68-cc9ff3069e61.png)

> Even better, we can simply type `"*"`, which will simply evaluate to `*`, running the command `cat *`, thus printing the contents of every file in the current directory

![image](https://user-images.githubusercontent.com/68913871/172059127-e4096dad-c9be-4a80-a3e8-cfb690e7f806.png)

> We can also use `"*/* *"` to print stuffs in other directories as well

![image](https://user-images.githubusercontent.com/68913871/172059242-57e69ddf-9c44-4e71-bc83-16fbe34608db.png)

`SEE{i_love_really_secure_algorithms_b5c0b187fe309af0f4d35982fd961d7e}`

## babyreeee

![image](https://user-images.githubusercontent.com/68913871/172076316-cee1e02b-c2fb-46e0-bc9c-e5ba97724a9b.png)

> First, analyze the given challenge file using the file command in Linux.

![image](https://user-images.githubusercontent.com/68913871/172076365-61077b6c-b7ed-47c0-8cd9-28c7a668dcba.png)

> Since it is an ELF file, we can proceed to decompile using [Ghidra](https://ghidra-sre.org/) and look for interesting functions.

```C

undefined8 FUN_00101080(void)

{
  char *pcVar1;
  undefined4 *puVar2;
  byte bVar3;
  size_t sVar4;
  ulong uVar5;
  ulong uVar6;
  char local_158 [128];
  undefined4 local_d8 [4];
  undefined4 local_c8;
  undefined4 uStack196;
  undefined4 uStack192;
  undefined4 uStack188;
  undefined4 local_b8;
  undefined4 uStack180;
  undefined4 uStack176;
  undefined4 uStack172;
  undefined4 local_a8;
  undefined4 uStack164;
  undefined4 uStack160;
  undefined4 uStack156;
  undefined4 local_98;
  undefined4 uStack148;
  undefined4 uStack144;
  undefined4 uStack140;
  undefined4 local_88;
  undefined4 uStack132;
  undefined4 uStack128;
  undefined4 uStack124;
  undefined4 local_78;
  undefined4 uStack116;
  undefined4 uStack112;
  undefined4 uStack108;
  undefined4 local_68;
  undefined4 uStack100;
  undefined4 uStack96;
  undefined4 uStack92;
  undefined4 local_58;
  undefined4 uStack84;
  undefined4 uStack80;
  undefined4 uStack76;
  undefined4 local_48;
  undefined4 uStack68;
  undefined4 uStack64;
  undefined4 uStack60;
  undefined4 local_38;
  undefined4 uStack52;
  undefined4 uStack48;
  undefined4 uStack44;
  undefined4 local_28;
  undefined4 uStack36;
  undefined4 uStack32;
  undefined4 uStack28;
  undefined4 local_18;
  undefined4 uStack20;
  undefined4 uStack16;
  undefined4 uStack12;

  puts("Hello! Welcome to SEETF. Please enter the flag.");
  local_d8[0] = 0x98;
  local_d8[1] = 0x8b;
  local_d8[2] = 0x88;
  local_d8[3] = 0xc3;
  local_c8 = 0x71;
  uStack196 = 0xb6;
  uStack192 = 0x7e;
  uStack188 = 0xa3;
  local_b8 = 0x72;
  uStack180 = 0xbb;
  uStack176 = 0x73;
  uStack172 = 0x7d;
  local_a8 = 0x7a;
  uStack164 = 0xa9;
  uStack160 = 0x74;
  uStack156 = 0x73;
  local_98 = 0x68;
  uStack148 = 0xa4;
  uStack144 = 0xb6;
  uStack140 = 0x6e;
  local_88 = 0x62;
  uStack132 = 0xbc;
  uStack128 = 0x61;
  uStack124 = 0x61;
  local_78 = 0x62;
  uStack116 = 0xb3;
  uStack112 = 0x67;
  uStack108 = 0xbc;
  local_68 = 0x61;
  uStack100 = 0x6b;
  uStack96 = 0xb8;
  uStack92 = 0xb5;
  local_58 = 0x56;
  uStack84 = 0x54;
  uStack80 = 0x89;
  uStack76 = 0x55;
  local_48 = 0x8c;
  uStack68 = 0x50;
  uStack64 = 0x5b;
  uStack60 = 0x51;
  local_38 = 0x53;
  uStack52 = 0x54;
  uStack48 = 0x5d;
  uStack44 = 0x5e;
  local_28 = 0x50;
  uStack36 = 0x86;
  uStack32 = 0x89;
  uStack28 = 0x89;
  local_18 = 0x48;
  uStack20 = 0x4f;
  uStack16 = 0x49;
  uStack12 = 0xf1;
  fgets(local_158,0x80,stdin);
  sVar4 = strlen(local_158);
  if (sVar4 == 0x35) {
    puts("Good work! Your flag is the correct size.");
    puts("On to the flag check itself...");
    sVar4 = strlen(local_158);
    uVar5 = 0;
    do {
      uVar6 = uVar5 & 0xffffffff;
      if (sVar4 - 1 == uVar5) {
        puts("Success! Go get your points, champ.");
        return 0;
      }
      pcVar1 = local_158 + uVar5;
      puVar2 = local_d8 + uVar5;
      bVar3 = (byte)uVar5;
      uVar5 = uVar5 + 1;
    } while ((byte)*puVar2 == (byte)(*pcVar1 + 0x45U ^ bVar3));
    printf("Flag check failed at index: %d",uVar6);
  }
  else {
    printf("Flag wrong. Try again.");
  }
  return 1;
}
```

> We can see that after the variable declarations and assignments, the line `fgets(local_158,0x80,stdin);` asks for a user input of max size 0x80 and stores in variable local_158. Also, in `sVar4 = strlen(local_158);` sVar4 is assigned to the length of local_158.

> Note that `fgets()` also reads newline character (\n). Since in the C language, strings are terminated by (\0), this means that `strlen()` will include (\n) in the count and cause the length to be 1 more than expected. We can visualize this in an [online C compiler](https://www.onlinegdb.com/online_c_compiler).

![image](https://user-images.githubusercontent.com/68913871/172077142-d673170a-de29-48c9-ac5e-b32794b1121a.png)

> Knowing the length of the string is important because the statement `if (sVar4 == 0x35)` checks for correct length. If length is incorrect, we cannot proceed further.

![image](https://user-images.githubusercontent.com/68913871/172078209-9c59bcfd-abef-45b3-af4b-eaaac1359295.png)

> Now that we know that the length of the flag is 0x35 - 0x1 = `52` (in decimal), we can proceed to test with a bunch of As (52 to be exact).

![image](https://user-images.githubusercontent.com/68913871/172078247-555762d7-c812-4747-9f13-fc10addff4f4.png)

> Now, we see a very useful feedback from the program which tells us which part of our flag has failed the check. In this case, at index 0 which is the case because the flag starts with `SEE{`. Let's modify our payload to see if this is true, keeping in mind that we still have to maintain the flag length of 52.

![image](https://user-images.githubusercontent.com/68913871/172078545-9de622d2-fe9d-4d52-8f23-c8a8d0285895.png)

> Indeed, now the failed index has changed from 0 to 4. Are you thinking what I'm thinking? Yes. Bruteforce!!! Do not feel ashamed of adopting a bruteforce approach, especially if you're a beginner. Of course, remember to abide by the rules. Since this challenge can be done on a local machine, bruteforcing is purely ethical. The script `brute.sh` is as follows:

```python
#!/usr/bin/python3
from pwn import *
import string

flag_known = "SEE{"

while(len(flag_known) < 51): # We also know the flag ends with }
	for char in string.printable:
		p = process('./chall', level='error') # level='error' removes all non-error log messages

		flag_test = flag_known + char*(52-len(flag_known)) # Maintain flag length of 52
		p.sendline(flag_test)

		p.recvuntil(b"Flag check failed at index: ")

		failed_index = int(p.recv().decode("utf-8"))

		if (failed_index == len(flag_known)):
			# Last character failed, restart and try a different ascii printable
			p.close()
		else:
			# failed_index is greater, meaning character matches. Update flag_known and print to terminal			   
			flag_known+=char
			print(flag_known)
			break # break out of inner loop and test next flag index

else:
	flag_known+="}"
	print(flag_known)
	p.close()
```

> Output is generated within seconds.

![image](https://user-images.githubusercontent.com/68913871/172081736-549ccdb4-7111-45a4-be89-77142d577afd.png)

`SEE{0n3_5m411_573p_81d215e8b81ae10f1c08168207fba396}`

## BestSoftware

![image](https://user-images.githubusercontent.com/68913871/172119876-c8f51a3a-495c-4875-a143-170370793240.png)

> After decompiling the executable using [jetbrains](https://www.jetbrains.com/decompiler/), we get the following code:

```java
// Decompiled with JetBrains decompiler
// Type: BestSoftware.Program
// Assembly: Program, Version=0.0.0.0, Culture=neutral, PublicKeyToken=null
// MVID: 77C10122-B016-4734-981A-F7A0DDF50575
// Assembly location: C:\Users\custo\Desktop\SEE\rev_bestsoftware\distrib\BestSoftware.exe

using System;
using System.Security.Cryptography;
using System.Text;

namespace BestSoftware
{
  internal class Program
  {
    private const string SECRET_KEY = "1_l0v3_CSh4rp";

    public static void Main(string[] args)
    {
      Console.WriteLine("===== BestSoftware =====");
      Console.WriteLine("> Checking BestSoftware license...");
      Console.WriteLine("> BestSoftware is unlicensed...");
      Console.WriteLine("> Please enter your name...");
      Console.Write("> ");
      string name = Console.ReadLine();
      Console.WriteLine("> Please enter your email...");
      Console.Write("> ");
      string email = Console.ReadLine();
      Console.WriteLine("> Please enter your license key...");
      Console.Write("> ");
      string licenseKey = Console.ReadLine();
      Console.WriteLine("> Activating BestSoftware license...");
      if (Program.CheckLicenseKey(name, email, licenseKey))
      {
        Console.WriteLine("> Activated BestSoftware license...");
        Console.WriteLine("> The flag is SEE{" + licenseKey + "}...");
      }
      else
        Console.WriteLine("> Activation failed, invalid license key...");
      Console.WriteLine("> Press any key to exit...");
      Console.ReadKey();
    }

    public static bool CheckLicenseKey(string name, string email, string licenseKey)
    {
      string shA256 = Program.CalculateSHA256(name + "1_l0v3_CSh4rp" + email);
      return licenseKey.Equals(shA256);
    }

    public static string CalculateSHA256(string inputString)
    {
      using (SHA256 shA256 = SHA256.Create())
      {
        byte[] hash = shA256.ComputeHash(Encoding.UTF8.GetBytes(inputString));
        StringBuilder stringBuilder = new StringBuilder();
        for (int index = 0; index < hash.Length; ++index)
          stringBuilder.Append(hash[index].ToString("X2"));
        return stringBuilder.ToString();
      }
    }
  }
}
```

> We can see that the program will prompt the user for name, email, followed by the license key. Then, the program will check if the license key is correct through the `CheckLicenseKey` method. If the license key is correct, the flag is printed. Otherwise, the program will feedback that activation has failed.

> In the `CheckLicenseKey` method, the program also calls the `CalculateSHA256` method with the parameter being the concatenation of name, "1_l0v3_CSh4rp", and email. Since we know the name and email from the challenge description, we can proceed to get our parameter which is `seetf1_l0v3_CSh4rpseetf@seetf.sg`

> Then, we can use an [online C# compiler](https://www.programiz.com/csharp-programming/online-compiler/) to pass in our inputString to the `CalculateSHA256` method to get our license key.

![image](https://user-images.githubusercontent.com/68913871/172122095-7617c27c-7119-41d8-ae33-fa7f2b35e366.png)

> Now that we have our license key, we can run the program and enter the required details to get the flag.

![image](https://user-images.githubusercontent.com/68913871/172123043-ccef41de-92c6-4cdc-8a1d-810fb3b77778.png)

`SEE{28F313A48C1282DF95E07BCEF466D19517587BCAB4F7A78532FA54AC6708444E}`

## Sourceless Guessy Web Baby Flag

![image](https://user-images.githubusercontent.com/68913871/172125717-aefc1af1-d304-485e-87da-e2ef3216735a.png)

> Navigating to the link provided, we can see the following

![image](https://user-images.githubusercontent.com/68913871/172126076-1479ffd4-32fc-47eb-be6d-2e2d47ba5723.png)

> When we look at the address bar, we can see `http://sourcelessguessyweb.chall.seetf.sg:1337/?page=whysoserious`. The page parameter seems vulnerable to a [directory traversal attack](https://portswigger.net/web-security/file-path-traversal), otherwise known as [dot-dot-slash attack](https://www.socinvestigation.com/dot-dot-slash-attack-prevention-detection/) or [Local File Inclusion](https://brightsec.com/blog/lfi-attack-real-life-attacks-and-attack-examples/). Basically, it is a web security vulnerability that allows an attacker to read arbitrary files on the server that is running an application.

> For example, we can navigate to `http://sourcelessguessyweb.chall.seetf.sg:1337/?page=../../../../etc/passwd`

![image](https://user-images.githubusercontent.com/68913871/172127065-9f76f31e-a9e6-4f81-8092-12a14f4bf325.png)

> We can notice that the contents have changed to that of /etc/passwd file. However, we still cannot see the flag because of the fancy fading script. However, if we were to inspect elements, we can see the flag.

![image](https://user-images.githubusercontent.com/68913871/172127360-2058d998-a35b-4f73-a2f4-144ff865c3a7.png)

`SEE{2nd_fl4g_n33ds_RCE_g00d_luck_h4x0r}`

## Close Enough

![image](https://user-images.githubusercontent.com/68913871/172127515-316d05d5-9327-4228-a6c2-e0cf012221fa.png)

> The contents of encrypt.py are:

```python
from Crypto.Util.number import getPrime, bytes_to_long
from Crypto.PublicKey import RSA
from secret import flag, getNextPrime

p = getPrime(1024)
q = getNextPrime(p)
n = p * q
e = 65537

key = RSA.construct((n, e)).export_key().decode()

with open("key", "w") as f:
    f.write(key)

m = bytes_to_long(flag.encode())
c = pow(m, e, n)
print(f"c = {c}")
```

> The contents of key is

```
-----BEGIN PUBLIC KEY-----
MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQBKS/xOueb8SyhYskLwm2DT
hofceXDq73pNlu7CAwf1rTYFfYUgbiaKqkOfyTDurLOVXhWnwcmCRo9HwUUEyHG3
swXS5OoSGmHHplMv8crTLlY+/hCpEFnLSPDcnl7HI7a/oprKpCgeiZOphEiIhm8x
UQqivWqZvGzeV9EfjeaAaPlztu3nuRyfccMjqozreU20f8SNSa9wD6vKqtAgvjv3
VapvlRVHRfPvlWCr09VE8W1qzdWvk0XWnyihd+3ssCgKBXpirylAT1WWZk6d3Ryq
bh7biTpeVqzovEFZpQrm2T8Ym6TMRkbImLo9ObEOyVvP3TyUOUtalgDh1iaqHWkn
AgMBAAE=
-----END PUBLIC KEY-----
```

> The ciphertext is

```
4881495507745813082308282986718149515999022572229780274224400469722585868147852608187509420010185039618775981404400401792885121498931245511345550975906095728230775307758109150488484338848321930294974674504775451613333664851564381516108124030753196722125755223318280818682830523620259537479611172718588812979116127220273108594966911232629219195957347063537672749158765130948724281974252007489981278474243333628204092770981850816536671234821284093955702677837464584916991535090769911997642606614464990834915992346639919961494157328623213393722370119570740146804362651976343633725091450303521253550650219753876236656017
```

> You can read more about [how RSA works](https://ctf101.org/cryptography/what-is-rsa/) or read my [previous writeup](https://github.com/Rookie441/CTF/blob/main/Storage/Writeups/BCACTF2.0_Writeup.md#crypto) showing how to calculate each parameter. The emphasis of this writeup however, is to show that after you've learnt the theory, you can explore some tools that can make your life much easier. In this case, we use [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool)

> Simply specify the `--publickey` file and `--uncipher` value and allow the script to do the rest.

![image](https://user-images.githubusercontent.com/68913871/172055807-95d0ba4e-d719-4b32-b004-9608a02b9470.png)

`SEE{i_love_really_secure_algorithms_b5c0b187fe309af0f4d35982fd961d7e}`

## Everyone Needs a Break

![image](https://user-images.githubusercontent.com/68913871/172129729-2d03a1f7-a662-4b32-b657-eae74b2e5fc6.png)

> Here is the photo

![image](https://user-images.githubusercontent.com/68913871/172129800-f5ecba2f-5722-4181-a3c5-4301fae8c373.png)

> Upon close inspection, we can see that there is a pool of water under the shelter which directs us to [prawning activities in Singapore](https://blog.seedly.sg/best-prawning-places-singapore/)

> In the website above, we can see the closest resemblance with `ATC Fishing Village
Address: 241 Jalan Ahmad Ibrahim Singapore, Singapore 629143`

> We can check on google maps to see if we're correct. Indeed, the location where the image is taken is found on this [google maps link](https://www.google.com/maps/@1.3202871,103.7087816,3a,75y,6.27h,82.92t/data=!3m6!1e1!3m4!1sLZT9UsVoahBdLdKjz1Bgtg!2e0!7i16384!8i8192)

![image](https://user-images.githubusercontent.com/68913871/172130351-3c5a5bc5-8431-4e6d-84cb-d1a42ca6251b.jpg)

`SEE{629143}`

## Regex101

![image](https://user-images.githubusercontent.com/68913871/172130576-f7ed6051-79c5-4198-ba5e-9ac52bbcffab.png)  
[flags.txt](https://github.com/Rookie441/CTF/files/8843185/flags.txt)

> As described in the challenge, there are 3000 fake flags in the flag.txt file. Even though the challenge gives us the detailed format of the flag, it is unwise to manually filter out the fake flags. The name of the challenge is directing us to use regex (or regular expressions) to derive the real flag.

> We can use notepad++ search function which has the regular expression option

![image](https://user-images.githubusercontent.com/68913871/172131956-bf03e681-6376-436d-acb6-8d0844771be9.png)

> After reading about the [syntax of Regex](https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html) we derive our payload to be `SEE{[A-Z]{5}[0-9]{5}[A-Z]{6}}`

![image](https://user-images.githubusercontent.com/68913871/172131830-4758481e-6ba2-4591-b22b-1bef29f601f4.PNG)

`SEE{RGSXG13841KLWIUO}`

## [Go to Top](#SEETF2022)
