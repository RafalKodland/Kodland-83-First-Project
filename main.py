import random

def pswd(pass_length=10):
    elements = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    
    return password
