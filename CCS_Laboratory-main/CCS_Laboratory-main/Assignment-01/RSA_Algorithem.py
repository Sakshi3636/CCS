import math

p = 13
q = 11

n = p*q
print("n =", n)

phi = (p-1)*(q-1)

e = 13
while(e<phi):
    if (math.gcd(e, phi) == 1):
        break
    else:
        e += 1

print("e =", e)

if 1 < e < phi and math.gcd(e, phi) == 1:
 
    d = pow(e, -1, phi)
    print("d=",d)

    public_key = (e, n)
    private_key = (d, n)

    
    print("Public Key: ", public_key)
    print("Private Key: ", private_key)
else:
    print("Invalid public key. Pleasetryagain.")

msg = 11
print(f'Original message:{msg}')


C = pow(msg, e)
C = math.fmod(C, n)
print(f'Encrypted message: {C}')


M = pow(C, d)
M = math.fmod(M, n)

print(f'Decrypted message: {M}')    