import numpy as np 
import math
def invertable(keymatrix) : 
    det = int(np.round(np.linalg.det(keymatrix,))) %26 
    if det!=0 and math.gcd(det , 26) ==1 : 
        return True
    else : 
        return False
    
def get_the_key () : 
    key = input("enter the key space generated: ")
    key = list(map(int , (key.split())))
    num_of_elements = len(key)
    n = int(math.sqrt(num_of_elements))
    while n*n !=num_of_elements : 
        key = input("Value error , you need to enter a number to perform a square : ")
        key = list(map(int , (key.split())))
        num_of_elements = len(key)
        n = int(math.sqrt(num_of_elements))        
    key_matrix = np.array((key)).reshape(n,n)
     
    if invertable(key_matrix) : 
        return  key_matrix , n
    else : 
        print("the key isnot  invertable ,try a different key and the program will end") 
 


def get_blocks_of_plaintxt(plain_txt , size) :  
    global nonalpha
    nonalpha = []
    
    plain_txt = "".join([char for char in plain_txt if char.isalpha()])#remove non alphapitica letters
    plain_numbers = [ord(char) - ord("a") for char in plain_txt]
    while len(plain_numbers) % size !=0 : 
        plain_numbers.append(ord('x') - ord('a'))
        
    blocks = [np.array(plain_numbers[i:i + size]) for i in range(0, len(plain_numbers), size)]
    return blocks

def hill_cipher_enc() : 
    plain_txt = input("enter the plain txt : ").lower()
    key , size = get_the_key()
    plain_numbers = get_blocks_of_plaintxt(plain_txt , size)
    cipher_numbers = []
    for block in plain_numbers : 
        multiply=np.dot(block , key)
        multiply=multiply%26
        for num in multiply : 
            cipher_numbers.append(chr(97 + num))
        
        
    return ''.join(cipher_numbers).upper()

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def extended_euclidean(a: int, b: int):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def multiplicative_inverse(a: int, m: int) -> int:
    gcd, x, _ = extended_euclidean(a, m)
    if gcd != 1:
        return None  # Inverse doesn't exist
    else:
        return x % m  # Ensure the result is positive

def matrix_determinant(matrix: np.ndarray) -> int:
    return int(np.round(np.linalg.det(matrix))) % 26

def matrix_inverse(key_matrix: np.ndarray) -> np.ndarray:
    det = matrix_determinant(key_matrix)
    det_inv = multiplicative_inverse(det, 26)
    
    if det_inv is None:
        raise ValueError("The key matrix is not invertible.")
    
    # Calculate the adjugate matrix
    adjugate = np.zeros_like(key_matrix)
    n = key_matrix.shape[0]
    
    for i in range(n):
        for j in range(n):
            minor = np.delete(np.delete(key_matrix, i, axis=0), j, axis=1)  # Minor matrix
            cofactor = ((-1) ** (i + j)) * int(np.round(np.linalg.det(minor))) % 26  # Cofactor
            adjugate[j, i] = cofactor  # Transpose to get adjugate
    
    # Multiply the adjugate by the modular inverse of the determinant
    inverse_matrix = (det_inv * adjugate) % 26
    return inverse_matrix

def hill_cipher_dec() :
    cipher_txt = input("please enter the cipher txt to decrypt : ").lower()
    key , size =get_the_key()  
    key_inverse = matrix_inverse(key)
    ciphertext_numbers = [ord(char) - ord('a') for char in cipher_txt if char.isalpha()]
    blocks = [np.array(ciphertext_numbers[i:i + size]) for i in range(0, len(ciphertext_numbers), size)]
    plaintext_letters = []
    for block in blocks:
        decrypted_block = np.dot(block, key_inverse) % 26
        for num in decrypted_block : 
          plaintext_letters.append(chr(num + 97))
    
    return ''.join(plaintext_letters).upper()

print("Welcom the hill cipher  : ")
cond = True
while cond:
    try:
        option = int(input("encryption---> 1 , decryption --->2 , decline --->0: "))
        while option not in range (0 , 3) : 
           option = int(input("Wrong option : only 1 , 2 , 0: "))
    except ValueError: 
           option = int(input("Value Error: only 1 , 2 , 0: "))   
    if option == 1 : 
        print(f"the encrypted message is : {hill_cipher_enc()}")
    elif option ==2 : 
        print(f"the decrypted message os : {hill_cipher_dec()}")
    else : 
        print("---Bye---")
        cond = False


    
    








   