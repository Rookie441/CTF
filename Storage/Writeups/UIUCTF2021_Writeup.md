# [UIUCTF2021](https://ctftime.org/event/1372)

<img align="left" width="200" height="175" src="https://user-images.githubusercontent.com/68913871/128167399-bee1608c-555c-4fd3-903c-c7cef6d2f5e0.png">

&nbsp; 48 hours Jeopardy-Style  
&nbsp; Sat, 31 July 2021, 08:00 SGT — Mon, 02 Aug. 2021, 08:00 SGT  

&nbsp; **Team Name:** *Rookie441*  
&nbsp; **Team Member(s):**  
&nbsp; 1. *Andre Lee*  

<br/><br>

| Challenge | Category |
| --- | --- |
| [CEO](#ceo)	| Misc |
| [doot doot](#doot-doot) | Misc |
| [OSINT The Creator](#osint-the-creator)	| Osint |
| [Chaplin PR Nightmare 1 to 7](#chaplin-pr-nightmare-1-to-7) | Osint |


## CEO

![image](https://user-images.githubusercontent.com/68913871/128170258-9153614d-55a6-42f4-a4c0-3f17f03517ec.png)  

> We can read the packets of a .cap file using aircrack-ng which is shown in this [writeup](https://github.com/0awawa0/CTF-Writeups/tree/master/ENCRYPT%20CTF%202019/Forensics/WrEP)

![image](https://user-images.githubusercontent.com/68913871/128170281-c7be66fd-bcfd-4be9-8593-95af5802af98.png)

>  When provided with a dictionary, we can bruteforce the password required for this challenge. Here, we will use [rockyou.txt](https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt)

![image](https://user-images.githubusercontent.com/68913871/128170292-b957a3ec-69aa-43c5-91e1-bdb00557f2fb.png)

`uiuctf{nanotechnology}`

## doot doot

![image](https://user-images.githubusercontent.com/68913871/128170992-4131deb8-6c78-49d9-bfbe-12ddae6bca71.png)  
https://en.wikipedia.org/wiki/List_of_most-viewed_YouTube_videos#Top_videos  
https://www.youtube.com/watch?v=zNXl9fqGX40  

> The challenge brings us to a 9hr-long video about Baby Shark but every time they go 'doo doo doo doo doo doo' the entire Bee Movie script scrolls in a Star Wars style text crawl

> Hint: the flag is in the yellow text, and occurs once in every instance of the yellow text

> Skimmed through and found a chunk of yellow text clumped together but that does not seem to be the flag.

![image](https://user-images.githubusercontent.com/68913871/128171005-107d5a6a-3734-4628-a465-f3cedd406446.png)

> No transcript provided so we have to look for it manually. Flag appeared at 9:56.

![image](https://user-images.githubusercontent.com/68913871/128171012-e18d66cd-7b09-4ac1-b2d4-ca19c9a069f1.png)

`uiuctf{doot_d0ot_do0t_arent_you_tired_of_the_int4rnet?}`

## OSINT The Creator

![image](https://user-images.githubusercontent.com/68913871/128172037-fbc7d867-4c28-4f0c-bb2e-034ee8fe56a9.png)

> Join the [UIUCTF discord](https://discord.gg/uiuctf) and look for the organizer's profile. Found Thomas and we can see a grey box in his "About Me" section.

![image](https://user-images.githubusercontent.com/68913871/128172046-35a7f4c8-af26-4f21-8707-045e9b3b7019.png)

> Click on the "spoiler box" to reveal the flag.

![image](https://user-images.githubusercontent.com/68913871/128172054-7ec7505d-18ee-4745-8ac1-75563d8c72ea.png)

`uiuctf{@b0uT_m3_suppOrT5_maRkD0wN}`

## Chaplin PR Nightmare 1 to 7
### Chaplin PR Nightmare 1
![image](https://user-images.githubusercontent.com/68913871/128172415-f86a53d0-1b1f-43b2-82cd-d604de83a30e.png)

> Find Charlie Chaplin's [twitter](https://twitter.com/ChaplinCoding) account and look for his posts.

![image](https://user-images.githubusercontent.com/68913871/128172424-e575f06d-ec24-4c82-8903-4ebaf7a52651.png)

> Navigate to [/lists](https://twitter.com/ChaplinCoding/lists)

![image](https://user-images.githubusercontent.com/68913871/128172436-9b37f29d-7fe8-4b6f-80d1-422c6716a226.png)

`uiuctf{pe@k_c0medy!}`

### Chaplin PR Nightmare 2
![image](https://user-images.githubusercontent.com/68913871/128172462-fc1d267e-eb4d-4eb5-80e8-cfa255786942.png)


![image](https://user-images.githubusercontent.com/68913871/128172490-abda3c04-3c68-4d33-8d46-4cc043eb87e4.png)

> Navigate to the [Youtube link](youtu.be/LniQBHja9bw) on Charlie's twitter account information.

![image](https://user-images.githubusercontent.com/68913871/128172504-e8aefaa4-4025-472e-9d87-58a297b2db72.png)

`uiuctf{ch@plin_oN_th3_tV!!}`

### Chaplin PR Nightmare 3
![image](https://user-images.githubusercontent.com/68913871/128172536-ddc24acf-036f-4836-bb64-b8fb39a02bf3.png)

> In the About section of Charlie's [Youtube account](https://www.youtube.com/channel/UCxPyHVMa8TyKrOj05x86osA/about), we can see a link to his [website](https://www.charliechaplin.dev/)

![image](https://user-images.githubusercontent.com/68913871/128172548-ee53b976-6f14-4f2c-b22c-bed9f7b2dc9b.png)

> Exploring the website, we see a few images and one of them has the flag written in a computer screen.

![image](https://user-images.githubusercontent.com/68913871/128172572-82a80372-19ba-4ea6-a25d-a7bfca45e581.png)

`uiuctf{ch@pl1n_i5_eL337}`

### Chaplin PR Nightmare 4
![image](https://user-images.githubusercontent.com/68913871/128172592-362816f0-62a4-495d-8944-c71a0c66eac4.png)

> Complete the [form](https://www.charliechaplin.dev/contact) on the website to obtain the flag.

![image](https://user-images.githubusercontent.com/68913871/128172597-c9b105f1-2f13-4829-a56a-4e3a6719e357.png)

`uiuctf{w3_d0_nOt_v@lu3_yoUR_1nPuT}`

### Chaplin PR Nightmare 5
![image](https://user-images.githubusercontent.com/68913871/128172616-ea3a7e5c-2ebe-4baa-985c-6451e824e08b.png)

> Under the [About Us](https://www.charliechaplin.dev/about-us) section, there is an image of Charlie Chaplin with Cane which when clicked, directs us to [this link](https://imgur.com/a/iZI1ov4).

![image](https://user-images.githubusercontent.com/68913871/128172634-4d825a3a-8a3c-49f5-bb55-c80850a4d4d0.png)

> Navigating to the link gives us the imgr account [ChaplinDevelopment](https://imgur.com/user/ChaplinDevelopment)

![image](https://user-images.githubusercontent.com/68913871/128172656-2fd35df9-b523-4928-9b99-a3710fcfeee1.png)

> Exploring the other pictures eventually revealed a flag in the comments section.

![image](https://user-images.githubusercontent.com/68913871/128172667-69efcce2-e0fd-4194-adf7-e1658dd88fc6.png)

`uiuctf{tH3_pR_p0Lic3_h@vE_cAugHt_Up?!}`

### Chaplin PR Nightmare 6
![image](https://user-images.githubusercontent.com/68913871/128172692-d02ab359-20d1-4912-b8d7-fc7fedf8383d.png)

> In Charlie's [website](https://www.charliechaplin.dev/contact), there is a short text at the bottom which reads:

![image](https://user-images.githubusercontent.com/68913871/128172707-3e9dfe1f-a4fa-457b-a56e-c2cbc2be1a9f.png)

> Using the above hint, we managed to find a linkedin group [C3D](https://www.linkedin.com/groups/13984825/).

![image](https://user-images.githubusercontent.com/68913871/128172723-8477ced7-71b0-4a0f-9f25-320f2dbbd78c.png)

> Exploring the group, we can see that the owner is known as Charlie C.

![image](https://user-images.githubusercontent.com/68913871/128172736-29a5fe8b-e2ef-4e9b-a458-485883493e44.png)

> Navigating to Charlie C's [linkedin page](https://www.linkedin.com/in/charlie-chaplin-dev/), we can see that he had previously hosted an event called `Top Hat Development Night`.

![image](https://user-images.githubusercontent.com/68913871/128172752-518a3346-26c0-4935-b3cc-541c1ec004d2.png)

> Search for the [Top hat development night event](https://www.linkedin.com/events/6822753659445743616/) on linkedin.  
The flag can be seen from the About section.

![image](https://user-images.githubusercontent.com/68913871/128172763-5bc143af-6994-4d1c-a19b-a11b753d4f09.png)

`uiuctf{pr0f3s5iOn@l_bUs1n3sS_envIroNm3n7}`

### Chaplin PR Nightmare 7
![image](https://user-images.githubusercontent.com/68913871/128172779-95c019fe-09b1-4a6e-9bdc-2aaf03498ffa.png)

> Locate Charlie C's [Github account](https://github.com/charliechaplindev).

![image](https://user-images.githubusercontent.com/68913871/128172807-9453acbe-a516-4bd1-87d9-d9361d712cb6.png)

> View the [C3d-Official Repository](https://github.com/charliechaplindev/C3D-Official)

![image](https://user-images.githubusercontent.com/68913871/128172821-f1021a79-f23b-4786-80d6-0e093e3ad0d2.png)

> There are 2 open issues and 1 closed issue.

![image](https://user-images.githubusercontent.com/68913871/128172829-2efd9e5e-d2f4-4742-a35e-a67971d7ca46.png)

![image](https://user-images.githubusercontent.com/68913871/128172832-ac981fc4-c353-42a9-b34f-083c8401b9a2.png)

> The name of the closed issue seems interesting. [View it](https://github.com/charliechaplindev/C3D-Official/issues/3) to obtain the flag.

![image](https://user-images.githubusercontent.com/68913871/128172836-d8690f4c-b0fe-42f8-ba3b-44c92b9f6a35.png)

`uiuctf{th3_TrUe_pR_N1gHtm@r3}`

## [Go to Top](#uiuctf2021)
