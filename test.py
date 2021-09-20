from cryptography.fernet import Fernet
#module that encrypts text using a key which we going to provide 



# we going to make two functions which will be used to check and add
#we will be able to call them view() and we do this for it to be repeatbale 
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''


def load_key():
    file = open("key.key","rb") # "rb is in bytes"
    key = file.read()
    file.close()
    return key

m_pwd = input("Choose your main password?  ")
key = load_key() + m_pwd.encode()
fer = Fernet(key)    



def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            #line.strip it takes the line and strips unwanted characters like \n

            #print(line.rstrip()) 
            data = line.rstrip()
            #what this does it will split the line and look for | and store user and passw
            user, passwrd = data.split("|")
            print("User: ",user , ", Password: ", fer.decrypt(passwrd.encode()).decode())
    

def add():
    name = input('Account name:  ')
    pwd = input('Password:  ')

    # code below we trying to append to the file the password. the 'with'
    #funtion allows us to open the file while we need it and it will close it when the 
    #instructions are done. this example 'a' just appends to the file 
    with open('passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")
        #

        





while True:
    mode = input("Would you like to add and new password or view an existing password ? (view,add). press q to quit.    ").lower()
    #this is going to require either view or add as inputs which we can check for either
    if mode == "q":
        break
    # this break will leave the loop so we dont have to make the next
    # elif 
    
    if mode == "view":
        view()
        
    elif mode == "add":
        add()
    else:
        print("Invalid mode")
        continue
