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
with open("thkey.key", "rb")as key:
    secretkey = key.read()


for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
       done =  thefile.write(contents_decrypted)
       if done:
        os.remove("thkey.key")
        print("dover")

    