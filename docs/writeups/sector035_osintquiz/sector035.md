## Sector035's OSINT quiz

The [osint quiz](https://twitter.com/Sector035/status/1211038518635614208) of
[𝕊𝕖𝕔𝕥𝕠𝕣𝟘𝟛𝟝](https://twitter.com/Sector035) and the [Quiztime](https://twitter.com/Quiztime) crew is probably the 
challenge you read most about (at least combined with OSINT).

--------------------------
### Challenge 0 - Start
As told in the referenced tweet above you start this quiz by sending an email to osintquiz@gmail.com
with the subject "start".

After sending this initial email you will receive a short introduction on how the ctf works and which subjects will 
be covered:
> - Geolocation (determining locations)
> - SIGINT (from 3G/LTE to WiFi)
> - Social media (anything goes!)
> - News articles (from any country)
> - Surface web & dark web (no worries, we'll stay legal!)
> - Metadata in files (a bit of basic forensics can't hurt right?)
> - Tracking traffic or objects (start looking up some URL's!)
> - Maybe more...

--------------------------
### Challenge 1
> Create the MD5 hash of the word "puzzletweet"

#### What is MD5?
>The MD5 (message-digest algorithm) hashing algorithm is a one-way cryptographic function that accepts a message of any length as input and returns as output a fixed-length digest value to be used for authenticating the original message.
> -- <cite>[TechTarget](https://www.techtarget.com/searchsecurity/definition/MD5) </cite>


Of course the md5 hash can be calculated using the command line command "md5sum":
````commandline
echo -n "puzzletweet" | md5sum
````
Keep in mind the -n option removes the newline after the echo output as you dont want the
newline character to be part of the plaintext string.

As I want to expand my python skills, I'll be trying to solve as many challenges as possible also in python:
````python
import hashlib

plaintext = "puzzletweet"
encoded_text = hashlib.md5(plaintext.encode())

print("The md5 of " + plaintext + " is: " + str(encoded_text.hexdigest()))
````
Pythonfile: 
[challenge001.py](../../../src/sector035_osintquiz/challenge001.py)
--------------------------