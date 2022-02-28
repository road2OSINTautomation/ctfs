import whois
import hashlib

domain = "facebook.com"
w = whois.whois(domain)

print("Creation date of \""+domain +"\": " +str(w['creation_date']))

date_correct_format = w['creation_date'].strftime("%Y%m%d")
print(date_correct_format)

encoded_text = hashlib.md5(date_correct_format.encode())
print("MD5 of " + date_correct_format + ": " + str(encoded_text.hexdigest()))