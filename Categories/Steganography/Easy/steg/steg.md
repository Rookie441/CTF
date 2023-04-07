## steg  

[original_image](https://github.com/Rookie441/CTF/blob/main/Categories/Steganography/Easy/steg/original_image.png)  
[captured_image](https://github.com/Rookie441/CTF/blob/main/Categories/Steganography/Easy/steg/captured_image.png)

> We are given 2 files that looks the same. [Steganographic Calculator](https://futureboy.us/stegano/compinput.html) does not provide anything interesting:

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Steganography/Easy/steg/compare.pl)  

> To solve this, we need to make use of Blind Watermark using [this tool](https://github.com/LYSCUT/https-github.com-linyacool-blind-watermark). After cloning the repository, we just need to place the 2 images in the same directory as decode.py and run the following command:

```bash
python decode.py --original original_image.png --image captured_image.png --result flag.png
```

> Opening the output flag.png, we can see our flag  

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Steganography/Easy/steg/flag.png)  

`CYBERLEAGUE{Y0U_C4NT_533_M3}`
