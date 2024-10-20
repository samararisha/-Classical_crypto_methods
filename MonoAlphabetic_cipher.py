def get_keyvalid(key) : 
    key = list(key)
    validkey = []
    seen = set()
    for letter in key : 
        if letter not in seen : 
            validkey.append(letter)
            seen.add(letter)
        
    return "".join(validkey)


def get_cipher_key (key) : #to complete the key after the user 
    cipher_alpha = []
    cipher_alpha = list(key)
    for letter in range (97,123) :
        if chr(letter) not in cipher_alpha  :
            cipher_alpha.append(chr(letter))
    print("the key after auto completion : ","".join(cipher_alpha) , "\n")
    return cipher_alpha
    
def MonoEnc() : 
    plaintxt = input("please enter the plain txt : ").lower()
    key = input("enter the key/cipher alphpaptic: ").lower()
    key = get_cipher_key(get_keyvalid(key))
    cipher = []
    plaintxt = list(plaintxt)
    for letter in plaintxt : 
            if letter.isalpha(): 
                 index = ord(letter) - ord("a") 
                 cipher.append(key[index])
            elif letter !=" " and not letter.isdigit() : 
                cipher.append(letter) 
            elif letter.isdigit() : 
                cipher.append(letter)
    return "".join(cipher).upper()
     
def monodyc () : 
    ciphertxt = input("enter the cipher txt to dycrypt : ").lower()
    plain = []
    key = input("enter the key/cipher alphpaptic: ").lower()
    key = get_cipher_key(get_keyvalid(key))
    key = list(key)
    for letter in ciphertxt: 
        if letter.isalpha()  :
            numofindex = key.index(letter)
            plain_letter  = chr(97 + numofindex)
            plain.append(plain_letter)
        elif not letter.isdigit() and not letter.isalpha(): 
            plain.append(letter)    
        elif letter.isdigit() : 
            plain.append(str(letter))
        else : 
            plain.append(letter)
    return "".join(plain).upper()       
        
        


cond = True
while cond  : 
    try: 
      
       option = int(input("Welcome to the monoalphapitic cipher to encrypt choose 1 \n to dcrypt choose 2 and to decline enter 0: "))
      
    except ValueError: 
       option=input("Only intgers allowd (0, 1 ,2) : ")
    if option == 1 : 
        print(f"the encrypted txt is : {MonoEnc()}")
    elif(option== 2) : 
         print(f"the plain txt is : {monodyc()}")
    else  :
         cond = False
         print("\n----Bye---")
            
            

    
    
