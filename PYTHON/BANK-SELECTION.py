import random as rd
import os
b_name=["ICIC BANK","HDFC BANK","AXIS BANK","SBI BANK","CITI BANK"]
b_osize=[4,6,3,9,2]
sb=0
for i in range(0,101):
    os.system('cls')
    print("Good morning Dear Customer. Please select the name of your bank.Click '2' to switch bank.Click 1 to enter")
    for i in range(0,5,1):
        if sb==i:
            print("===>", end="")
        print(b_name[i])
    k_in=str(input())
    if k_in=="2":
        sb=sb+1
        if sb==5:
            sb=0
    if k_in=="1" and k_in!="2":
        break
    


#
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
print("OTP IS",otp_gen2(b_osize[sb], 1))
