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
[challenge001.py](https://github.com/road2OSINTautomation/ctfs/blob/main/src/sector035_osintquiz/challenge001.py)

--------------------------

### Challenge 2
> In December 2017 @Sector035 posted a photo of a puzzle. What is the ID of the photo? 
> That is the highlighted part in this URL

Wow, this challenge seemed to be so easy to implement in python. <br/>
Twitter has really well documented API and also there are quite a couple of python modules already
implementing the api. <br />
Unfortunately you can not search twitter data longer than 7 days old with the free API.

Doing it manually seems so straight forward. Just head to the twitter 
[advance search](https://twitter.com/search-advanced?lang=en) type in @Sector035 as username and add the from and to 
dates at the bottom of the form. <br />
After that you can click on Photos and you will only see 6 different posts and can easily find the photo 
of a puzzle.
First click on the photo and then right click to and view the photo in a new tab...Now you can copy the needed part of 
the url and create your md5 :)

Anyway my goal is to solve these challenges in a pythonic way:

Also I definitely was getting frustrated to not be able to do this simple manual call with the 
free Twitter API, I randomly clicked through my twitter developer dashboard and found the "Premium"-section.
You can find it via Dashboard -> Products (on the left) -> Premium.
After setting up a "Dev Environment" you can use the "Search Tweets API: Full Archive"-API.

And voila this is exactly what I was after!!!
You can find the documentation including a curl example here:
https://developer.twitter.com/en/docs/twitter-api/premium/search-api/quick-start/premium-full-archive

I used the example to code the python request. After filtering on tweets including the word 'puzzle' 
you can get the tweet_id of the tweet including the photo of the puzzle.

Now you're still not quite finished as you need the photo_id. To help me get that id I used the 
example code of twitter for the 
["Tweet-Lookup"-API](https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Tweet-Lookup/get_tweets_with_bearer_token.py).

Putting it all together ended with [challenge002.py](https://github.com/road2OSINTautomation/ctfs/blob/main/src/sector035_osintquiz/challenge002.py)

#### Side notes on challenge 2
After finishing setting everything up I put my keys and secrets into an extra file "twitter_api.creds" in the following 
format:
````editorconfig
[DEFAULT]
consumer_key = XXXXXXXXXXXXXXXXXXXXXXXXX
consumer_secret = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
access_token_key = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
access_token_secret = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
bearer_token = XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
````
You will have to escape the percentage sign '%' within the bearer_token by replacing the single '%' with 
two of them => '%%'.

It may seem as a little bit of a hassle but if you stick to the guide and applying for an "Elevated" Account straight 
after you should be done in less than 10 minutes. I missed creating the elevated Account first and got a warning that I 
am not allowed to use the full api when verifying my developer account with python-twitter
````python
 print(api.VerifyCredentials())
````
BTW: If you ever need a twitter user's id either look in the source code of the following button or just 
use this javascript snippet:
There are plenty of online tools but most of the time it is useful to at least 
know what and how exactly third party tools work.
````javascript
alert(document.querySelector('div[data-testid="placementTracking"] div[data-testid]').dataset.testid.split('-')[0])
````

#### Summary
Wow this straight forward challenge really got me digging into the twitter API. Great opportunity 
which I otherwhise would probably not have done so soon!

-----------------------------------
