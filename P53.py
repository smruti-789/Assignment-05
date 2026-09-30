a=int(input("Enter a:"))
b=int(input("Enter b:"))
for n in range(a+1,b):
    original=n
    sum=0
    while n>0:
        digit=n%10
        fact =1
        for i in range(1,digit+1):
            fact=fact*i
        sum=sum+fact
        n=n//10
    if sum ==original:
        print(sum,"Strong Number")
   