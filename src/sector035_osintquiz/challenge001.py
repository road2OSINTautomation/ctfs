import hashlib

plaintext = "puzzletweet"
encoded_text = hashlib.md5(plaintext.encode())

print("The md5 of " + plaintext + " is: " + str(encoded_text.hexdigest()))
