# [CDDC21 BrainHack](https://cddc-s.cyb0x.com/)

![image](https://user-images.githubusercontent.com/68913871/123534360-42eabb80-d74f-11eb-9cf9-cf32bbc31590.png)

&nbsp; 36 hours Jeopardy-Style  
&nbsp; Thur, 24 June 2021, 10:00 SGT — Fri, 25 June 2021, 22:00 SGT  

**Team Name:** *2p2k*  
**Team Member(s):**
1. *Andre Lee*
2. *Preston Long*
3. *Wee Kiat*
4. *Jun Wei*

**Final Position:** *[61/417](https://user-images.githubusercontent.com/68913871/123620688-144b0e80-d83d-11eb-8353-3f0448d9a9e8.png)*

![image](https://user-images.githubusercontent.com/68913871/123534548-8eea3000-d750-11eb-96a6-faccb3e04b11.png)

**About:** CDDC21 is the reason I got interested in Cyber Security. The courses I took over a 1-month span as part of the event were excellent. They were all well structured and was able to pique interest in a beginner like me, yet pose a fair bit of challenge too. I was extremely excited as this would be my first local CTF. It was organized by DSTA, a well-established government agency. However, this event would prove to be the worst experience I've had so far.    

**Disclaimer:** This is an incomplete writeup, reason being the website was taken down immediately after the event. I did not manage to take all the screenshots of the challenges during the event as navigating the pages was extremely laggy. Much of the time was focused on trying to solve incomplete challenges and I thought the screenshots can be taken once the event was over. I was also constantly on the lookout for those challenges which were only doable for a small window as they were down most of the time.

| Table of Contents |
| --- |
| [Event Breakdown](#event-breakdown) |
| [Other Issues](#other-issues) |
| [Challenges](#challenges) |

# Event Breakdown

This event was actually scheduled to start on 23 June 10:00 SGT. However, due to some technical issues, the event was delayed. The following are the list of errors I faced while trying to login.

![image](https://user-images.githubusercontent.com/68913871/123535718-328b0e80-d758-11eb-9e64-2ba4d87a3042.PNG)

![image](https://user-images.githubusercontent.com/68913871/123535720-34ed6880-d758-11eb-85fc-0f1e27cdf79c.PNG)

![image](https://user-images.githubusercontent.com/68913871/123535723-37e85900-d758-11eb-9d57-5969c654dc64.PNG)

![image](https://user-images.githubusercontent.com/68913871/123535727-3d45a380-d758-11eb-8e3f-d64ad2cb5252.PNG)

Participants were put on hold and told to wait for an announcement 3 hours later at 13:00. At this point of time however, some participants were able to view the questions and started working on them. This wasn't my concern as scoring will only matter to the top teams and I wasn't expecting to place in the top positions given my lack of experience. At 13:00, there was no update and logging in still gave an error. Since this was a local CTF, I decided to be more forgiving and patient so I waited. At around 18:30, I received an email from the organizers stating that my team and I had to re-register for the competition by 18:45, as the event was rescheduled to take place at 19:00. We only had 15 minutes.

![image](https://user-images.githubusercontent.com/68913871/123535789-db396e00-d758-11eb-8a78-bb773104f376.png)

After receiving the news, I immediately notified my team members and followed the instructions to re-register. However, it stated that "The event is not accepting new players". Thankfully, we are not the only ones. Others from the discord server also shared the same issue. So, we waited and tried. After trying for about 20 minutes, I was finally able to register. At 7pm, another announcement was made to reschedule the event to 8pm as there are still teams who have yet to register. This was to be expected as the window they gave was too small and no one would have expected them to ask us to manually re-register. Waited again and at 8pm, I attempted to login but it stated that "The event was stopped". Soon after, an announcement was made, postponing the event to the morning next day, as well as shortening the competition from 48 to 36 hours.

![image](https://user-images.githubusercontent.com/68913871/123536046-839c0200-d75a-11eb-8b3f-ce8babe0e9ce.png)

The next day, I logged in at 10:00 and faced the same authentication issues but was later advised to change the website from https to http.

![image](https://user-images.githubusercontent.com/68913871/123536093-d8d81380-d75a-11eb-8c80-64fcf7a3e016.png)

![image](https://user-images.githubusercontent.com/68913871/123535728-3e76d080-d758-11eb-9148-00f88192514e.PNG)

How ironic, for a cyber security competition to host the event over an insecure protocol. I casted all the negative emotions aside and started attempting the questions.

# Other Issues

This is a list of issues that further worsened the event experience:

During the Event:
- Time to time, the site would crash and log me out for no reason.
- Support team was inactive.
- Challenges were down way too often.
- One challenge was so insecure that others managed to get root access and changed the flag to stop others in their tracks.
- Another was extremely creepy that had others able to message "hi" to me after connecting to the target and port via netcat.
- Other challenges allowed me to view other's attempts which include clicking on their malicious injections.

![image](https://user-images.githubusercontent.com/68913871/123536663-56515300-d75e-11eb-857d-98549dcb4e67.png)

![image](https://user-images.githubusercontent.com/68913871/123536667-5b160700-d75e-11eb-8180-402bd3025440.png)

![image](https://user-images.githubusercontent.com/68913871/123536698-83056a80-d75e-11eb-8552-d039892cb8d5.png)

- Leaked flags found under /flag.txt which allowed teams to score without solving the challenge as intended.

![image](https://user-images.githubusercontent.com/68913871/123536673-5f422480-d75e-11eb-8e90-c71b6a0ad5fc.png)

After the Event:
- Event organizers deleted the entire discord chat history and disconnected everyone.

![image](https://user-images.githubusercontent.com/68913871/123536847-366e5f00-d75f-11eb-8985-927188bb25df.png)

- Too quick to take down the website.

![image](https://user-images.githubusercontent.com/68913871/123536888-6cabde80-d75f-11eb-9aae-b7c34799e4bc.png)

- Did not release the full scoreboard at the end of the event. Had to specially email the organizers to inquire.

![image](https://user-images.githubusercontent.com/68913871/123536829-1dfe4480-d75f-11eb-8cab-96563d7b735a.png)

Eventually, the organizers apologized and explained their position.

![image](https://user-images.githubusercontent.com/68913871/123537191-c660d880-d760-11eb-9966-5decfbbca995.png)

I wish to join next year CDDC22 and hope that the same thing will not happen again.

# Challenges
## AccessKey
![image](https://user-images.githubusercontent.com/68913871/123537359-90702400-d761-11eb-85f3-518714d912ab.png)

> This web challenge bring us to a website, and this is seen after inspecting sources.

![image](https://user-images.githubusercontent.com/68913871/123537373-a54cb780-d761-11eb-84b2-eb4729d7d5ed.png)

> There is a URL encoded string stored as the variable `pass` so I keyed in the variable into the console and copied the result into this [url decoder](https://www.utilities-online.info/urlencode).

![image](https://user-images.githubusercontent.com/68913871/123537379-a8e03e80-d761-11eb-94c1-eb5034f34f97.png)

> We obtain a list of decimal numbers which can then be [converted to ascii](https://onlineasciitools.com/convert-decimal-to-ascii) to give us the flag.

![image](https://user-images.githubusercontent.com/68913871/123537491-4b002680-d762-11eb-9fbf-bd6d66e4609c.png)

`CDDC21{_ De0bfu$cated-F!aG_}`

## Opening the Gate
![image](https://user-images.githubusercontent.com/68913871/123537514-6703c800-d762-11eb-9021-35c04fa1e85c.png)

> This is a Linux based challenge which requires us to login to a target using ssh private key. I initially thought that I had to crack the passphrase using John the Ripper but later realised that the passphrase was provided.

> This is the content of `bot1.key`.

```html
-----BEGIN OPENSSH PRIVATE KEY-----
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
oT2N5+L8xI5riuf/fKLUgBi80zU=
-----END OPENSSH PRIVATE KEY-----
```

> This is the content of Note.txt

```html
Notice

1. As part of the ZIP file, you will find a text file that can be used to connect to the target machine.

2. Each one of the flags is the password for the next user. Your main goal is to access the last user account.

3. The flags are located in the user home folders.

4. The passphrase for the SSH key is: q1w2e3r4
```

> Simply type in the correct command while guessing that the name of the user should be `bot1`. Enter the passphrase `q1w2e3r4` provided and we are now connected to bot1@cybot02. Simple `ls` and `cat` commands provided us with the flag.

![image](https://user-images.githubusercontent.com/68913871/123537582-c06bf700-d762-11eb-8679-3860c4c3994c.png)

`CDDC21{S$H_keYs_are_Be!ter_than_PaSSw0rds}`

## Scrambled Eggs
![image](https://user-images.githubusercontent.com/68913871/123537758-a0890300-d763-11eb-8215-89785727b1ae.png)

> This next challenge is a continuation of the Linux challenge: Opening the Gate. Now, we are expected to switch to user `bot2` using the flag as the password. After switching user with `su` command, we can see a data file in the home folder with read permissions. However, running a `cat` command gave us some gibberish.

> I went ahead and ran `strings` and pipe it with a `grep` command for CDDC21{  
There were numerous flags which aren't the correct flag format as they lack the closing bracers.

![image](https://user-images.githubusercontent.com/68913871/123537860-4c325300-d764-11eb-8f59-7bffa6c7f85e.png)

> So, I refined my search using some simple grep expressions to get the correct flag.

![image](https://user-images.githubusercontent.com/68913871/123537906-93b8df00-d764-11eb-8679-289524c77206.png)

`CDDC21{Th1s_!s_IT}`

## Alarm
![image](https://user-images.githubusercontent.com/68913871/123537962-e4c8d300-d764-11eb-8ebe-e3e4b48dcdd4.png)

> This is a reverse engineering challenge which requires us to key in a correct password to turn off the alarm so as to obtain the flag.

> Upon unzipping and opening the alarm file, I realized that it has an ELF header and proceeded to analyze it using [Ghidra](https://ghidra-sre.org/). After decompiling the main function, this is what I got.

```c
undefined8 main(void)
{
  bool bVar1;
  basic_ostream *this;
  long lVar2;
  char *pcVar3;
  long in_FS_OFFSET;
  allocator<char> local_85;
  int local_84;
  int local_80;
  int local_7c;
  basic_string local_78 [8];
  basic_string local_58 [8];
  char local_38 [4];
  undefined local_34;
  undefined local_33;
  undefined local_32;
  undefined local_31;
  undefined local_30;
  undefined local_2f;
  undefined local_2e;
  undefined local_2d;
  undefined local_2c;
  undefined local_2b;
  undefined local_2a;
  undefined local_29;
  undefined local_28;
  undefined local_27;
  long local_20;

  local_20 = *(long *)(in_FS_OFFSET + 0x28);
  local_38[0] = '\r';
  local_38[1] = 0x36;
  local_38[2] = 4;
  local_38[3] = 0x2a;
  local_34 = 0x7a;
  local_33 = 8;
  local_32 = 0x20;
  local_31 = 0x52;
  local_30 = 0x20;
  local_2f = 0x6f;
  local_2e = 0x2f;
  local_2d = 0x26;
  local_2c = 0x17;
  local_2b = 0x19;
  local_2a = 3;
  local_29 = 0x44;
  local_28 = 0x7d;
  local_27 = 0x3e;
  std::allocator<char>::allocator();
                    /* try { // try from 00400f53 to 00400f57 has its CatchHandler @ 00401139 */
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
            ((char *)local_78,(allocator *)&DAT_00401268);
  std::allocator<char>::~allocator(&local_85);
                    /* try { // try from 00400f6e to 004010ae has its CatchHandler @ 00401164 */
  this = std::operator<<((basic_ostream *)std::cout,
                         "Home Alarm control client. Alarm is currently on. \nEnter password to turn it off"
                        );
  std::basic_ostream<char,std::char_traits<char>>::operator<<
            ((basic_ostream<char,std::char_traits<char>> *)this,
             std::endl<char,std::char_traits<char>>);
  std::operator>>((basic_istream *)std::cin,local_78);
  local_80 = 0x32;
  local_7c = 0x28;
  lVar2 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::size();
  if (lVar2 == 8) {
    pcVar3 = (char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::
                     operator[]((ulong)local_78);
    if (*pcVar3 == 'K') {
      pcVar3 = (char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>
                       ::operator[]((ulong)local_78);
      if (*pcVar3 == 'Z') {
        pcVar3 = (char *)std::__cxx11::
                         basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[]
                                   ((ulong)local_78);
        if (*pcVar3 == 'e') {
          pcVar3 = (char *)std::__cxx11::
                           basic_string<char,std::char_traits<char>,std::allocator<char>>::
                           operator[]((ulong)local_78);
          if (*pcVar3 == 'M') {
            pcVar3 = (char *)std::__cxx11::
                             basic_string<char,std::char_traits<char>,std::allocator<char>>::
                             operator[]((ulong)local_78);
            if ((int)*pcVar3 == local_7c + local_80) {
              pcVar3 = (char *)std::__cxx11::
                               basic_string<char,std::char_traits<char>,std::allocator<char>>::
                               operator[]((ulong)local_78);
              if (*pcVar3 == 'a') {
                pcVar3 = (char *)std::__cxx11::
                                 basic_string<char,std::char_traits<char>,std::allocator<char>>::
                                 operator[]((ulong)local_78);
                if (*pcVar3 == 'S') {
                  pcVar3 = (char *)std::__cxx11::
                                   basic_string<char,std::char_traits<char>,std::allocator<char>>::
                                   operator[]((ulong)local_78);
                  if (*pcVar3 == 'r') {
                    bVar1 = true;
                    goto LAB_00401098;
                  }
                }
              }
            }
          }
        }
      }
    }
  }
  bVar1 = false;
LAB_00401098:
  if (bVar1) {
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string
              (local_58);
                    /* try { // try from 004010bd to 004010c1 has its CatchHandler @ 00401153 */
    dec(local_38,(int)register0x00000020 - 0x58);
                    /* try { // try from 004010c9 to 00401114 has its CatchHandler @ 00401164 */
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
              ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_58);
    puts("Alarm is off!");
    local_84 = 0;
    while (local_84 < 0x12) {
      putchar((int)local_38[local_84]);
      local_84 = local_84 + 1;
    }
    putchar(10);
  }
  else {
    puts("wrong pass!");
  }
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string
            ((basic_string<char,std::char_traits<char>,std::allocator<char>> *)local_78);
  if (local_20 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

> From the code, we can see that the alarm is currently on. Only by executing `LAB_00401098`, will we be able to turn off the alarm. This is only possible if we fulfill all the if statements above. Upon closer analysis of the if statements, we can see that `lVar2` refers to the password length which is 8, and the password is a character array which is dereferenced by `*pcVar3`.

> We can then find the password which goes: `KZeM?aSr`. Here, the `?` is unknown and referring to the code, it is type-casted as `int` and has the value `local_7c + local_80`. Further exploring the code revealed the values of local_80 to be 0x32 and local_7c to be 0x28.

> Applying [hexadecimal addition](https://www.calculator.net/hex-calculator.html?number1=32&c2op=%2B&number2=28&calctype=op&x=57&y=21), we obtain a value of 5A, which when [converted to ascii](https://www.rapidtables.com/convert/number/hex-to-ascii.html), gives us the letter `Z`. Thus, the new password is `KZeMZaSr`. Knowing this information, we then obtain our flag.

![image](https://user-images.githubusercontent.com/68913871/123538599-653d0300-d768-11eb-886d-3cd227a3fb66.png)

`CDDC21{k5JkMxP66d}`

## Never
![image](https://user-images.githubusercontent.com/68913871/123538700-b77e2400-d768-11eb-821e-1f1c4735dcfe.png)

> In this cryptography challenge, we are provided with 2 files: `data` and `gdc_secret`. gdc_secret had an ELF header whereas the data file appears to be more interesting:

```txt
TG\EV^_WVVXG\I^DLG:TG\EV^_WV]TEN_DUV@^;TORBV^WYQCDWQC^DWSP_USUBTCMI^D;wRFTC^X^_PTV[THVBRCH3yUGTCP___PDQHVVXTSHT3yUGTCP___PCU]]X\XTXYTYDKCH^D3=suurKxEny[\nEXEDTUnm__L;
```

> From the challenge description, we can tell that this should be an XOR cipher and they even gave more hints which stated that the length of the key is 6 and the original message contained the word "Never".  
Knowing all these information, we can then proceed to run an [XOR decoder](https://www.dcode.fr/xor-cipher) with key length 6 and look for for the keyword "Never" to obtain the flag.

![image](https://user-images.githubusercontent.com/68913871/123538929-b0a3e100-d769-11eb-9fd7-0150e7c6e4ce.png)

`CDDC21{It_@ll_$tarted_Th3n}`

## Transatlantic
![image](https://user-images.githubusercontent.com/68913871/123538950-c87b6500-d769-11eb-822f-5a1191bad6cb.png)

> This is another cryptography challenge and we are given this text file and expected to decipher the message.

```txt
Gh
Tr!h}DeChisa C D!p_t  bDstn_ ieC_i0h ss230t@  t1nn_r t!{c_td
```

> The challenge description suggests that this is a well-known cipher. And by looking at the name of the challenge, it suggests some form of translation. Skip cipher came to mind and I tried to [decode it](https://www.dcode.fr/skip-cipher) but this was the closest result I got: (I did not include the first line containing `Gh` because there were no readable results.)

```txt
Th!s_3nchat_h@rde best!ripti0n_} CDDC21{!s_n0t_tDC is t
```
> Since the online decoder was unable to brute force the answer for me, I decided to do it manually, and this time, including the line with `Gh`. I realised that it is a cipher that starts at "Tr!h}De`C`hisa" and every subsequent 8th character, including spaces.

> Gh  
Tr!h}De`C`hisa C `D`!p_t  b`D`stn_ ie`C`_i0h ss`2`30t@  t`1`nn_r t!`{`c_td

> It must be noted that there is a space at the end of the 2nd line which must be included in the count, as well as looping to the top line. So, I combined them into a string and wrote a simple python script to solve the encryption.

```python
code = "GhTr!h}DeChisa C D!p_t  bDstn_ ieC_i0h ss230t@  t1nn_r t!{c_td "
flag = ""
length = len(code)
index = 9 #starting point
while True:
    flag+=code[index]
    if code[index] == "}": #end of the flag
        break
    index+=8 #shift by 8
    if index > length -1: #loop back to beginning
        index-=length
print(flag)
```

`CDDC21{Th!s_3ncripti0n_!s_n0t_that_h@rd}`

## [Go to Top](#cddc21-brainhack)
