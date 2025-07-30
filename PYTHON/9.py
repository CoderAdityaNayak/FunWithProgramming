#10 o clock 60 degree
# 9 o clock 90 degree
print("Angle between the Hands \n")

for j in range(0,4,1):
    print()
    for i in range(0,12,1):
        val1=90-(j*30)+(i*30)-(2.5*i)
        val1=val1%360
        print("TIME: ",9+j,5*i,"                   ANGLE",val1)
print()






































print("SECOND PART OF THE CODE")
for j in range(1,6,1):
    print()
    for i in range(0,12,1):
        val2=30+(30*j-30)+(i*30)+(2.5*i)
        if(val2>=360):
           val2=val2%360
        print("TIME:",j,":",i*5,"                  ANGLE",val2)


for j in range(0,6,1):
    print()
    for i in range(0,12,1):
        val1=180-(j*30)+(i*30)-(2.5*i)
        if(val1>=360):
           val1=val1%360
        print("TIME: ",6+j,5*i,"                   ANGLE",val1)
