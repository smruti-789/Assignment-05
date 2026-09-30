a=int(input("Enter a:"))
b=int(input("Enter b:"))
sum=0
for i in range(a+1,b):
    #print("Factors of",i,":")
    for j in range(1,(i//2)+1):
        if i%j==0:
            sum = sum+j
    if sum==i:
     print("Perfect Number is:", i)
    
    sum=0