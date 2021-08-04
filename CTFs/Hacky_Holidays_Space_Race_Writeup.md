# [Hacky_Holidays-SPACE_RACE](https://hackyholidays.io)

<img align="left" width="200" height="200" src="https://user-images.githubusercontent.com/68913871/126026520-8bde8602-ccb2-4946-8485-56fa3fe5ed31.png">

&nbsp; 1 Month Jeopardy-Style  
&nbsp; Fri, 02 July 2021, 18:00 SGT — Mon, 26 July 2021, 18:00 SGT  

&nbsp; [Hackazon Portal Leaderboard.pdf](https://github.com/Rookie441/CTF/files/6877577/Hackazon.Portal.Leaderboard.pdf)

<br/><br/><br/><br/>

**Team Name:** *Rookie441*  
**Team Member(s):**
1. *Lee Wen Bin Andre*

**Final Position:** *210/1042*

| Challenge | Category |
| --- | --- |
| [TEASER su admin](#teaser-su-admin)	| Web |
| [TEASER Locked Out](#teaser-locked-out) | Cloud |
| [BowShock](#bowshock) | Reversing |
| [Enumerating the Cloud](#enumerating-the-cloud) |	Cloud |
| [Quantum Snacks](#quantum-snacks) | Quantum |
| [UFOria](#uforia) | Web, Osint |
| [Space Snacks](#space-snacks) | Misc, Crypto |
| [Unitentifi3d Flying Object](#unitentifi3d-flying-object) | Stego |
| [Stolen Research](#stolen-research) | Forensics |
| [Power Snacks](#power-snacks) | Powershell |
| [Quantum Shuttle](#quantum-shuttle) | Quantum |

**About:** I was intrigued when I noticed that this CTF spanned a duration of 1 month as most CTFs usually lasts for about 2-3 days. I decided to give it a shot and was surprised by the repertoire of categories available such as cloud, powershell and quantum, which were very interesting to solve. Definitely a novel experience and suited for a beginner.

**Disclaimer:** This is not a professional writeup. Its core purpose is to serve as memory and/or personal education.  

# Challenges
## TEASER su admin

![image](https://user-images.githubusercontent.com/68913871/126033313-11ad0817-fced-4d27-aaf5-31b63159c732.png)

![image](https://user-images.githubusercontent.com/68913871/126033316-1bf08a22-62b5-4750-b7a0-50bac70c3cb4.png)

![image](https://user-images.githubusercontent.com/68913871/126033318-f313d1fc-f442-47cb-9ce9-d7b28122fc97.png)

[admin_flag.png](https://user-images.githubusercontent.com/68913871/126033344-ae4ec591-b933-4ae3-a90d-90a7d6a85441.png)

![image](https://user-images.githubusercontent.com/68913871/126033388-0aa650d9-5eac-4fb3-a79d-f4d0477907fb.png)

> Navigate to the required [flag designer URL](https://portal.hackazon.org/flagdesigner)

![image](https://user-images.githubusercontent.com/68913871/126033475-4100a99d-3633-4abf-9bb9-3827a7ea8163.png)

> We have to design the flag such that it looks that the one in the picture shown in [admin_flag](https://user-images.githubusercontent.com/68913871/126033344-ae4ec591-b933-4ae3-a90d-90a7d6a85441.png)  
However, using the settings only allow us to get as far as the image shown below.

![image](https://user-images.githubusercontent.com/68913871/126033476-1ae793cd-47ed-478b-9e0c-4bcfa6e2cb6f.png)

> We are missing out on the black logo in the middle of the flag.  
After further exploration, I realized that overlay #2 is the layer we are looking for. However, out of the 15 choices, none of them represent the logo we are looking for.

![image](https://user-images.githubusercontent.com/68913871/126033480-b7b656ec-b93d-41f6-b1bc-636bc18a7566.png)

> Hence, we inspected elements and see the image source. Here, we can observe that by changing the overlay #2 option, the value of the src changes with respect to the option number. Thus, we manually change the value to 15, which is the 16th choice to get the logo we need.

![image](https://user-images.githubusercontent.com/68913871/126033481-42077f96-93d5-4803-95be-a9248a7fd379.png)

![image](https://user-images.githubusercontent.com/68913871/126033485-c958e542-6288-4fba-85e2-cf89d1fe8068.png)

`CTF{YOU-HAZ-ADMIN-FLAG}`

### [Go to Top](#hacky_holidays-space_race)

## TEASER locked out

![image](https://user-images.githubusercontent.com/68913871/126036373-b2838579-da17-4bbf-bbb8-80fd02057e2e.png)

![image](https://user-images.githubusercontent.com/68913871/126036375-05397999-0da7-47d0-9d39-64c6b4d55057.png)

![image](https://user-images.githubusercontent.com/68913871/126036379-22d76999-1b99-45e5-90ca-46c40fd88b52.png)

> Navigate to the [external storage](https://external-spaceship-storage-b38e8c6.s3-eu-west-1.amazonaws.com/). We see the following XML file:

```xml
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<Name>external-spaceship-storage-b38e8c6</Name>
<Prefix/>
<Marker/>
<MaxKeys>1000</MaxKeys>
<IsTruncated>false</IsTruncated>
<Contents>
<Key>external-spaceship-storage.txt</Key>
<LastModified>2021-06-24T18:36:04.000Z</LastModified>
<ETag>"0acc4ebca6124adf3f29d5be7ababed8"</ETag>
<Size>89</Size>
<StorageClass>STANDARD</StorageClass>
</Contents>
</ListBucketResult>
```
> An interesting thing to note is the key tag that shows a txt file. Append `/external-spaceship-storage.txt` to the given URL and use the curl command to get the contents.

![image](https://user-images.githubusercontent.com/68913871/126036491-158090df-9b7a-4d08-ba1a-15fefbcde2ad.png)

`CTF{6c2c45330a85b126f551}`

![image](https://user-images.githubusercontent.com/68913871/126036541-62fd60a9-b8a1-472a-ab3e-834ea80b8e90.png)

> I found a useful link to list buckets, folders or objects using the [s3 ls command](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html)  
I went ahead and execute the command but was given an error `SignatureDoesNotMatch`.

![image](https://user-images.githubusercontent.com/68913871/126036604-c414ebe7-919b-491e-aa2d-743f4cce8d0f.png)

> After some more googling, I realized that I first have to provide the Access Key ID and Secret Access Key using [aws configure](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html), which are given to us in the previous question.

![image](https://user-images.githubusercontent.com/68913871/126036842-4067d0be-5d8d-48a5-9204-d804da9d122c.png)

> We have successfully listed the key in external-spaceship-storage. However, the question requires us to get inside and check the internal spaceship storage.  
My first instinct was to change the url from `external` to `internal`.

![image](https://user-images.githubusercontent.com/68913871/126036885-c444c4fe-1a2a-41db-8235-0800ac76dc9b.png)

> I received an error `NoSuchBucket`. This meant that the name of the bucket I provided was invalid. I need to find a way to get the name of available buckets.  
This can be done using [list-buckets](https://docs.aws.amazon.com/cli/latest/reference/s3api/list-buckets.html) which I found in the [aws s3api documentation](https://docs.aws.amazon.com/cli/latest/reference/s3api/index.html). After knowing the name of the bucket, I can then use `aws s3 ls` to list the contents and found `spaceship-keys`.

![image](https://user-images.githubusercontent.com/68913871/126037008-55e6ff2a-ef95-42ec-baba-561dd294b0b8.png)

> Since it is a folder and not a .txt file, we need to cp to our created flagfolder

![image](https://user-images.githubusercontent.com/68913871/126037511-9a62fe41-11b5-41da-90d4-74d0ca019bc3.png)

`CTF{4ababede5580d9a22a2a}`

### [Go to Top](#hacky_holidays-space_race)

## BowShock

![image](https://user-images.githubusercontent.com/68913871/126037533-1cf9c410-8822-48d7-9c66-0a3504e640b9.png)

![image](https://user-images.githubusercontent.com/68913871/126037535-bebfde4a-4ec6-4405-93f5-1b60eb4195cc.png)

![image](https://user-images.githubusercontent.com/68913871/126037537-4747ad67-73a3-4273-9afc-3f484cdb0b5c.png)

[BowShock.jar](https://portal.hackazon.org/files/bfb155f97c39ecb22540844bd3321cfd91da8ef2/BowShock.jar)

![image](https://user-images.githubusercontent.com/68913871/126037584-38c1cf8b-16f2-4f15-a26f-f1399ace5fc0.png)

> We can decompile a .jar file using [this](https://jdec.app/) tool. We get the following output:

```java
/* Decompiler 4ms, total 256ms, lines 50 */
import java.util.InputMismatchException;
import java.util.Scanner;

class BowShock {
   public static int totalInput;

   public static int getInput() {
      System.out.println("Set the amount of plasma to the correct amount to minimize bow shock: ");
      Scanner var0 = new Scanner(System.in);

      int var1;
      while(true) {
         try {
            var1 = var0.nextInt();
            break;
         } catch (InputMismatchException var3) {
            System.out.print("Invalid input. Please reenter: ");
            var0.nextLine();
         }
      }

      totalInput += var1;
      return var1;
   }

   public static void bowShock() {
      System.out.println("And all was dust in the wind.");
      System.exit(-99);
   }

   public static void main(String[] var0) {
      System.out.println("Oh damn, so much magnetosphere around here!");
      if (getInput() != 333) {
         bowShock();
      }

      System.out.println("We survive another day!");
      if (getInput() != 942) {
         bowShock();
      }

      if (getInput() != 142) {
         bowShock();
      }

      System.out.println("Victory!");
      System.out.println("CTF{bowsh0ckd_" + totalInput + "}");
   }
}
```

> From the code, we can see that the flag is CTF{bowsh0ckd_`totalInput`}, where `totalInput` is unknown.  
Upon further analysis, we can also see that the bowShock() function is executed when our getInput() does the correspond to the required value. This causes System.exit.

> Also note the line `totalInput += var1;`. Thus, this suggests that the value of totalInput will continually add up, which gives us the value of 333+942+142 = 1417

`CTF{bowsh0ckd_1417}`

### [Go to Top](#hacky_holidays-space_race)

## Enumerating The Cloud

![image](https://user-images.githubusercontent.com/68913871/126038023-184096a7-be34-4993-a93c-72f4a07677cc.png)

![image](https://user-images.githubusercontent.com/68913871/126038028-13187b1e-8b96-4360-a930-7de0e54e5835.png)

![image](https://user-images.githubusercontent.com/68913871/126038031-8cd8badc-3aca-4b79-85ee-ee6de9e080bc.png)

> Navigate to the [spaceship](http://planet-bucket-43b2a07.s3-website-eu-west-1.amazonaws.com/). Other than a picture of a rocket in space, there isn't anything interesting to see. Hence, I inspected element and after some exploring, I found something interesting in Network > Initiator.

![image](https://user-images.githubusercontent.com/68913871/126038039-35fa8367-0f9d-48b6-92a8-18475abad7e5.png)

> There is a new bucket which can be explored further.

![image](https://user-images.githubusercontent.com/68913871/126038041-bc84597d-958c-42c3-85a4-162042bbfd91.png)

> Navigate to [rocket-bucket](https://rocket-bucket-723aa76.s3.amazonaws.com). We see the following XML file:

```xml
<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<Name>rocket-bucket-723aa76</Name>
<Prefix/>
<Marker/>
<MaxKeys>1000</MaxKeys>
<IsTruncated>false</IsTruncated>
<Contents>
<Key>external-information-panel.txt</Key>
<LastModified>2021-06-24T19:24:39.000Z</LastModified>
<ETag>"d18c834974b76e5e2a02d27b5f5f2a67"</ETag>
<Size>60</Size>
<StorageClass>STANDARD</StorageClass>
</Contents>
<Contents>
<Key>flag.txt</Key>
<LastModified>2021-06-24T19:24:39.000Z</LastModified>
<ETag>"ebfd1e6eb5d2bd7daf1facf9f81c2689"</ETag>
<Size>45</Size>
<StorageClass>STANDARD</StorageClass>
</Contents>
<Contents>
<Key>rocket_bucket.png</Key>
<LastModified>2021-06-24T19:24:38.000Z</LastModified>
<ETag>"2b6e9f2e40e4ba07e6530f4e8dff83bb"</ETag>
<Size>31428</Size>
<StorageClass>STANDARD</StorageClass>
</Contents>
</ListBucketResult>
```

> We can see a key named flag.txt. Get the flag by appending `/flag.txt` to the URL.  
https://rocket-bucket-723aa76.s3.amazonaws.com/flag.txt

`CTF{0841862f273fd2ca20ea3b94a645781071ab19d7}`

![image](https://user-images.githubusercontent.com/68913871/126038441-0e34c357-2eba-40ef-871a-90261ad3fb67.png)

> Another interesting key in the above XML file is external-information-panel.txt.  
Navigate to https://rocket-bucket-723aa76.s3.amazonaws.com/external-information-panel.txt and we get the following link:

```txt
https://g0341x75tb.execute-api.eu-west-1.amazonaws.com/logs
```

> Navigating to the link gives us the error `405 Request method 'GET' not allowed`. This suggests that we need to change the [HTTPS request methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods).

> This can be done using [Burp Suite](https://portswigger.net/burp). Change GET request to PUT. The PUT method replaces all current representations of the target resource with the request payload.

![image](https://user-images.githubusercontent.com/68913871/126038567-a7fb73a0-3f6e-4e31-aa14-d090029aa116.png)

> The flag is embedded in the first few lines of the response:

```InputMismatchExceptionHTTP/2 200 OK
Date: Thu, 08 Jul 2021 07:01:12 GMT
Content-Type: text/plain; charset=utf-8
Content-Length: 7752
Apigw-Requestid: CI5c3h0EjoEEPNA=

The periscope data is optimal. Have a flag for your effort: CTF{9177a9c8bb1cd5c85934}.<br>
[
    {
        "Id": "dfa0f62de13a1719d125ac2f3382543067701c5031289006c8170d3bab33994a",
        "Created": "2021-06-24T17:33:58.623969048Z",
        "Path": "/bin/bash",
        "Args": [],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 154123,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2021-06-24T17:33:59.110711065Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:0df4a5c988ef613a6208ed14e7bc6fc12433f8d0fc3954c2dfc2fb8ee92da3bb",
        "ResolvConfPath": "/var/lib/docker/containers/dfa0f62de13a1719d125ac2f3382543067701c5031289006c8170d3bab33994a/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/dfa0f62de13a1719d125ac2f3382543067701c5031289006c8170d3bab33994a/hostname",
        "HostsPath": "/var/lib/docker/containers/dfa0f62de13a1719d125ac2f3382543067701c5031289006c8170d3bab33994a/hosts",
        "LogPath": "/var/lib/docker/containers/dfa0f62de13a1719d125ac2f3382543067701c5031289006c8170d3bab33994a/dfa0f62de13a1719d125ac2f3382543067701c5031289006c8170d3bab33994a-json.log",
        "Name": "/musing_herschel",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": null,
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {},
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/e477d4ab9d51efce36b43fdaef194bee5da248d85b01bacde2aea1e7d140bfa7-init/diff:/var/lib/docker/overlay2/ff7ce56c606465fe889eb3726103d9f95123caff68a64764bb2b9edb837a332e/diff:/var/lib/docker/overlay2/584993a5c026ea9eb4378504366be08e4d2aba25790928f993fd594fed00bb96/diff:/var/lib/docker/overlay2/9716217cfc5718574d82efce50de50dfad4e17bf888408b01894b8727232c02d/diff",
                "MergedDir": "/var/lib/docker/overlay2/e477d4ab9d51efce36b43fdaef194bee5da248d85b01bacde2aea1e7d140bfa7/merged",
                "UpperDir": "/var/lib/docker/overlay2/e477d4ab9d51efce36b43fdaef194bee5da248d85b01bacde2aea1e7d140bfa7/diff",
                "WorkDir": "/var/lib/docker/overlay2/e477d4ab9d51efce36b43fdaef194bee5da248d85b01bacde2aea1e7d140bfa7/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [],
        "Config": {
            "Hostname": "dfa0f62de13a",
            "Domainname": "",
            "User": "",
            "AttachStdin": true,
            "AttachStdout": true,
            "AttachStderr": true,
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Env": [
                "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "AWS_SECRET_ACCESS_KEY=dpmlpQnMgZFZ5Nt8k7AkCTizqGrY84ZRW55lo+52",
                "AWS_ACCESS_KEY_ID=AKIA552OOUKCBWDIUCWS"
            ],
            "Cmd": [
                "/bin/bash"
            ],
            "Image": "0df4a5c988ef",
            "Volumes": null,
            "WorkingDir": "",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {}
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "bf51d811c4e9c7857bc50968fca735fbd8df34759e0169203ef7164cffdaee69",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {},
            "SandboxKey": "/var/run/docker/netns/bf51d811c4e9",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "9aa6994b3efb337422b98c9c9fabef444a1803eb47dfe15755c6544596f83fda",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.2",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:02",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "81a709997e1724facaaa40eb14889840b1ff603dc83a9f9964150a0c3cf26b3c",
                    "EndpointID": "9aa6994b3efb337422b98c9c9fabef444a1803eb47dfe15755c6544596f83fda",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.2",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:02",
                    "DriverOpts": null
                }
            }
        }
    }
]
```

`CTF{9177a9c8bb1cd5c85934}`

![image](https://user-images.githubusercontent.com/68913871/126038659-c598f66a-ce27-4a9d-954d-9c35df784660.png)

> From the above response, we can get the following AWS_SECRET_ACCESS_KEY and AWS_ACCESS_KEY_ID:

```
"AWS_SECRET_ACCESS_KEY=dpmlpQnMgZFZ5Nt8k7AkCTizqGrY84ZRW55lo+52",
"AWS_ACCESS_KEY_ID=AKIA552OOUKCBWDIUCWS"
```

> We can then proceed to `aws configure` as well as list the available buckets.

![image](https://user-images.githubusercontent.com/68913871/126038709-c5d1be6c-2c87-448a-b4e1-d72d7e860875.png)

> We can also use the `aws s3 ls` command.

![image](https://user-images.githubusercontent.com/68913871/126038726-af2afd89-c43f-455f-bf2e-a93e57faf2f5.png)

> The challenge required us to get the tag in the cleaning bucket. This can be done using [get-bucket-tagging](https://docs.aws.amazon.com/cli/latest/reference/s3api/get-bucket-tagging.html)

![image](https://user-images.githubusercontent.com/68913871/126038776-afc56619-8de0-42d7-9099-072aa337844a.png)

`CTF_855cc724fd34896c8875`

### [Go to Top](#hacky_holidays-space_race)

## Quantum Snacks

![image](https://user-images.githubusercontent.com/68913871/126038879-ff79cc25-ac10-4957-a32e-6a7e3eb8fdf1.png)

![image](https://user-images.githubusercontent.com/68913871/126038880-816bb644-b182-4611-bfb0-1c0731d599fc.png)

![image](https://user-images.githubusercontent.com/68913871/126038883-034b1c0d-e8b4-4d64-8e49-9db191bb2217.png)

![image](https://user-images.githubusercontent.com/68913871/126038890-8b847a39-9f04-4ff1-8673-5cb03191f7ef.png)

![image](https://user-images.githubusercontent.com/68913871/126038891-2d90c6ef-6446-4581-893d-7fa0dc2516b8.png)

```python
2**3 = 8
```

`8`

![image](https://user-images.githubusercontent.com/68913871/126039568-af4306e7-3104-4ac1-b485-bd2142c1666a.png)

> We are required to use matrix multiplication to get a combination of H and X operations that can change the state from init`(1,0)` to target`(-1,0)`.

> We can make use of python `numpy` module to do matrix multiplication instead of manually keying in a graphic calculator or using pen and paper. The following is the code I wrote:

```python
import numpy as np
import math

init = np.array([[1],
                 [0]])
target = np.array([[-1],
                   [0]])

H = (1/math.sqrt(2))*np.array([[1,1],
                               [1,-1]])
X = np.array([[0,1],
              [1,0]])

def applyHX(combi):
    res = init
    for i in combi:
        if i=="X":
            res = np.matmul(X,res)
        elif i=="H":
            res = np.matmul(H,res)
    return res
```
> We can proceed to explore by using the `applyHX` function created.

![image](https://user-images.githubusercontent.com/68913871/126039735-cd4fe1ea-8c8a-4825-8c2e-deca65cf8efc.png)

> Here, we see that `X` alone swaps the top and bottom. `H` alone does not give us target. So, proceed to try combination of 2 to see what it does.

![image](https://user-images.githubusercontent.com/68913871/126039768-4d016e29-6adf-4c19-98b6-9da337d1043b.png)

> `XH` interesting as it brings the negative which is present in our `target`.

> After some trial and error, we get the combination `XHXHX` which gives us the target`(-1,0)`. We can then obtain the flag using the [checker](https://282184fcf85d294cc51692e55a2b1235.challenge.hackazon.org/) provided.

![image](https://user-images.githubusercontent.com/68913871/126039821-725c2a84-8a5a-4e52-a042-cfbeb59824fc.png)

`CTF{quantum_circuit_master}`

![image](https://user-images.githubusercontent.com/68913871/126039896-b396e6e6-9f35-41f1-a710-0d0f214d1d96.png)

> Now, we are allowed to use an additional operation `Z`. Thus, we edit our above code to the following:

```python
import numpy as np
import math

init = np.array([[1],
                 [0]])
target = np.array([[-1],
                   [0]])

H = (1/math.sqrt(2))*np.array([[1,1],
                               [1,-1]])
X = np.array([[0,1],
              [1,0]])

Z = np.array([[1,0],
              [0,-1]])

def applyHXZ(combi):
    res = init
    for i in combi:
        if i=="X":
            res = np.matmul(X,res)
        elif i=="H":
            res = np.matmul(H,res)
        elif i=="Z":
            res = np.matmul(Z,res)
    return res
```

> Exploring the `Z` operation, we noticed that it alone does not do anything.

![image](https://user-images.githubusercontent.com/68913871/126039969-d4464642-327f-4069-b770-debe77ab82d1.png)

> With the addition of Z, let's see combinations of 2 to find anything interesting.

![image](https://user-images.githubusercontent.com/68913871/126039992-023e6c75-eabb-45a0-a1df-c1ee7a18a19c.png)

> We can proceed to explore combinations of 3 to find out more but here we can see `HZ` and `XZ` gives us negative, which is present in target`(-1,0)`. But `XZ` gives us closer to the answer.  
In fact, we just need to flip it, so we append an `X` to get `XZX` as the solution.

> We can then obtain the flag using the [checker](https://282184fcf85d294cc51692e55a2b1235.challenge.hackazon.org/) provided.

`XZX`

### [Go to Top](#hacky_holidays-space_race)

## UFOria

![image](https://user-images.githubusercontent.com/68913871/126040140-9084135d-200c-4bb0-92dd-6841d9b8e862.png)

![image](https://user-images.githubusercontent.com/68913871/126040142-cadb0194-3078-4798-a645-aa07f34d8878.png)

![image](https://user-images.githubusercontent.com/68913871/126040143-cb846c3e-82ca-477c-a044-fa2d3720b5a8.png)

![image](https://user-images.githubusercontent.com/68913871/126040148-e092a0a4-1c5f-41cb-b15e-6e8bcdf8f384.png)

> Navigating to the [link](https://fdac14c304cd49c16b0c74573779cedb.challenge.hackazon.org/) provided, we see the following:

![image](https://user-images.githubusercontent.com/68913871/126040151-2a3dea6e-859d-40e1-9f56-25051dd8ed37.png)

> Only the Fleet ticket is interactable and upon clicking the `Contact us` button, there is a javascript alert prompting us for the invite code which we do not have.

![image](https://user-images.githubusercontent.com/68913871/126040157-8fafdb53-b798-4038-890a-366e69898c83.png)

> Upon inspecting the source code, I found an interesting section regarding the `contactus` button.

```javascript
<script>
    function contactus() {
        var code = prompt("This option is invitation only. Enter your invite code:");

        var verify = (function(code) {
            if (code.length != 12) { return false; }

            var parts = [code.substr(0,3), code.substr(4,4), code.substr(9,3)];
            if (parts.join("-") != code) { return false; }

            if (parts[0] != "UFO") { return false; }
            if (parts[1] != btoa("UFO")) { return false; }
            if (parts[2] != ("UFO".charCodeAt(0) + "UFO".charCodeAt(1) + "UFO".charCodeAt(2))) { return false; }

            return true;
        })(code);

        if (verify) {
            alert("Great, please continue the booking process by sending us an email with your invitation code.")        
        } else {
            alert("Wrong invite code.")
        }
    }
</script>
```

> Since I am not too familiar with javascript, I found this useful [online compiler](https://jsfiddle.net/) where I can paste the code.

> `code.length` tells us that the code is 12 characters long.  
`var parts` tells us that the code is in the form xxx-xxxx-xxx  
`parts[0]` tells us that the First 3 characters are --> `UFO`  
`parts[1]` tells us that the Next 4 characters are --> btoa("UFO") --> `VUZP`  
`parts[2]` tells us that the Last 3 characters are --> ("UFO".charCodeAt(0) + "UFO".charCodeAt(1) + "UFO".charCodeAt(2)) -->  `234`.

> Combining them together, we get the final invite code as `UFO-VUZP-234`. We can proceed to verify the code by keying into the javascript alert to obtain the flag.

`UFO-VUZP-234`

![image](https://user-images.githubusercontent.com/68913871/126041023-3578d9b2-cba0-40de-8f10-f919e389d18e.png)

> The Members tab requires a login using a username and password, both of which we do not have. However, an interesting to note is that there is `I've forgotten my password` function which prompts for a username. Thus, we need to first get a username.

![image](https://user-images.githubusercontent.com/68913871/126041127-c8b46f7a-af8f-4607-8253-dc8a0cab6500.png)

> By exploring the About page, we get a valid username as `borgana` which is the login for Ben Organa, UFOria CEO.

![image](https://user-images.githubusercontent.com/68913871/126041024-6f713558-6c40-4d11-8db3-1bb40a4c550b.png)

> By providing the username in the `Forgot password` function, we are then prompted with a security question which upon solving, will allow us to recover the password.

![image](https://user-images.githubusercontent.com/68913871/126041030-22858742-0a8a-41af-8538-22e67940d498.png)

> We need to find the CEO's place of birth. Looking back at the About page, the following sentence stood out to me:

> “I can never forget the day that we decided to establish the pillars of this company with Elliot Talton in our trip to our home town.”

> Since this is an Open Source Intelligence (OSINT) challenge, we need to take a look at the social media pages provided in the site such as this [Linkedin page](https://www.linkedin.com/company/uforia-aerospace/).

> The phrase "our home town" suggests that Elliot Talton had a close relation to the CEO when they were young. Look for Co-founder Elliot Talton and [his post](https://www.linkedin.com/feed/update/urn:li:activity:6811178494656057344/)

![image](https://user-images.githubusercontent.com/68913871/126041425-fcc71050-bfd9-466b-88db-45257315faa3.png)

> "Sweet childhood memories" suggests that Elliot Talton used to visit `Lands Huys Café` when he was a child. Since it is likely that the CEO grew up at the same location as Elliot Talton, I did a research on the café and found the location as `Bourtange`.

![image](https://user-images.githubusercontent.com/68913871/126041432-6eef2932-0e5e-4ede-bdde-fa5292ce5bc4.png)

> Entering the location `Bourtange` as the answer to the security question gave us the password `fataborgana42`, which coupled with the username `borgana`, allows us to enter the members only area and obtain the flag.

![image](https://user-images.githubusercontent.com/68913871/126041622-e415e0f7-88a2-4ad8-90c4-49d1cf1b1849.png)

`CTF{fataborgana42}`

### [Go to Top](#hacky_holidays-space_race)

## Space Snacks

![image](https://user-images.githubusercontent.com/68913871/126041746-0d835c41-900b-4b30-bb39-2611ba0a4a3d.png)

![image](https://user-images.githubusercontent.com/68913871/126041748-6639720e-d894-482a-9cea-a57cfa87b59f.png)

![image](https://user-images.githubusercontent.com/68913871/126041750-a23921d7-56cf-43e9-a63e-5f44e56273d2.png)

> Rotten and 13 circles gives a hint that it is a `ROT13` encryption, which is then decoded [here](https://gchq.github.io/CyberChef/#recipe=ROT13(true,true,false,13)&input=VmcgbmNjcm5lZiBsYmggdW5xIGp1bmcgdmcgZ254cmYgZ2IgZmJ5aXIgZ3VyIHN2ZWZnIHB5aHIKSnJ5eSBRYmFyIGZjbnByIHBucXJnCnBnc3tMYmhfc2JoYXFfZ3VyX2ViZ30KTnBwcmZmIHBicXIgY25lZyAxOiBRTw)

```
It appears you had what it takes to solve the first clue
Well Done space cadet
ctf{You_found_the_rot}
Access code part 1: DB
```

`ctf{You_found_the_rot}`

![image](https://user-images.githubusercontent.com/68913871/126041925-bd8f6d0b-413f-4749-b10b-f3c7f7d0d15a.png)

> Roman gives the hint that it is `caeser cipher`, which is then decoded [here](https://www.dcode.fr/caesar-cipher) using brute-force guessing of the shift.

```
Caesar never was very good at hiding messages.
ctf{The_one_true_salad}
code part: GP
```

`ctf{The_one_true_salad}`

![image](https://user-images.githubusercontent.com/68913871/126041974-8eb69b6d-c76f-4419-8cc1-7994ebff67a5.png)

> Base line of 64 speakers and the = sign suggest that it is `base64` encoded, which is then decoded [here](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true)&input=UlhabGJpQWdhVzRnYzNCaFkyVWdkMlVnYkdsclpTQjBhR1VnWW5WMGRHVnllU0JpYVhOamRYUWdZbUZ6WlM0Z1kzUm1lMGxmYkdsclpWOTBhR1ZmWW5WMGRHVnllVjlpYVhOamRXbDBYMkpoYzJWOUlDNGdRV05qWlhOeklIQmhjblFnTXpvZ1dFUT0)

```
Even  in space we like the buttery biscut base. ctf{I_like_the_buttery_biscuit_base} . Access part 3: XD
```

`ctf{I_like_the_buttery_biscuit_base}`

![image](https://user-images.githubusercontent.com/68913871/126042037-e5be706a-3da3-4acb-93b6-3b28cefd8fc7.png)

```
.. -. ... .--. . -.-. - --- .-. / -- --- .-. ... . / .-- --- ..- .-.. -.. / -... . / .--. .-. --- ..- -.. / --- ..-. / -.-- --- ..- .-. / . ..-. ..-. --- .-. - ... .-.-.- / -.-. - ..-. ---... ... .--. .- -.-. . -.. .- ... .... ..--- ----- ..--- .---- / .- -.-. -.-. . ... ... / -.-. --- -.. . ---... / .--- --...
```

> Beeps on radio suggests that it is a `morse code`, which is then decoded [here](https://morsecode.world/international/translator.html)

```
INSPECTOR MORSE WOULD BE PROUD OF YOUR EFFORTS. CTF:SPACEDASH2021 ACCESS CODE: J7
```

`CTF:SPACEDASH2021`

![image](https://user-images.githubusercontent.com/68913871/126042182-2b1f3cfe-187c-4400-88cc-4211eb817ad5.png)

```
* ****  * * * *** ***  **    *  *  * ****  * ** *  ** ***  ** ***  ** * *  *   ** *     *  * ** *  *   ** *     *   **  *   *****  **** *  ***  *  ** * *     *
```

> The code is made up of asterisk(*) and spaces( ). This suggests a binary code where the asterisk represents 0 and the spaces represents 1 or vice versa. Here, the former is the correct interpretation and gives us the following binary:

```
0100001101010100010001100111101101101000011010010110010001100100011001010110111001011111011010010110111001011111011100110111000001100001011000110110010101111101
```

> Use [Cyber Chef - From Binary](https://gchq.github.io/CyberChef/#recipe=From_Binary('Space',8)&input=MDEwMDAwMTEwMTAxMDEwMDAxMDAwMTEwMDExMTEwMTEwMTEwMTAwMDAxMTAxMDAxMDExMDAxMDAwMTEwMDEwMDAxMTAwMTAxMDExMDExMTAwMTAxMTExMTAxMTAxMDAxMDExMDExMTAwMTAxMTExMTAxMTEwMDExMDExMTAwMDAwMTEwMDAwMTAxMTAwMDExMDExMDAxMDEwMTExMTEwMQ) to decode the binary and obtain the flag.

`CTF{hidden_in_space}`

### [Go to Top](#hacky_holidays-space_race)

## Unitentifi3d Flying Object

![image](https://user-images.githubusercontent.com/68913871/126042325-567357eb-4812-4f2b-bd72-32631e7a59ae.png)

![image](https://user-images.githubusercontent.com/68913871/126042329-9537d563-6614-45f5-b7a9-f92958fe47fe.png)

![image](https://user-images.githubusercontent.com/68913871/126042333-9b56e863-40bf-4aa7-8fbb-9de1ff9f7d69.png)

[unidentifi3d.gcode](https://portal.hackazon.org/files/b281f3dce14acc94b22f5ada593e3494bc5767c3/unidentifi3d.gcode)

![image](https://user-images.githubusercontent.com/68913871/126042347-a1877f6b-6fa9-459f-beeb-82f758fa1394.png)

> Open the .gcode file using a text editor like notepad and we can find some interesting parameters at the bottom of the file, after the Gcode. The `SETTING_3 definition` is the closest resemblance to a printer's make and model.

```
;End of Gcode
;SETTING_3 {"global_quality": "[general]\\nversion = 4\\nname = Extra Fast #2\\n
;SETTING_3 definition = geeetech_A10M\\n\\n[metadata]\\ntype = quality_changes\\
;SETTING_3 nsetting_version = 16\\nquality_type = verydraft\\n\\n[values]\\nsupp
;SETTING_3 ort_enable = True\\n\\n", "extruder_quality": ["[general]\\nversion =
;SETTING_3  4\\nname = Extra Fast #2\\ndefinition = fdmprinter\\n\\n[metadata]\\
;SETTING_3 ntype = quality_changes\\nsetting_version = 16\\nposition = 0\\nquali
;SETTING_3 ty_type = verydraft\\n\\n[values]\\n\\n", "[general]\\nversion = 4\\n
;SETTING_3 name = Extra Fast #2\\ndefinition = fdmprinter\\n\\n[metadata]\\ntype
;SETTING_3  = quality_changes\\nsetting_version = 16\\nposition = 1\\nquality_ty
;SETTING_3 pe = verydraft\\n\\n[values]\\n\\n"]}
```

`geeetech A10M`

![image](https://user-images.githubusercontent.com/68913871/126042477-723c4f7a-3ab2-4177-99e1-e306e893f74d.png)

> We are required to analyze the gcode file using the correct software for visualization. [Ultimaker Cura](https://ultimaker.com/software/ultimaker-cura) is the choice for this challenge.

> The 3D object is that of a UFO, but with the Helpers, it looks like a house, as shown below:

![image](https://user-images.githubusercontent.com/68913871/126042490-23c6d3c8-26da-4851-b566-7fafd697b4d9.png)

> After fiddling around with the software, I switched to top view and drag the layer from bottom up as if I was printing this using a 3D printer. I saw some words which is likely our flag. However, it wasn't so clear.

![image](https://user-images.githubusercontent.com/68913871/126042497-31b4bb52-9841-49b4-8aae-9ef0d9e3a01f.png)

> I proceeded to untick some options in view to get a clearer image, which then revealed the flag.

![image](https://user-images.githubusercontent.com/68913871/126042499-ded63946-adf3-4389-8354-41189ee6ee6b.png)

![image](https://user-images.githubusercontent.com/68913871/126042503-bb8dab9f-f4f4-4545-8092-78ed11823419.png)

`CTF{flying_saucer}`

### [Go to Top](#hacky_holidays-space_race)

## Stolen Research

![image](https://user-images.githubusercontent.com/68913871/126042758-f5cf2428-acb4-4340-97db-6cb0b78fe49c.png)

![image](https://user-images.githubusercontent.com/68913871/126042761-4ea41941-53ca-494e-b6ab-fb09dc8b7ab6.png)

![image](https://user-images.githubusercontent.com/68913871/126042762-cdbb1262-5f3b-4c03-b7fe-d19b2a474a3c.png)

[memdump.vem.7z](https://portal.hackazon.org/files/6625a4cb113816668304191ec4217e05acd5738d/memdump.vmem.7z)  
[stolen.pcapng](https://portal.hackazon.org/files/97660a376fd39341fab7e0d8ecc1efd5648be310/stolen.pcapng)

![image](https://user-images.githubusercontent.com/68913871/126042776-4b750966-8350-4fb1-a586-f58452493753.png)

> Use 7zip to extract archive memdump.vmem and analyze the .vmem file using [this link](https://filext.com/file-extension/VMEM) to get the OS and kernel.

![image](https://user-images.githubusercontent.com/68913871/126042781-79431ddb-04ff-4959-aef9-aa6ca6a47fa7.png)

`5.10.0-kali8-amd64`

### [Go to Top](#hacky_holidays-space_race)

## Power Snacks

![image](https://user-images.githubusercontent.com/68913871/126042854-04561f3e-bfb0-4e15-bc3f-ab6fb65e3444.png)

![image](https://user-images.githubusercontent.com/68913871/126042855-b99d7960-6126-410f-af76-d743848c195a.png)

![image](https://user-images.githubusercontent.com/68913871/126042858-394aa71e-e781-4267-b520-a0e45f74c5dc.png)

![image](https://user-images.githubusercontent.com/68913871/126042859-3eed5ecc-d24c-47b5-b5e0-9f0af1096e70.png)

> This challenge requires knowledge of how to construct a [loop in powershell](https://www.business.com/articles/powershell-for-loop/), as well as the modulo operation %.

> $x = for ($i=1;$i -le 1337;$i++){if ($i %42 -eq 0){"Life, the universe, and everything";} else {"$i"}}  
$x | Check

![image](https://user-images.githubusercontent.com/68913871/126043003-29d94e26-34fa-4b7a-9d86-8f9275fdbb47.png)

`CTF{using_your_powers_for_powershell}`

![image](https://user-images.githubusercontent.com/68913871/126043267-35d5589d-7167-4824-8083-e505120d4bc2.png)

> Get all words with `iydhlao`. This is a bad powershell command but it works    
$a = Get-Content dictionary | Select-String -Pattern 'k', 'z', 'e', 'j', 'm', 'b', 'n', 'c', 'f', 'g', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'  -NotMatch

> Only include those with length 2 or more. Pattern option followed by regular expression  
$a = $a | Select-String -Pattern '.{2,}'

> Combine them together:  
$a = Get-Content dictionary | Select-String -Pattern 'k', 'z', 'e', 'j', 'm', 'b', 'n', 'c', 'f', 'g', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'  -NotMatch | Select-String -Pattern '.{2,}'

> After playing around with powershell I decided to just use python as a work around  
Save the output as dictionary_trim.txt with newline separator:

```
AOL
Aaliyah
Ada
Aida
Al
Aldo
Ali
Allah
Ayala
Dada
Dalai
Dali
Day
Di
Dial
Dido
Doha
Dolly
Hal
Hall
Hay
Hilda
Hill
Holiday
Holly
Hood
I'd
I'll
Idaho
Ila
Iliad
La
Lao
Layla
Li
Lidia
Lila
Lilia
Lilly
Lily
Lloyd
Lola
Loyd
Loyola
Lydia
Lyly
Ohio
Ola
Yahoo
Yoda
ad
add
ado
ah
aha
ahoy
aid
ail
all
allay
alloy
ally
aloha
ay
dad
daddy
dado
dahlia
daily
dally
day
dial
did
dill
dilly
dillydally
do
dodo
doily
doll
dolly
doodad
ha
had
hah
hail
hall
halo
hay
hi
hid
hill
hilly
ho
hod
hold
holiday
holly
holy
hood
hoodoo
id
idly
idol
idyl
idyll
ill
la
lad
lady
laid
lay
lid
lily
lo
load
loll
loyal
loyally
odd
oddly
oh
oho
oil
oily
old
y'all
yahoo
yo
```

> Create a python script to further remove repeated characters and capital letters, as well as sort by ascending length and output to a list of strings.

```python
myList = []
with open('dictionary_trim.txt','r') as myFile:
    for line in myFile:
        myList.append(line[:-1]) #Remove \n
newList = []
#Remove repeated characters and capital letters
for string in myList:
    for char in string:
        if string.count(char) >= 2 or char.isupper():
            newList.append(string)
            break
        else:
            pass
finalList = [i for i in myList if i not in newList]
#Sort by ascending length
print(sorted(finalList, key=len))
```

```
['ad', 'ah', 'ay', 'do', 'ha', 'hi', 'ho', 'id', 'la', 'lo', 'oh', 'yo', 'ado', 'aid', 'ail', 'day', 'had', 'hay', 'hid', 'hod', 'lad', 'lay', 'lid', 'oil', 'old', 'ahoy', 'dial', 'hail', 'halo', 'hold', 'holy', 'idly', 'idol', 'idyl', 'lady', 'laid', 'load', 'oily', 'daily', 'doily', 'holiday']
```

![image](https://user-images.githubusercontent.com/68913871/126043333-27d69cc7-1cd1-4124-87c7-2bdf652dbb16.png)

`CTF{using_your_holidays_for_learning_powershell}`

### [Go to Top](#hacky_holidays-space_race)

## Quantum Shuttle

![image](https://user-images.githubusercontent.com/68913871/126043514-0f6c8a91-292f-4efd-982f-0cb7c175d9c3.png)

![image](https://user-images.githubusercontent.com/68913871/126043517-e9126250-d4e8-442a-98da-610e36afc18d.png)

![image](https://user-images.githubusercontent.com/68913871/126043522-cec851d4-7f8a-434d-b631-ff1cb7254c55.png)

![image](https://user-images.githubusercontent.com/68913871/126043525-53a3d75f-2cbb-4c80-aed4-9f58db25cece.png)

[background-info.pdf](https://portal.hackazon.org/files/fc46531e8d4f49b54afbb37815ad888ddaf91f3e/background-info.pdf)

![image](https://user-images.githubusercontent.com/68913871/126043551-9d85f9fa-524d-4f7b-8f03-852fafc77983.png)

> Create a python script, defining the CNOT and NOTC functions, then run the given protocol to get the resulting bit-string.

```python
b = 'x000101001011' #index start from 1

def flip(bit):
    if bit == '1':
        return '0'
    else:
        return '1'

def CNOT(control,target):
    if control == '1':
        return control+flip(target)
    else:
        return control+target

def NOTC(target,control):
    if control == '1':
        return flip(target)+control
    else:
        return target+control

print(CNOT(b[1],b[2])+NOTC(b[3],b[4])+CNOT(b[7],b[5])+NOTC(b[6],b[8])+CNOT(b[11],b[12])+NOTC(b[10],b[9]))
```

```
001100101011
```

`001100101011`

**Summary:** The challenges in this CTF were fun, though I only managed to solve the beginner and easy challenges.   

## [Go to Top](#hacky_holidays-space_race)
