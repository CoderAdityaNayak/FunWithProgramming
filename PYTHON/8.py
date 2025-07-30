f1=open("in2.txt","r")
f2=open("out1.txt","w")
s1=str(f1.readline())
list1=s1.split(",")
n1=int(list1[0])
n2=int(list1[1])

for i in range(n1,n2+1,1):
    for j in range(1,11,1):
        s2=str[i]+"*"+str[j]+"="+str[i*j]
        f2.write(s2)
        print("\n")
        print()
        print("\n")
        
f2.close()
