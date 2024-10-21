import numpy as np
def get_valid_key(key): 
    key = list(key)     
    valid_key = []
    setforkey = set()
    for item in key : 
        if item not in setforkey and item!='j' : 
            setforkey.add(item)
            valid_key.append(item)
    for num in range(97 , 123) : 
        if chr(num) not in  valid_key and chr(num)!='j' :
            valid_key.append(chr(num)) 
    return (valid_key)

import numpy as np

def get_valid_plaintxt(plaintxt):
    valid_plain = [char for char in plaintxt.lower() if char.isalpha()]
    
    plainumbers = [ord(char) - ord('a') for char in valid_plain]
    
    if len(plainumbers) % 2 != 0:
        plainumbers.append(ord('x') - ord('a'))  
    plainchars = []
    for num in plainumbers : 
        char = (chr(num + 97))
        plainchars.append(char)
    blocks = np.array([plainchars[i:i + 2] for i in range(0, len(plainumbers), 2)])
    
    
    return blocks

def playfair_enc () :
    plantxt = input("please enter the plain txt : ").lower()

    key = input("please enter the key : ").lower()
    alpha_key = list(key)
    cond  =False
    for item in alpha_key: 
        if item.isalpha() == False : 
         cond = True
    count = 0        
    while cond : 
        key = input("Erro , only alphabetic letters allowd : ")
        alpha_key = list(key)
        for item in alpha_key: 
          if item.isalpha() == False : 
            count+=1
        if count == 0 : 
           cond = False 
        else : 
          cond =True
    encrypt_message = ""
    valid_key =np.array(get_valid_key(key)).reshape(5 , 5)
    plain_blocks = get_valid_plaintxt(plantxt) 
    for block in plain_blocks : 
        pos_char1 = np.argwhere(valid_key == block[0])
        pos_char2 = np.argwhere(valid_key == block[1])
        
        row1 , col1 = pos_char1[0]
        row2 , col2 = pos_char2[0]
        if row1 == row2 : 
            encrypt_message+=valid_key[(row1 , (col1+1)%5)]
            encrypt_message+=valid_key[(row2 , (col2 + 1)%5)]
        elif col1 == col2 : 
            encrypt_message+=valid_key[((row1+1)%5 , col1)]
            encrypt_message+=valid_key[((row2+1)%5 , col2)]
        else : 
            encrypt_message+=(valid_key[row1, col2])
            encrypt_message+=(valid_key[row2, col1])
    
    return encrypt_message

def playfair_dec () : 
    ciphertxt = input("please enter the cipher txt to decrypt : ").lower()  
    key = input("please enter the key : ").lower()
    alpha_key = list(key)
    cond  =False
    for item in alpha_key: 
        if item.isalpha() == False : 
         cond = True
    count = 0        
    while cond : 
        key = input("Erro , only alphabetic letters allowd : ")
        alpha_key = list(key)
        for item in alpha_key: 
          if item.isalpha() == False : 
            count+=1
        if count == 0 : 
           cond = False 
        else : 
          cond =True
    decrypt_message = ""
    valid_key =np.array(get_valid_key(key)).reshape(5 , 5)  
    plain_blocks = get_valid_plaintxt(ciphertxt) 
    for block in plain_blocks : 
        pos_char1 = np.argwhere(valid_key == block[0])
        pos_char2 = np.argwhere(valid_key == block[1])
        
        row1 , col1 = pos_char1[0]
        row2 , col2 = pos_char2[0]
        if row1 == row2 : 
            decrypt_message+=valid_key[(row1 , (col1-1)%5)]
            decrypt_message+=valid_key[(row2 , (col2 - 1)%5)]
        elif col1 == col2 : 
            decrypt_message+=valid_key[((row1-1)%5 , col1)]
            decrypt_message+=valid_key[((row2-1)%5 , col2)]
        else : 
            decrypt_message+=(valid_key[row1, col2])
            decrypt_message+=(valid_key[row2, col1])
    return decrypt_message
    
    
    
    
    
    
    
         
print("Welcom to the playfair cipher")
cond = True
while cond:
    try:
        option = int(input("encryption---> 1 , decryption --->2 , decline --->0: "))
        while option not in range (0 , 3) : 
           option = int(input("Wrong option : only 1 , 2 , 0: "))
    except ValueError: 
           option = int(input("Value Error: only 1 , 2 , 0: "))   
    if option == 1 : 
        print(f"the encrypted message is : {playfair_enc()}")
    elif option ==2 : 
        print(f"the decrypted message is : {playfair_dec()}")
    else : 
        print("---Bye---")
        cond = False
    

 
        



 
    
