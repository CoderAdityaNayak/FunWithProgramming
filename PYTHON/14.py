import random as rd
def otp_gen1(size):
    n=size
    upper=(10**n)-1
    lower=(10**(n-1))
    rdn=rd.randint(lower, upper)
    return rdn
print(otp_gen1(7))