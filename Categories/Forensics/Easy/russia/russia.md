## Russia

[flag](https://github.com/Rookie441/CTF/blob/main/Categories/Forensics/Easy/russia/flag)  

> We are given a flag file which we can analyze using the Linux `file` command to see that it is ASCII text and further analyzing using the `head` command, we can see the the first few bytes indicate that it is base64 encoded.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Forensics/Easy/russia/FirstFile.png)  

> We can then proceed to decode using `base64 --decode` and output to a new file named flag1. Then, by running the file command again, we see that this time it is a zip file, so we unzip and rename the new file flag2.

> We then repeat the process and discovered that flag2 is a bzip2 file, so we rename it with the .bz2 extension and then decode using `bzip2 -d`

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Forensics/Easy/russia/SecondFile.png)  

> By repeating this analysis process, we can discover all the possible file types as follows:

```
ASCII text, Zip, bzip2, gzip
```

> We can then proceed to write a python script to extract the files and apply base64 decoding whenever the file type is ASCII text. We will be adapting the script from [this writeup](https://ctftime.org/writeup/13378)

```python
import os, base64
import bz2, zipfile, gzip
import magic # pip install python-magic

i = 0
current_file = "flag"

while True:
   new_file = "decompressed-" + str(i)

   # Analyzing file type.
   file_type = magic.from_file(current_file)
   print("[*] File '{}' is '{}'.".format(current_file, file_type))

   # Found the flag.
   with open(current_file, "r") as cf:
      try:
         read_data = cf.read()
         if "STANDCON22{" in read_data:
            print (read_data)
            break
      except:
         print("cannot decode")

   # Analyzing archives.

   if "bzip2" in file_type:

      with open(new_file, 'wb') as nf, open(current_file, 'rb') as cf:
         decompressor = bz2.BZ2Decompressor()
         for data in iter(lambda : cf.read(100 * 1024), b''):
            nf.write(decompressor.decompress(data))

   elif "Zip" in file_type:

      with zipfile.ZipFile(current_file) as cf:
         if len(cf.namelist()) == 1:
            file_to_be_extracted = cf.namelist()[0]
         else:
            print ("[!] Too much files into the archive!")
            break
         cf.extractall()
         os.rename(file_to_be_extracted, new_file)

   elif "ASCII text" in file_type:

      with open(current_file, "r") as cf:
         encoded_data = cf.read()
      decoded_data = base64.b64decode(encoded_data)
      with open(new_file, "wb") as nf:
         nf.write(decoded_data)

   elif "gzip" in file_type:

      with gzip.open(current_file, "r") as cf:
         read_data = cf.read()
      with open(new_file, "wb") as nf:
         nf.write(read_data)

   else:
      print ("[!] Unknown archive, exiting.")
      break

   # Removing old file and going on with analysis.
   #os.remove(current_file)
   current_file = new_file
   i += 1
```

> Note that running of the script did not provided us with the flag because the flag format `STANDCON22{` was not in plaintext. Moreover, there is an unknown archive of type `data`. As such, to further analyze the files, I commented the `os.remove()` line, so I could manually browse the last few files before the error occurred.  

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Forensics/Easy/russia/Ending.png)  
![image](https://github.com/Rookie441/CTF/blob/main/Categories/Forensics/Easy/russia/LastFile.png)  

> Opening `decompressed-898`, we can see that it is no longer base64 encoded as we expect it to be. It is a series of hexadecimal values. As such, our script has failed by trying to base64 decode it.

```
53 54 41 4E 44 43 4F 4E 32 32 7B 44 30 4C 4C 5F 46 30 52 5F 53 41 4E 47 4E 49 4C 41 5F 55 54 41 4D 41 7D 22
```

> Here, we can simply decode from hex to get the flag. However, if we want to work on `decompressed-899` then we first need to base64 encode it (reverse the base64 decode process) to get these hex values then decrypting it. This can be done using CyberChef.

![image](https://github.com/Rookie441/CTF/blob/main/Categories/Forensics/Easy/russia/Decrypted.png)  

`STANDCON22{D0LL_F0R_SANGNILA_UTAMA}`
