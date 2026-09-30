a=int(input("Enter a:"))
b=int(input("Enter b:"))
for i in range(a+1,b):
    fact=1
    for j in range(1,i+1):
        fact=fact*j
    print("Factorial of",i,":",fact)