"""
create a function that can store our password, if don't have one before, create a new one and store it in a txt file
create a view function and add function to handle it
use cryptography.fernet module to encrypt the password
"""

# Here is a code for password manager without encryption
"""
master_pwd = input("what is the master password?")

def view():
    with open("password.txt", 'r') as f:
        # readlines() would read all the lines in the file, and now we are using the for loop to print our all the lines
        # why readlines() is using a for loop is it would return a list instead of printing the file documents one by one
        # read() could print all the documents in the file, read(5) could even print the first 5 index in the file
        # readline() could print the line in document one by one

        # print(f.read().strip())
        # print(f.readlines())
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user}, Password: {passw}")


    

def add():
    # we would need to config who is going to add the file first, so an account name and pwd would be neccessary
    name = input("Account name: ")
    pwd = input("Password: ")

    # since we are using the with here, so once we have finished doing what is indented in the with function, the function would automatically close the file for us
    # 'w' means write, which means to create a file/override if the file already exists
    # 'r' would be a read mode, only thing you can do is to read text in the file, if you trying to use r to open a file that doesn't exist, it would cause a problem
    # 'a' would be the most flexible mode. it allows you to add something to a file, or if the file that is not exists, it would create a new file to write things in
    with open("password.txt", "a") as f:
        f.write(name + "|" + pwd + "\n")



while True:
    mode = input("Add, view the password or press q to quit? ").lower()
    if mode == 'q':
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("please enter valid password")
        continue
        
"""

# Here is a code for password manager with encryption
from cryptography.fernet import Fernet
# key + password + text to encrypt = random text
# random text + key + password = text to encrypt


def load_key():
    # 'rb' means read bytes mode. 
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# encode() would take your things convert into bytes
key = load_key() 
# initializing the fernet module
fer = Fernet(key)

'''
def write_key():
    key = Fernet. generate_key()
    # 'wb' means write bytes mode. is a special file format, binary file 
    with open("key.key", "wb") as key_file:
        key_file.write(key)

'''



def view():
    with open("password.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user}, Password: {fer.decrypt(passw.encode().decode())}")


    

def add():
    # we would need to config who is going to add the file first, so an account name and pwd would be neccessary
    name = input("Account name: ")
    pwd = input("Password: ")

    with open("password.txt", "a") as f:
        # encode() would convert string into bytes string and decode() would convert it into normal string
        f.write(name + "|" + fer.encrypt(pwd.encode().decode()) + "\n")



while True:
    mode = input("Add, view the password or press q to quit? ").lower()
    if mode == 'q':
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("please enter valid password")
        continue