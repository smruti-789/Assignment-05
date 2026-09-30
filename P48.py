a=int(input("Enter a:"))
b=int(input("Enter b:"))
fact=1
for i in range(a+1,b):
    print("Factors of",i,":")
    for j in range(1,i+1):
        if i%j==0:
            print(j)