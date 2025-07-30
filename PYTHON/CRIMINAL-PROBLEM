
status=["OPEN","CLOSED"]
arr1=["CLOSED"]*100
for j in range(1,101,1):
    for i in range(1,101,1):
        if i%j==0:
            if arr1[i-1]==status[0]:
                arr1[i-1]=status[1]
            else:
                arr1[i-1]=status[0]
    print("DOOR",j,arr1[j-1])
