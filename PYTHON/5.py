n1=int(input("Enter the First Number"))
n2=int(input("Enter the second number:"))
for i in range(n1,n2+1,1):
    for j in range(1,11,1):
        print(i,j,j*i)
    print()
    
