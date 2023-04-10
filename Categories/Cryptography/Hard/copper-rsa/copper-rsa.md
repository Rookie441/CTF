## Copper RSA

[main.py](https://github.com/Rookie441/CTF/blob/main/Categories/Cryptography/Hard/copper-rsa/main.py)  
[encrypted.txt](https://github.com/Rookie441/CTF/blob/main/Categories/Cryptography/Hard/copper-rsa/encrypted.txt)

> The contents of main.py is as follows:

```python
from Crypto.Util.number import getPrime, bytes_to_long

FLAG = <REDACTED>

assert len(FLAG) == 49

msg = b"THIS FISH IS SO RAW " + FLAG + b" HE'S STILL FINDING NEMO"

msg = bytes_to_long(msg)
msg = 4 * (msg ** 2) + 521 * msg + 47829

e = 3
c_arr = []
n_arr = []

for i in range(5):
    p, q = getPrime(1024), getPrime(1024)
    n = p * q
    c = pow(msg, e, n)
    c_arr.append(c)
    n_arr.append(n)

print(f'c_arr = {c_arr}\nn_arr = {n_arr}')
```

> Here, we can see that the script generates five public-private key pairs using RSA encryption scheme. Each pair consists of a modulus `n` and an encrypted message `c`. These pairs are stored in two lists: `c_arr` and `n_arr`.

> - The modulus `n` is calculated as a product of two large prime numbers p and q
> - The encrypted message `c` is calculated as `msg^e mod n`, where msg is the plaintext message
> - The public exponent `e` has a fixed value of 3.

> The goal is to obtain the FLAG which is in the msg variable. This is achieved using a variant of the Coppersmith's method, called [Håstad's broadcast attack](https://en.wikipedia.org/wiki/Coppersmith%27s_attack#H%C3%A5stad's_broadcast_attack). This attack uses a set of encrypted messages where the same plaintext message is encrypted using several different public keys with the same small exponent e, and the goal is to recover the plaintext message.

> In this case, the attack is carried out by first computing a polynomial equation `f(x) = msg^e - c = 0 mod n` that represents the encrypted messages, and then using Coppersmith's method to find a small root of the polynomial equation modulo n, which corresponds to the plaintext message.

> Note that since the plaintext message was further obfuscated by the polynomial equation `msg = 4 * (msg ** 2) + 521 * msg + 47829`, we will have to solve the polynomial before getting our true plaintext.

> The following is the solver script, which can be found in [decrypt.py](https://github.com/Rookie441/CTF/blob/main/Categories/Cryptography/Hard/copper-rsa/decrypt.py).

```python
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
```

> The output is as follows:

```
THIS FISH IS SO RAW CS2107{c0pP3r_br@s5_Br0nz3_m3tAl_s73el_1r0n_Go1d} HE'S STILL FINDING NEMO
```

`CS2107{c0pP3r_br@s5_Br0nz3_m3tAl_s73el_1r0n_Go1d}`
