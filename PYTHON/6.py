f1=open("in1.txt","r")
n1=int(f1.readline())
n2=int(f1.readline())
for i in range(n1,n2+1,1):
    for j in range(1,11,1):
        print(i,j,i*j)
    print()
    
