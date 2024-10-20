option = int(input("to Encrypt enter 1 , to decrypt enter 2 : ").strip())
while option not in range (1,3) : 
   option = int(input("Wrong option 1 for encryption and 2 for dycription").strip())

theAvalue = ord("a")

def ceaserenc() : 
      plain = input("please enter the plain text : ").lower()
      try : 
          key = int(input("please enter the number"))
      except ValueError :
          key = int(input("Only intgers are allowd: "))      
      cipher_list= []
      for letter in plain : 
         if letter ==" " : 
            cipher_list.append(letter)
         elif letter.isdigit() :
            num_shit = (key + int(letter)) %10
            cipher_list.append(str(num_shit))
         elif not letter.isalpha() and not letter.isdigit(): 
            cipher_list.append(letter)
         else : 
           letter_position = ord(letter) -theAvalue   
           shift = (letter_position+ key) % 26
           cipher = chr(shift +theAvalue)
           cipher_list.append(cipher)
      cipher_txt="".join(cipher_list)
      return cipher_txt
   
def ceaserdec() : 
    plain_list = []
    cipher_txt = input("enter the cipher txt : ").lower()
    key = int(input("enter the key : "))
    for letter in cipher_txt : 
       if letter == " " :
         plain_list.append(letter)
       elif letter.isdigit() : 
          num_shift = (int(letter) - key ) %10
          plain_list.append(str(num_shift))
       elif not letter.isalpha() and not letter.isdigit() : 
          plain_list.append(letter)
       else : 
        letter_position = ord(letter) - theAvalue
        shift =(letter_position-key) % 26
        plain=chr(shift + theAvalue)
        plain_list.append(plain)
        
    plain_txt = "".join(plain_list)
    return plain_txt
 
 
 
 
if option == 1 : 
   print(f"the encrypted message : {ceaserenc()}")
if option == 2 :
   print(f"the dycrpted meassage : {ceaserdec()}")
           
    
