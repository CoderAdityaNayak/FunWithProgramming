import random as rd

def otp_gen2(size,quantity):
    otps=[]
    def otp_gen1(size):
        upper=(10**size)-1
        lower=(10**(size-1))
        rdn=rd.randint(lower, upper)
        
        otps.append(rdn)
    for i in range(0,quantity,1):
        otp_gen1(size)
    return otps
print(otp_gen2(4, 10))
