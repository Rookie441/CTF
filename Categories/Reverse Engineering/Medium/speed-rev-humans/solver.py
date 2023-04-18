from z3 import *

s = Solver()

# Define variables
param_1 = [BitVec('param_%d' % i, 8) for i in range(16)]

# Add constraints


'''
Insert conditions
'''

s.add(param_1[1] + param_1[0] == 0xc3)
s.add(param_1[2] + param_1[1] == 0xd9)
s.add(param_1[3] + param_1[2] == 0xd4)
s.add(param_1[4] + param_1[3] == 0xc0)
s.add(param_1[5] + param_1[4] == 0xa3)
s.add(param_1[6] + param_1[5] == 200)
s.add(param_1[7] + param_1[6] == 0xbe)
s.add(param_1[8] + param_1[7] == 0x80)
s.add(param_1[9] + param_1[8] == 0x99)
s.add(param_1[10] + param_1[9] == 0xd2)
s.add(param_1[11] + param_1[10] == 0xdd)
s.add(param_1[12] + param_1[11] == 0xbb)
s.add(param_1[12]  == ord('N'))
s.add(param_1[13]  == ord('c'))
s.add(param_1[14]  == ord('e'))



# Add additional constraints for lowercase letters, uppercase letters, and numbers
for i in range(16):
    s.add(Or(And(param_1[i] >= 48, param_1[i] <= 57),  # numbers
             And(param_1[i] >= 65, param_1[i] <= 90),  # uppercase letters
             And(param_1[i] >= 97, param_1[i] <= 122)))  # lowercase letters


# Check if the constraints are satisfiable and print the solution if it exists
if s.check() == sat:
    m = s.model()
    decoded_message = ''
    for i in range(16):
        char_value = m[param_1[i]].as_long()
        decoded_message += chr(char_value)
    print(decoded_message)
else:
    print("unsatisfiable")
    
'''
s.add(param_1[1] + param_1[0] == 0xda)
s.add(param_1[2] + param_1[1] == 0xa3)
s.add(param_1[3] + param_1[2] == 0x7b)
s.add(param_1[4] + param_1[3] == 0x94)
s.add(param_1[5] + param_1[4] == 0xc1)
s.add(param_1[6] + param_1[5] == 0xdd)
s.add(param_1[7] + param_1[6] == 0xb8)
s.add(param_1[8] + param_1[7] == 0xb0)
s.add(param_1[9] + param_1[8] == 0x9c)
s.add(param_1[10] + param_1[9] == 0x8d)
s.add(param_1[11] + param_1[10] == 0x8b)
s.add(param_1[12] + param_1[11] == 0x90)
s.add(param_1[13] + param_1[12] == 0x8a)
s.add(param_1[14] + param_1[13] == 0x75)
s.add(param_1[15] + param_1[14] == 0xa9)

s.add(param_1[0]  == ord('w'))
s.add(param_1[1]  == ord('w'))
s.add(param_1[2]  == ord('w'))
s.add(param_1[3]  == ord('w'))
s.add(param_1[4]  == ord('w'))
s.add(param_1[5]  == ord('w'))
s.add(param_1[6]  == ord('w'))
s.add(param_1[7]  == ord('w'))
s.add(param_1[8]  == ord('w'))
s.add(param_1[9]  == ord('w'))
s.add(param_1[10]  == ord('w'))
s.add(param_1[11]  == ord('w'))
s.add(param_1[12]  == ord('w'))
s.add(param_1[13]  == ord('w'))
s.add(param_1[14]  == ord('w'))
s.add(param_1[15]  == ord('w'))
'''

