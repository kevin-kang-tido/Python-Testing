import random

chars = "this is kevin tido "

def encryption(text):

    encrypted = ""

    for char in text:
        if char != " ":
            random_the_valuse = random(10,1)
  
  

print("Before the Encryption:", chars)

encrypted_text = encryption(chars)

print("After the Encryption:", encrypted_text)
