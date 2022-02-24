# [DownUnderCTF2021](https://ctftime.org/event/1312)

<img align="left" width="200" height="175" src=https://user-images.githubusercontent.com/68913871/134802390-b88491b8-8a36-4f8e-a636-b6a32a247bef.png>

&nbsp; 48 hours Jeopardy-Style  
&nbsp; Fri, 24 Sept. 2021, 17:00 SGT — Sun, 26 Sept. 2021, 17:00 SGT  

&nbsp; **Team Name:** *Rookie441*  
&nbsp; **Team Member(s):**  
&nbsp; 1. *Lee Wen Bin Andre*  
<br/><br>

**Final Position:** *[367/2133](https://user-images.githubusercontent.com/68913871/135020243-7facf0b7-c32d-4d4f-8dbb-0ce6e5785cfa.jpg)*  

| Challenge | Category |
| --- | --- |
| [General Skills Quiz](#general-skills-quiz) | Misc |
| [Rabbit](#rabbit)	| Misc |
| [Substitution Cipher I](#substitution-cipher-i) | Crypto |
| [Inside Out](#inside-out)	| Web |
| [Bad Bucket](#bad-bucket)	| Cloud |
| [Who goes there?](#who-goes-there)	| Osint |

## General Skills Quiz

![image](https://user-images.githubusercontent.com/68913871/134803988-aeb9b974-f913-42a9-ba2b-a7bff563026d.png)

> On the server, we are required to answer a series of questions within a time limit of 30 seconds, which is humanly impossible. Thus, we create a script using pwntools.

```python
#!/usr/bin/python3
from pwn import *
from urllib.parse import unquote
import base64
import codecs

r = remote('pwn-2021.duc.tf', 31905)

#start press enter
line = r.recvuntil(b"...")
print(line.decode("utf-8"))
r.send(b"\n")

#1+1=2
line = r.recvuntil(b"1+1=?")
print(line.decode("utf-8"))
r.sendline(b"2")

#define recv function
def recv():
        line = r.recvuntil(b": ")
        print(line.decode("utf-8"))
        res = r.recvuntil(b"\n")
        res = res[:-1].decode("utf-8")
        print("Input received:",res)
        return res

#define send function
def send(payload):
        print("Output:",payload)
        r.sendline(bytes(str(payload),"ascii"))

#hex to dec
payload = int(recv(),16)
send(payload)

#hex to ascii
payload = chr(int("0x"+recv(),16))
send(payload)

#decode url
payload = unquote(str(recv()))
send(payload)

#from base64
payload = base64.b64decode(recv().encode('ascii'))
payload = payload.decode("utf-8")
send(payload)

#to base64
payload = base64.b64encode(recv().encode('ascii'))
payload = payload.decode("utf-8")
send(payload)

#decode rot13
payload = codecs.decode(recv(), 'rot_13')
send(payload)

#encode rot13
payload = codecs.encode(recv(), 'rot_13')
send(payload)

#binary to decimal
payload = int(recv(),2)
send(payload)

#decimal to binary
payload = bin(int(recv()))
send(payload)

#get flag
line = r.recvuntil(b'?')
print(line.decode("utf-8"))
payload = "DUCTF"
send(payload)
#r.interactive()
line = r.recvuntil(b'//|\\')
print(line.decode("utf-8"))

r.close()
```

> This is the output:

```
[+] Opening connection to pwn-2021.duc.tf on port 31905: Done
Welcome to the DUCTF Classroom! Cyber School is now in session!
Press enter when you are ready to start your 30 seconds timer for the quiz...
Woops the time is always ticking...
Answer this maths question: 1+1=?

Well I see you are not a bludger then.

Decode this hex string and provide me the original number (base 10):
Input received: 0x18
Output: 24
You're better than a dog's breakfast at least.

Decode this hex string and provide me the original ASCII letter:
Input received: 78
Output: x
Come on this isn't hard yakka

Decode this URL encoded string and provide me the original ASCII symbols:
Input received: %22%60%5C
Output: "`\
You haven't gone walkabout yet. Keep going!

Decode this base64 string and provide me the plaintext:
Input received: Z2V0dGluZ19iZXR0ZXJfcHJvZ3JhbW1lX25hdGl2ZQ==
Output: getting_better_programme_native
That's a fair crack of the whip.

Encode this plaintext string and provide me the Base64:
Input received: repository_opera_iraq_ae
Output: cmVwb3NpdG9yeV9vcGVyYV9pcmFxX2Fl
Fair dinkum! That's not bad.

Decode this rot13 string and provide me the plaintext:
Input received: vg_vawhevrf_zvffrq_ox
Output: it_injuries_missed_bk
Don't spit the dummy yet!

Encode this plaintext string and provide me the ROT13 equilavent:
Input received: legislature_sunrise_peers_vulnerability
Output: yrtvfyngher_fhaevfr_crref_ihyarenovyvgl
You're sussing this out pretty quickly.

Decode this binary string and provide me the original number (base 10):
Input received: 0b1011010010101
Output: 5781
Crikey, can you speak computer?

Encode this number and provide me the binary equivalent:
Input received: 7485
Output: 0b1110100111101
You're better than a bunnings sausage sizzle.

Final Question, what is the best CTF competition in the universe?
Output: DUCTF

Bloody Ripper! Here is the grand prize!



   .^.
  (( ))
   |#|_______________________________
   |#||##############################|
   |#||##############################|
   |#||##############################|
   |#||##############################|
   |#||########DOWNUNDERCTF##########|
   |#||########(DUCTF 2021)##########|
   |#||##############################|
   |#||##############################|
   |#||##############################|
   |#||##############################|
   |#|'------------------------------'
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|
   |#|  DUCTF{you_aced_the_quiz!_have_a_gold_star_champion}
   |#|
   |#|
   |#|   
  //|\
[*] Closed connection to pwn-2021.duc.tf port 31905
```

`DUCTF{you_aced_the_quiz!_have_a_gold_star_champion}`

## Rabbit

![image](https://user-images.githubusercontent.com/68913871/134803872-7973bde6-24e4-4ed1-a792-fdf4e23c24e9.png)  
[flag.txt](https://github.com/Rookie441/CTF/files/7231190/flag.txt)

> Run file command on Linux, we see that flag.txt is a bzip2 compressed data.

![image](https://user-images.githubusercontent.com/68913871/134804821-c632a0f3-01a5-4bc9-bd1e-c800dbabce6d.png)

> Proceed to try to decompress...

![image](https://user-images.githubusercontent.com/68913871/134804870-898f4011-e960-4221-ae80-39df6579fc98.png)

> Seems like there are many embedded files. Moreover, it is not limited to bzip2 data. There are also zip files.

![image](https://user-images.githubusercontent.com/68913871/134804882-c5cd9a9c-38e1-4f84-83a2-aed874b07331.png)

> Intended solution involves writing a script as shown [here](https://github.com/DownUnderCTF/Challenges_2021_Public/tree/main/misc/rabbit). However, we will be doing it manually using [7zip](https://www.7-zip.org/download.html).

> These are the steps:

```
1. Rename file extention from .txt to .zip
2. 7zip->Open Archive
3. Ctrl+PgDn for about a minute until reach the end.
4. Open last flag file --> RFVDVEZ7YmFidXNoa2FzX3YwZGthX3dhc19oM3IzfQ==
5. Base64 decode --> DUCTF{babushkas_v0dka_was_h3r3}
```

> Process takes about 1-2 minutes, which is way faster than writing a script. Watch the video [here](https://www.youtube.com/watch?v=MzBfIV-mJwU).

> This method is inspired by a similar challenge I did during BCACTF2.0 - [Infinite Zip](https://github.com/Rookie441/CTF/blob/main/CTFs/BCACTF2.0_Writeup.md#forensics).

> My solution won the "Best Write Up with an Unintended Solution" prize money of AUD$50. [twitter link](https://twitter.com/DownUnderCTF/status/1452544420448858119).

`DUCTF{babushkas_v0dka_was_h3r3}`

## Substitution Cipher I

![image](https://user-images.githubusercontent.com/68913871/134805137-ad9c4da2-d324-4146-b572-a6602a9e5337.png)  
[substitution-cipher-i.sage](https://play.duc.tf/files/30fd220967d9db549f8ad07090043398/substitution-cipher-i.sage?token=eyJ1c2VyX2lkIjo3NjAsInRlYW1faWQiOjQ0MSwiZmlsZV9pZCI6NTZ9.YVBUMg.tOF0e9NDlNbrkP96cyeTkivZK24)  
[output.txt](https://play.duc.tf/files/8cda362b3e7ff0a1e5dc806bb5e30f0f/output.txt?token=eyJ1c2VyX2lkIjo3NjAsInRlYW1faWQiOjQ0MSwiZmlsZV9pZCI6NTd9.YVBUMg.hfeY94njAG2mhpEawo78BkK3BIc)

> This is the contents of the .sage file which shows the encryption algorithm.

```python
def encrypt(msg, f):
    return ''.join(chr(f.substitute(c)) for c in msg)

P.<x> = PolynomialRing(ZZ)
f = 13*x^2 + 3*x + 7

FLAG = open('./flag.txt', 'rb').read().strip()

enc = encrypt(FLAG, f)
print(enc)

```

> This is the contents of output.txt file which is the ciphertext that needs to be decrypted to give us the flag.

```
𖿫𖝓玲𰆽𪃵𢙿疗𫢋𥆛🴃䶹𬑽蒵𜭱𫢋𪃵蒵🴃𜭱𩕑疗𪲳𜭱窇蒵𱫳
```

> With the keywords `sage` and `PolynomialRing`, I stumbled across the [documentation](https://doc.sagemath.org/html/en/tutorial/tour_polynomial.html) as well as an [online interface](https://sagecell.sagemath.org/) where I can test some codes.

> We will adopt a bruteforce approach. Encrypt all printable ascii characters with the given encryption algorithm and store them in a list, then compare them with the ciphertext.

```python
import string
printable_list = string.printable

def encrypt(msg, f):
    return ''.join(chr(f.substitute(c)) for c in msg)

P.<x> = PolynomialRing(ZZ)
f = 13*x^2 + 3*x + 7

enc = encrypt(bytes(printable_list, "ascii"), f)

code_store = list(enc)

ct = "𖿫𖝓玲𰆽𪃵𢙿疗𫢋𥆛🴃䶹𬑽蒵𜭱𫢋𪃵蒵🴃𜭱𩕑疗𪲳𜭱窇蒵𱫳"

for ch in ct:
    if ch in code_store:
        print(printable_list[code_store.index(ch)],end='')
    else:
        print("Non-printable character found!")
```

> Entering the above code in the [online interface](https://sagecell.sagemath.org/) will yield the flag.

`DUCTF{sh0uld'v3_us3d_r0t_13}`

## Inside Out

![image](https://user-images.githubusercontent.com/68913871/134805683-ecd0a23b-ed84-404c-ba48-981d1d0f4bd3.png)

> Navigating to the [link](https://web-inside-out-b3d9f3b9.chal-2021.duc.tf/), we see the following:

![image](https://user-images.githubusercontent.com/68913871/134805749-18000aa4-bde5-4b1a-8507-f9e779c6fcbc.png)

> Viewing page source we can see `/admin` written in comments

```html
<!doctype html>
<title>Index</title>
<link rel="stylesheet" href="/static/style.css">
<section class="content">

  <h1>Index</h1>


    <p>Welcome fellow hackers!</p>
    <p>Need to hide your requests? You're in the right place.</p>
    <p>Send your requests through our server and you'll never be found.</p>
    <a href="/request?url=http://example.com/">Proxy Example</a>
    <br>
    <br>
    <br>
    <br>
    <p><i>We're DEFINITELY not recording your web requests.</i></p>
    <!-- <a href="/admin">Admin Panel</a> -->

</section>
```

> Try to navigate to `/admin` and we are returned with a 403 Forbidden Error.

![image](https://user-images.githubusercontent.com/68913871/134805827-adfa13ee-b915-4c29-806f-0e9438838a39.png)

> It says only accessible from the local network. Keeping that in mind, we look at the proxy example `/request?url=http://example.com` and we get the following json:

```
{"hostname":"example.com","port":80,"redirect_url":"","status":"success","status_code":200,"text":"1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000\n    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00\n    inet 127.0.0.1/8 scope host lo\n       valid_lft forever preferred_lft forever\n    inet6 ::1/128 scope host \n       valid_lft forever preferred_lft forever\n3: eth0@if185: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1460 qdisc noqueue state UP group default \n    link/ether 6e:dd:77:78:50:24 brd ff:ff:ff:ff:ff:ff link-netnsid 0\n    inet 10.96.0.167/32 brd 10.96.0.167 scope global eth0\n       valid_lft forever preferred_lft forever\n    inet6 fe80::6cdd:77ff:fe78:5024/64 scope link \n       valid_lft forever preferred_lft forever\n","title":"Example"}
```

> Initially thought it was a [host header authentication bypass](https://portswigger.net/web-security/host-header/exploiting/lab-host-header-authentication-bypass) but after some googling, [this writeup](https://ctftime.org/writeup/12832) showed me that I can append ip addresses after `?url=` which is relevant in this context as seen in the proxy example earlier on.

> I proceeded to look for ip addresses in the json output and found `127.0.0.1` and `10.96.0.167`. I tried `/request?url=http://127.0.0.1/admin` but was given a Blacklisted Error.

![image](https://user-images.githubusercontent.com/68913871/134806089-a8e26d90-c8bf-44a6-9450-f18fcb515dc8.png)

> There was a loopback as the site was trying to redirect to itself. Hence, we have used the wrong ip. Try the other `/request?url=http://10.96.0.167/admin` and we get the flag embedded in the json output.

```
{"hostname":"10.96.0.167","port":null,"redirect_url":"","status":"success","status_code":200,"text":"<!doctype html>\n<title>Admin Panel</title>\n<link rel=\"stylesheet\" href=\"/static/style.css\">\n<section class=\"content\">\n  \n  <h1>Admin Panel</h1>\n\n  \n    <p>Lmao did they actually think we're not recording their requests \ud83d\ude02</p>\n    <hr>\n    <div>\n      \n        <p>http://0.0.0.0/admin from 679.645.939.511\n</p>\n      \n        <p>http://10.96.1.23/admin from 825.746.912.442\n</p>\n      \n        <p>http://example.com/admin from 463.686.353.735\n</p>\n      \n        <p>http://10.96.0.167 from 944.810.806.628\n</p>\n      \n        <p>http://10.96.0.167/admin from 634.645.444.608\n</p>\n      \n      <p>DUCTF{very_spooky_request}</p>\n    </div>\n    <hr>\n    <i>Yes the IPs are not real</i>\n\n</section>","title":"Admin Panel"}
```

`DUCTF{very_spooky_request}`

## Bad Bucket

![image](https://user-images.githubusercontent.com/68913871/134808969-80a78e18-f90d-497a-b454-64ce6c08e56c.png)

> Navigate to the [link](https://storage.googleapis.com/the-bad-bucket-ductf/index.html), cannot find anything interesting other than a few images of buckets. Since this is a cloud challenge, we know buckets contains objects which can be listed. Here, the bucket name is `the-bad-bucket-ductf`.

> We can make our requests using this [google api](https://cloud.google.com/storage/docs/json_api/v1/objects/list?apix=true#try-it).

![image](https://user-images.githubusercontent.com/68913871/134809123-a446d21c-4553-44a5-b5bc-6f085d2cd143.png)

> Credentials are provided, we do not have to configure it.

![image](https://user-images.githubusercontent.com/68913871/134809141-3004d49b-61dd-4aca-a793-8ca77aa41903.png)

> We get the following json output:

```json
{
  "kind": "storage#objects",
  "items": [
    {
      "kind": "storage#object",
      "id": "the-bad-bucket-ductf/buckets/.notaflag/1631512648813277",
      "selfLink": "https://www.googleapis.com/storage/v1/b/the-bad-bucket-ductf/o/buckets%2F.notaflag",
      "mediaLink": "https://content-storage.googleapis.com/download/storage/v1/b/the-bad-bucket-ductf/o/buckets%2F.notaflag?generation=1631512648813277&alt=media",
      "name": "buckets/.notaflag",
      "bucket": "the-bad-bucket-ductf",
      "generation": "1631512648813277",
      "metageneration": "1",
      "contentType": "text/plain; charset=utf-8",
      "storageClass": "STANDARD",
      "size": "158",
      "md5Hash": "1mwb5duT97D9emOwH0q+sQ==",
      "crc32c": "bw5j5g==",
      "etag": "CN2VhJ+i+/ICEAE=",
      "timeCreated": "2021-09-13T05:57:28.814Z",
      "updated": "2021-09-13T05:57:28.814Z",
      "timeStorageClassUpdated": "2021-09-13T05:57:28.814Z"
    },
    {
      "kind": "storage#object",
      "id": "the-bad-bucket-ductf/buckets/bucket1.jpg/1631512648813815",
      "selfLink": "https://www.googleapis.com/storage/v1/b/the-bad-bucket-ductf/o/buckets%2Fbucket1.jpg",
      "mediaLink": "https://content-storage.googleapis.com/download/storage/v1/b/the-bad-bucket-ductf/o/buckets%2Fbucket1.jpg?generation=1631512648813815&alt=media",
      "name": "buckets/bucket1.jpg",
      "bucket": "the-bad-bucket-ductf",
      "generation": "1631512648813815",
      "metageneration": "1",
      "contentType": "image/jpeg",
      "storageClass": "STANDARD",
      "size": "4695",
      "md5Hash": "HSWKhbWNdJWXMRNQvvHGvw==",
      "crc32c": "nHZj8A==",
      "etag": "CPeZhJ+i+/ICEAE=",
      "timeCreated": "2021-09-13T05:57:28.814Z",
      "updated": "2021-09-13T05:57:28.814Z",
      "timeStorageClassUpdated": "2021-09-13T05:57:28.814Z"
    },
    {
      "kind": "storage#object",
      "id": "the-bad-bucket-ductf/buckets/bucket2.jpg/1631512648717292",
      "selfLink": "https://www.googleapis.com/storage/v1/b/the-bad-bucket-ductf/o/buckets%2Fbucket2.jpg",
      "mediaLink": "https://content-storage.googleapis.com/download/storage/v1/b/the-bad-bucket-ductf/o/buckets%2Fbucket2.jpg?generation=1631512648717292&alt=media",
      "name": "buckets/bucket2.jpg",
      "bucket": "the-bad-bucket-ductf",
      "generation": "1631512648717292",
      "metageneration": "1",
      "contentType": "image/jpeg",
      "storageClass": "STANDARD",
      "size": "62174",
      "md5Hash": "bwtGQScYy9WybBhy2LW8Zw==",
      "crc32c": "i8YdVQ==",
      "etag": "COyn/p6i+/ICEAE=",
      "timeCreated": "2021-09-13T05:57:28.718Z",
      "updated": "2021-09-13T05:57:28.718Z",
      "timeStorageClassUpdated": "2021-09-13T05:57:28.718Z"
    },
    {
      "kind": "storage#object",
      "id": "the-bad-bucket-ductf/buckets/bucket3.png/1631512648816168",
      "selfLink": "https://www.googleapis.com/storage/v1/b/the-bad-bucket-ductf/o/buckets%2Fbucket3.png",
      "mediaLink": "https://content-storage.googleapis.com/download/storage/v1/b/the-bad-bucket-ductf/o/buckets%2Fbucket3.png?generation=1631512648816168&alt=media",
      "name": "buckets/bucket3.png",
      "bucket": "the-bad-bucket-ductf",
      "generation": "1631512648816168",
      "metageneration": "1",
      "contentType": "image/png",
      "storageClass": "STANDARD",
      "size": "116478",
      "md5Hash": "Hckvww7auky6SgjDkfIztw==",
      "crc32c": "0Lcq6g==",
      "etag": "CKishJ+i+/ICEAE=",
      "timeCreated": "2021-09-13T05:57:28.817Z",
      "updated": "2021-09-13T05:57:28.817Z",
      "timeStorageClassUpdated": "2021-09-13T05:57:28.817Z"
    },
    {
      "kind": "storage#object",
      "id": "the-bad-bucket-ductf/buckets/bucket4.png/1631512648815315",
      "selfLink": "https://www.googleapis.com/storage/v1/b/the-bad-bucket-ductf/o/buckets%2Fbucket4.png",
      "mediaLink": "https://content-storage.googleapis.com/download/storage/v1/b/the-bad-bucket-ductf/o/buckets%2Fbucket4.png?generation=1631512648815315&alt=media",
      "name": "buckets/bucket4.png",
      "bucket": "the-bad-bucket-ductf",
      "generation": "1631512648815315",
      "metageneration": "1",
      "contentType": "image/png",
      "storageClass": "STANDARD",
      "size": "80940",
      "md5Hash": "JfdU2mtYtJOSlVwoMjvRCg==",
      "crc32c": "urzSpA==",
      "etag": "CNOlhJ+i+/ICEAE=",
      "timeCreated": "2021-09-13T05:57:28.816Z",
      "updated": "2021-09-13T05:57:28.816Z",
      "timeStorageClassUpdated": "2021-09-13T05:57:28.816Z"
    },
    {
      "kind": "storage#object",
      "id": "the-bad-bucket-ductf/index.html/1631512648715963",
      "selfLink": "https://www.googleapis.com/storage/v1/b/the-bad-bucket-ductf/o/index.html",
      "mediaLink": "https://content-storage.googleapis.com/download/storage/v1/b/the-bad-bucket-ductf/o/index.html?generation=1631512648715963&alt=media",
      "name": "index.html",
      "bucket": "the-bad-bucket-ductf",
      "generation": "1631512648715963",
      "metageneration": "1",
      "contentType": "text/html; charset=utf-8",
      "storageClass": "STANDARD",
      "size": "1790",
      "md5Hash": "JIi5UAeKAC0OYTFHIJ5dSg==",
      "crc32c": "TmyfRg==",
      "etag": "CLud/p6i+/ICEAE=",
      "timeCreated": "2021-09-13T05:57:28.717Z",
      "updated": "2021-09-13T05:57:28.717Z",
      "timeStorageClassUpdated": "2021-09-13T05:57:28.717Z"
    }
  ]
}
```

> We can see something interesting in the storage. There is an object with `"name": "buckets/.notaflag"`. Navigate to `/buckets/.notaflag`, we get our flag.

```
THIS IS A SECRET FILE THAT SHOULD NOT BE SHARED UNDER ANY CIRCUMSTANCE

jk heres the flag good job!

DUCTF{if_you_are_beggining_your_cloud_journey_goodluck!}
```

`DUCTF{if_you_are_beggining_your_cloud_journey_goodluck!}`

## Who goes there?

![image](https://user-images.githubusercontent.com/68913871/134810388-bb927302-628f-4b86-b8e0-d0c7cf9bcb4b.png)

> We are provided with the domain `646f776e756e646572.xyz`. The alphanumeric string is a hexadecimal that translates to ascii `downunder`. Interesting, but will result in a rabbit hole if we were to investigate `downunder.xyz`.

> We can get the information of registered domain names using the [ICANN tool](https://lookup.icann.org/).

> Sadly, no phone numbers under Contact information.

![image](https://user-images.githubusercontent.com/68913871/134810602-618d8211-dbbd-4a0e-a553-c4cb800259c2.png)

> Proceed to view `Raw Registrar RDAP Response`.

```json
{
   "rdapConformance": [
      "rdap_level_0",
      "icann_rdap_response_profile_0",
      "icann_rdap_technical_implementation_guide_0"
   ],
   "objectClassName": "domain",
   "lang": "en",
   "links": [
      {
         "href": "https://rdap.namecheap.com/domain/646f776e756e646572.xyz",
         "rel": "self",
         "type": "application/rdap+json",
         "value": "https://rdap.namecheap.com/domain/646f776e756e646572.xyz"
      }
   ],
   "handle": "D249935594-CNIC",
   "ldhName": "646f776e756e646572.xyz",
   "unicodeName": "646f776e756e646572.xyz",
   "events": [
      {
         "eventAction": "last update of RDAP database",
         "eventDate": "2021-09-26T13:04:52"
      },
      {
         "eventAction": "registration",
         "eventDate": "2021-09-10T11:13:08"
      },
      {
         "eventAction": "expiration",
         "eventDate": "2022-09-10T11:13:08"
      }
   ],
   "status": [
      "client transfer prohibited",
      "server transfer prohibited",
      "add period"
   ],
   "secureDNS": {
      "delegationSigned": false,
      "zoneSigned": false
   },
   "port43": "whois.namecheap.com",
   "publicIds": [
      {
         "type": "NAMECHEAP INC",
         "identifier": "1068"
      }
   ],
   "entities": [
      {
         "objectClassName": "entity",
         "vcardArray": [
            "vcard",
            [
               [
                  "version",
                  {},
                  "text",
                  "4.0"
               ],
               [
                  "fn",
                  {},
                  "text",
                  "NAMECHEAP INC"
               ],
               [
                  "tel",
                  {
                     "Type": [
                        "voice"
                     ]
                  },
                  "uri",
                  "tel:+1.6613102107"
               ],
               [
                  "email",
                  {},
                  "text",
                  "abuse@namecheap.com"
               ]
            ]
         ],
         "roles": [
            "abuse"
         ]
      },
      {
         "objectClassName": "entity",
         "vcardArray": [
            "vcard",
            [
               [
                  "version",
                  {},
                  "text",
                  "4.0"
               ],
               [
                  "fn",
                  {},
                  "text",
                  "NAMECHEAP INC"
               ],
               [
                  "adr",
                  {},
                  "text",
                  [
                     "4600 E Washington St #305",
                     "Phoenix",
                     "Arizona",
                     "85034"
                  ]
               ],
               [
                  "tel",
                  {
                     "Type": [
                        "voice"
                     ]
                  },
                  "uri",
                  "tel:+1.6613102107"
               ],
               [
                  "email",
                  {},
                  "text",
                  "support@namecheap.com"
               ]
            ]
         ],
         "roles": [
            "registrar"
         ]
      },
      {
         "objectClassName": "entity",
         "handle": "ggjq27hogid0g9rk",
         "vcardArray": [
            "vcard",
            [
               [
                  "version",
                  {},
                  "text",
                  "4.0"
               ],
               [
                  "fn",
                  {},
                  "text",
                  "Isa Haxmoore"
               ],
               [
                  "kind",
                  {},
                  "text",
                  "individual"
               ],
               [
                  "adr",
                  {},
                  "text",
                  [
                     "1337 Kaesler Road",
                     "HATHERLEIGH",
                     "SA",
                     "5280",
                     "AU"
                  ]
               ],
               [
                  "tel",
                  {
                     "Type": [
                        "voice"
                     ]
                  },
                  "uri",
                  "tel:+61.420091337"
               ],
               [
                  "email",
                  {},
                  "text",
                  "Isa.Haxmoore@outlook.com"
               ]
            ]
         ],
         "roles": [
            "Registrant"
         ]
      },
      {
         "objectClassName": "entity",
         "handle": "wp0yz45xwv9olpou",
         "vcardArray": [
            "vcard",
            [
               [
                  "version",
                  {},
                  "text",
                  "4.0"
               ],
               [
                  "fn",
                  {},
                  "text",
                  "Isa Haxmoore"
               ],
               [
                  "kind",
                  {},
                  "text",
                  "individual"
               ],
               [
                  "adr",
                  {},
                  "text",
                  [
                     "1337 Kaesler Road",
                     "HATHERLEIGH",
                     "SA",
                     "5280",
                     "AU"
                  ]
               ],
               [
                  "tel",
                  {
                     "Type": [
                        "voice"
                     ]
                  },
                  "uri",
                  "tel:+61.420091337"
               ],
               [
                  "email",
                  {},
                  "text",
                  "Isa.Haxmoore@outlook.com"
               ]
            ]
         ],
         "roles": [
            "Administrative"
         ]
      },
      {
         "objectClassName": "entity",
         "handle": "r0ad7ttvr8rqs7mc",
         "vcardArray": [
            "vcard",
            [
               [
                  "version",
                  {},
                  "text",
                  "4.0"
               ],
               [
                  "fn",
                  {},
                  "text",
                  "Isa Haxmoore"
               ],
               [
                  "kind",
                  {},
                  "text",
                  "individual"
               ],
               [
                  "adr",
                  {},
                  "text",
                  [
                     "1337 Kaesler Road",
                     "HATHERLEIGH",
                     "SA",
                     "5280",
                     "AU"
                  ]
               ],
               [
                  "tel",
                  {
                     "Type": [
                        "voice"
                     ]
                  },
                  "uri",
                  "tel:+61.420091337"
               ],
               [
                  "email",
                  {},
                  "text",
                  "Isa.Haxmoore@outlook.com"
               ]
            ]
         ],
         "roles": [
            "Technical"
         ]
      }
   ],
   "nameservers": [
      {
         "objectClassName": "nameserver",
         "ldhName": "dns1.registrar-servers.com",
         "unicodeName": "dns1.registrar-servers.com"
      },
      {
         "objectClassName": "nameserver",
         "ldhName": "dns2.registrar-servers.com",
         "unicodeName": "dns2.registrar-servers.com"
      }
   ],
   "notices": [
      {
         "title": "RDAP Terms of Service",
         "description": [
            "By querying Namecheap’s RDAP Domain Database, you agree to comply with Namecheap’s RDAP Terms of Service, including but not limited to the terms herein, and you acknowledge and agree that your information will be used in accordance with Namecheap Privacy Policy (https://www.namecheap.com/legal/general/privacy-policy/), including that Namecheap may retain certain details about queries to our RDAP Domain Database for the purposes of detecting and preventing misuse. If you do not agree to any of these terms, do not access or use ,the RDAP Domain Database.",
            "Although Namecheap believes the data to be reliable, you agree and acknowledge that any information provided is 'as is' without any guarantee of accuracy.",
            "You further agree that you will:",
            "1) Not misuse the RDAP Domain Database. It is intended solely for query-based access and should not be used for or relied upon for any other purpose.",
            "2) Not use the RDAP Domain Database to allow, enable, or otherwise support the transmission of unsolicited, commercial advertising or solicitations.",
            "3) Not access the RDAP Domain Database through the use of high volume, automated electronic processes that send queries or data to the systems of Namecheap, any other ICANN-accredited registrar, or any registry operator.",
            "4) Not compile, repackage, disseminate, or otherwise use the information contained in the RDAP Domain Database in its entirety, or in any substantial portion, without our prior written permission.",
            "5) You will only use the information contained in the RDAP Domain Database for lawful purposes.",
            "We reserve the right to restrict or deny your access to the RDAP Domain Database if we suspect that you have failed to comply with these terms.",
            "We reserve the right to modify this agreement at any time."
         ],
         "links": [
            {
               "href": "https://www.namecheap.com/legal/domains/rdap",
               "rel": "alternate",
               "type": "text/html",
               "value": "https://rdap.namecheap.com/policies"
            }
         ]
      },
      {
         "description": [
            "This response conforms to the RDAP Operational Profile for gTLD Registries and Registrars version 1.0"
         ]
      },
      {
         "title": "Status Codes",
         "description": [
            "For more information on domain status codes, please visit https://icann.org/epp"
         ],
         "links": [
            {
               "href": "https://icann.org/epp",
               "rel": "alternate",
               "type": "text/html",
               "value": "https://icann.org/epp"
            }
         ]
      },
      {
         "title": "RDDS Inaccuracy Complaint Form",
         "description": [
            "URL of the ICANN RDDS Inaccuracy Complaint Form: https://www.icann.org/wicf"
         ],
         "links": [
            {
               "href": "https://www.icann.org/wicf",
               "rel": "alternate",
               "type": "text/html",
               "value": "https://www.icann.org/wicf"
            }
         ]
      }
   ]
}
```

> We found the phone number `"tel:+61.420091337"`.

`DUCTF{+61420091337}`

## [Go to Top](#downunderctf2021)
