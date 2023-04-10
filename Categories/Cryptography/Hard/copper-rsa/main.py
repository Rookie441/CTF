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