from Crypto.Util.number import getPrime, bytes_to_long
import ast

# Extract c_arr and n_arr from encrypted.txt
with open('encrypted.txt', 'r') as f:
    contents = f.read()
    c_arr_str = contents.split('=')[1].split('\n')[0].strip()
    n_arr_str = contents.split('=')[2].strip()
    c_arr = ast.literal_eval(c_arr_str)
    n_arr = ast.literal_eval(n_arr_str)
    
f.close()

def cube_root(x): 
    high = 1
    while high ** 3 < x:
        high *= 2
    low = high//2
    while low < high:
        mid = (low + high) // 2
        if low < mid and mid**3 < x:
            low = mid
        elif high > mid and mid**3 > x:
            high = mid
        else:
            return mid
    return mid + 1

totalSum = 0
allNMultiply = 1

# Multiply all modulo together
'''
The purpose of this computation is to obtain a value that is a cubic residue modulo each modulus in n_arr.
This allows us to apply the Chinese Remainder Theorem (CRT) to obtain a unique solution modulo the product of all the moduli.
Finally, the cube root of the resulting value modulo the product of all the moduli is taken to obtain the recovered plaintext message.
'''
for i in range(0, 5):
  allNMultiply *= n_arr[i]

for i in range(0, 5):
  quotient = allNMultiply // n_arr[i]
  totalSum += pow(quotient, -1, n_arr[i]) * c_arr[i] * quotient

# Cube Root
plainTextDec = cube_root(totalSum % allNMultiply)
#print(plainTextDec)

'''
We are not done yet because msg was further obfuscated by a polynomial equation, which we will need to solve.
'''
from sympy import *
x = Symbol('x')
'''
SymPy returns a list of all real or complex solutions to the polynomial equation.
Takes the maximum real solution of the equation and convert it to an integer using int()
'''
answer = int(max(solve(4*x**2 + 521*x + (47829-plainTextDec), x)))
msg = bytes.fromhex(hex(answer)[2:]).decode()
print(msg)
