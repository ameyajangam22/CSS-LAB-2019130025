
import numpy as np
import math
import copy
def substitution():
    print ("You have selected substitution algorithm..")
    givenString=takeInput("Enter string:")
    shifts=int(input("Enter the no. of shifts "))
    encryptedText=""
    for char in givenString:
        if char==" ":
            encryptedText+=" "
        else:
            encryptedText+=chr(ord('a')+(ord(char)-ord('a')+shifts)%26)

    decryptedText=""
    for char in encryptedText:
        if char==" ":
            decryptedText+=" "
        else:
            decryptedText+=chr(ord('a')+(ord(char)-ord('a')-shifts+26)%26)
    printOutput(encryptedText,decryptedText)
    return

def rot13():
    print ("You have selected ROT13 algorithm..")
    givenString=takeInput("Enter string:")
    encryptedText=""
    shifts=13
    encryptedText=""
    for char in givenString:
        if char==" ":
            encryptedText+=" "
        else:
            encryptedText+=chr(ord('a')+(ord(char)-ord('a')+shifts)%26)   

    decryptedText=""
    for char in encryptedText:
        if char==" ":
            decryptedText+=" "
        else:
            decryptedText+=chr(ord('a')+(ord(char)-ord('a')-shifts+26)%26)
    printOutput(encryptedText,decryptedText)
    return

def transpose():
    print ("You have selected Transposition algorithm..")
    givenString=takeInput("Enter string: ")
    key = input('Enter the key:')
    key.upper()
    order = sorted(list(key))
    col = len(key)

    # Encryption
    msg_len = len(givenString)
    msg_arr = list(givenString)
    row = int(math.ceil(msg_len/col))
    null_values = row*col - msg_len
    msg_arr.extend('_'*null_values)
    matrix = np.array(msg_arr).reshape(row,col)
    encryptedText = ''
    for i in range(col):
        index = key.index(order[i])
        encryptedText += ''.join([row[index] for row in matrix])
    print('Encrypted Text:',encryptedText)

    # Decryption
    encryptedText_arr = list(encryptedText)
    decryptedText = ''
    ptr = 0
    decrypt_matrix = np.array([None]*len(encryptedText)).reshape(row,col)
    for i in range(col):
        index = key.index(order[i])
        for j in range(row):
            decrypt_matrix[j,index] = encryptedText_arr[ptr]
            ptr += 1
    decryptedText = ''.join(''.join(x for x in y) for y in decrypt_matrix)
    #REMOVE UNDERSCORES FROM STRING
    real_decrypted_text=""
    for char in decryptedText:
        if char=="_":
            break
        else:
            real_decrypted_text+=char

    decryptedText=real_decrypted_text
    print('Decrypted Text:',decryptedText)

def doubleTranspose():
    print ("You have selected Double Transposition algorithm..")
    givenString=takeInput("Enter string:")
    key = input('Enter the key:')
    key.upper()
    order = sorted(list(key))
    col = len(key)

    ## Encryption
    msg_len = len(givenString)
    msg_list = list(givenString)
    row = int(math.ceil(msg_len/col))
    null_values = row*col - msg_len
    msg_list.extend('_'*null_values)
    matrix = np.array(msg_list).reshape(row,col)
    middleText,encryptedText = '',''

    for i in range(col):
        index = key.index(order[i])
        middleText += ''.join([row[index] for row in matrix])
    print("Single Encryption:",middleText)

    middletxt_lst = list(middleText)
    matrix = np.array(middletxt_lst).reshape(row,col)
    for i in range(col):
        index = key.index(order[i])
        encryptedText += ''.join([row[index] for row in matrix])
    print('Double Encryption:',encryptedText)

    ## Decryption
    encryptedText_lst = list(encryptedText)
    middleText,decryptedText = '',''
    pointer = 0
    dec_matrix = np.array([None]*len(encryptedText)).reshape(row,col)
    for i in range(col):
        index = key.index(order[i])
        for j in range(row):
            dec_matrix[j,index] = encryptedText_lst[pointer]
            pointer += 1

    middleText = ''.join(''.join(col for col in row) for row in dec_matrix)
    pointer = 0
    print('Single Decryption:',middleText)

    middletxt_lst = list(middleText)
    dec_matrix = np.array([None]*len(middleText)).reshape(row,col)
    for i in range(col):
        index = key.index(order[i])
        for j in range(row):
            dec_matrix[j,index] = middletxt_lst[pointer]
            pointer += 1
    real_decrypted_text=""
    for char in decryptedText:
        if char=="_":
            break
        else:
            real_decrypted_text+=char

    decryptedText=real_decrypted_text
    real_decrypted_text=""
    decryptedText = ''.join(''.join(col for col in row) for row in dec_matrix)
    real_decrypted_text=""
    for char in decryptedText:
        if char=="_":
            break
        else:
            real_decrypted_text+=char

    decryptedText=real_decrypted_text
    print('Double Decryption:',decryptedText)

def vernamCipher():
    print ("You have selected Vernam Cipher algorithm..")
    givenString=takeInput("Enter string:")
    givenKey=takeInput("Enter key:")
                
    if(len(givenString)!=len(givenKey)):
          return "\nError: Length of given string and given key should be equal\n"
    encryptedText=""
    for item in range(0,len(givenString)):
        if givenString[item]==" " and givenKey[item]==" ":
            encryptedText+=" "
        else:
            encryptedText+=chr(ord('a')+(ord(givenString[item])+ord(givenKey[item])-2*ord('a'))%26)

    decryptedText=""
    for item in range(0,len(givenString)):
        if encryptedText[item]==" " and givenKey[item]==" ":
            decryptedText+=" "
        else:
            decryptedText+=chr(ord('a')+(ord(encryptedText[item])-ord(givenKey[item])+26)%26)
    
    printOutput(encryptedText,decryptedText)
    return

def diffieHellman():
    g=int(input("Enter Prime Number (g):"))
    p=int(input("Enter Second Prime Number (p):"))
    xa=int(input("Enter Secret (Xa):"))
    xb=int(input("Enter Secret (Xb):"))

    #Generated keys
    ya=int((pow(g,xa,p)))
    yb=int((pow(g,xb,p)))

    print(f"Ya:{ya}")
    print(f"Yb:{yb}")

    #Shared keys
    k1=int((pow(yb,xa,p)))
    k2=int((pow(ya,xb,p)))

    print(f"The secret key k1 shared with A is: {k1}")
    print(f"The secret key k2 shared with B is: {k2}")

    return
def exitter():
    print("Exiting...")
    exit()


def returnAlgoFunc(func):
    return func()

def takeInput(text):
    givenString=input(text)
    return givenString

def printOutput(encryptedText,decryptedText):
    print(f"Encrypted Text: {encryptedText}")
    print(f"Decrypted Text: {decryptedText}")


print("Select one of the cryptography methods:")
switcher = {
    1: substitution,
    2: rot13,
    3: transpose,
    4: doubleTranspose,
    5: vernamCipher,
    6: diffieHellman,
    7: exitter
}

while True:
    print("1. Substitution Algorithm")
    print("2. ROT 13 Algorithm")
    print("3. Transpose Algorithm")
    print("4. Double Transposition Algorithm")
    print("5. Vernam Cipher Algorithm")
    print("6. Diffie Hellman Algorithm")
    print("7. Exit")
    print("Enter your option:")
    option = int(input())
    returnAlgoFunc(switcher.get(option))
