x=1
for i in range(1,6):
    for j in range(1,i+1):
        if j==1 or i==j or i==5:
            print(chr(96+x),end=" ")
        else:
            print(" ",end=" ")
        x+=1
    print()    