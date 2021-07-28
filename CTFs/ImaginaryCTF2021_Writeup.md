# [ImaginaryCTF2021](https://2021.imaginaryctf.org/)

<img align="left" width="200" height="175" src="https://user-images.githubusercontent.com/68913871/127268030-8804cadb-df78-4deb-a02f-b0d8745399a7.png">

&nbsp; 96 hours Jeopardy-Style  
&nbsp; Sat, 24 July 2021, 00:00 SGT — Wed, 28 July 2021, 00:00 SGT  

&nbsp; **Team Name:** *Rookie441*  
&nbsp; **Team Member(s):**  
&nbsp; 1. *Lee Wen Bin Andre*  

<br/><br>

| Challenge | Category |
| --- | --- |
| [Formatting](#formatting)	| Misc |
| [Spelling-Test](#spelling-test)	| Misc |
| [Vacation](#vacation) | Misc |
| [stackoverflow](#stackoverflow) | Pwn |

## Formatting

![image](https://user-images.githubusercontent.com/68913871/127269715-17aaa809-c790-4f9c-af97-06d811d7d0bf.png)  
[stonks.py](https://imaginaryctf.org/r/14BD-stonks.py)

```python
#!/usr/bin/env python3

art = '''
                                         88
            ,d                           88
            88                           88
,adPPYba, MM88MMM ,adPPYba,  8b,dPPYba,  88   ,d8  ,adPPYba,
I8[    ""   88   a8"     "8a 88P'   `"8a 88 ,a8"   I8[    ""
 `"Y8ba,    88   8b       d8 88       88 8888[      `"Y8ba,
aa    ]8I   88,  "8a,   ,a8" 88       88 88`"Yba,  aa    ]8I
`"YbbdP"'   "Y888 `"YbbdP"'  88       88 88   `Y8a `"YbbdP"'
'''

flag = open("flag.txt").read()

class stonkgenerator: # I heard object oriented programming is popular
    def __init__(self):
        pass
    def __str__(self):
        return "stonks"

def main():
    print(art)
    print("Welcome to Stonks as a Service!")
    print("Enter any input, and we'll say it back to you with any '{a}' replaced with 'stonks'! Try it out!")
    while True:
        inp = input("> ")
        print(inp.format(a=stonkgenerator()))

if __name__ == "__main__":
main()
```

> This challenge is about format string vulnerability in python which is explained [here.](https://lucumr.pocoo.org/2016/12/29/careful-with-str-format/)  
In essence: whoever controls the format string can access potentially internal attributes of objects.

> If the user can inject format_string here they could discover the secret string like this:  
`{event.__init__.__globals__[CONFIG][SECRET_KEY]}`

![image](https://user-images.githubusercontent.com/68913871/127270247-96d8ac45-03eb-44b2-8eb3-7ca1abc51104.png)

`ictf{c4r3rul_w1th_f0rmat_str1ngs_4a2bd219}`

## Spelling-Test

![image](https://user-images.githubusercontent.com/68913871/127271980-6473a4c6-763e-4430-847b-b8c8f03ca591.png)  
[words.txt](https://imaginaryctf.org/r/CBC8-words.txt)

> Create a python script using the `autocorrect` module to detect misspelled words.

```python
from autocorrect import Speller

spell = Speller(lang='en')
flag = ""

with open("words.txt","r") as myFile:
    for line in myFile:
        if line != spell(line): #Spelling mistake detected
            wrong = list(line[:-1]) #[:-1] to remove newline char
            correct = list(spell(line[:-1]))
            index = 0
            # Find first character difference (misspelled)
            while wrong[index] == correct[index]:
                index+=1
            else:
                flag+=wrong[index]

print(flag)
```

```
ictfyoupassedthespellingtest
```

> Proceed to insert "{}" into the flag where it meets the format.

`ictf{youpassedthespellingtest}`

## Vacation

![image](https://user-images.githubusercontent.com/68913871/127273077-5f92afa4-faab-48ba-a483-2c224fc4ff25.png)  
[image.jpg](https://imaginaryctf.org/r/EA9D-image.jpg)

> We need to find the latitude and longitude of the location where the following picture was taken:

![image](https://user-images.githubusercontent.com/68913871/127273152-104b32d3-cacb-4504-859d-a4b096d221cd.png)

> Explore different parts of the picture by zooming in:

![image](https://user-images.githubusercontent.com/68913871/127274229-74ccac71-71e5-4781-9925-2036abe9f8d3.png)

> City of South Lake Tahoe, California

![image](https://user-images.githubusercontent.com/68913871/127274244-d8a1cbbe-b658-47be-879f-84db209801a6.png)

> Rock Shop, Tahoe Hemp Company

![image](https://user-images.githubusercontent.com/68913871/127274276-5c5084f8-5c5a-4aa3-b1b1-8b6f4bf5af99.png)

> Use [Google Maps](https://www.google.com/maps) and the hints above to find the [location](https://www.google.com.sg/maps/@38.94711,-119.9614202,3a,75y,69.58h,78.62t/data=!3m6!1e1!3m4!1soFk1nXrY9AhpaaIpQOhM2g!2e0!7i16384!8i8192)

![image](https://user-images.githubusercontent.com/68913871/127274283-dfd80982-a2fe-42e3-9ce4-97a9e95e9e2d.png)

> The latitude and longitude can be seen from the url above. `38.94711,-119.9614202`   
Round off to 3 decimal places and include the flag format.

`ictf{38.947_-119.961}`

## stackoverflow

![image](https://user-images.githubusercontent.com/68913871/127276966-9ea4fc38-158e-4f22-ad2a-da8e7a45f235.png)  
[stackoverflow](https://imaginaryctf.org/r/E795-stackoverflow)

> Disassemble the ELF file using Ghidra to get the following code:

```c
undefined8 main(void)

{
  undefined local_38 [40];
  long local_10;

  local_10 = 0x42424242;
  setvbuf(stdout,(char *)0x0,2,0);
  setvbuf(stdin,(char *)0x0,2,0);
  puts(
      "Welcome to StackOverflow! Before you start ~~copypasting code~~ asking good questions, we would like you to answer a question. What\'s your favorite color?"
      );
  __isoc99_scanf(&DAT_001009a3,local_38);
  puts("Thanks! Now onto the posts!");
  if (local_10 == 0x69637466) {
    puts("DEBUG MODE ACTIVATED.");
    system("/bin/sh");
  }
  else {
    puts("ERROR: FEATURE NOT IMPLEMENTED YET");
  }
  return 0;
}
```

> This [youtube link](https://www.youtube.com/watch?v=yH8kzOkA_vw) explains a similar stackoverflow problem.

>  Objective is to get into `DEBUG MODE` where we can access `/bin/sh`. This can happen only if `local_10 == 0x69637466`

![image](https://user-images.githubusercontent.com/68913871/127277239-8ccb5558-6a96-4fab-9f23-0dd612ab3f6d.png)

> `0x69637466 == ftci`  
`undefined local_38 [40]` implies there are 40 element in the array which we must overflow in order to reach `local_10`. This can be done using a python command, using
the cat command to retain the stdin, while piping to the netcat.

> After which, we can using `ls` and `cat` commands to obtain the flag.

![image](https://user-images.githubusercontent.com/68913871/127277273-c0023d99-06eb-4114-82b6-c703ff3188f3.png)

> Manually, it should look something like this:

![image](https://user-images.githubusercontent.com/68913871/127277321-1afbf448-75e2-406e-a4a4-9c9b1588693c.png)

`ictf{4nd_th4t_1s_why_y0u_ch3ck_1nput_l3ngth5_486b39aa}`

## [Go to Top](#imaginaryctf2021)
