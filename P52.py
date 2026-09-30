a = int(input("Enter a:"))
b = int(input("Enter b:"))
for i in range(a+1,b):
    original=i
    sum=0
    while i>0:
        digit = i%10
        sum=sum+digit*digit*digit
        i=i//10
    if sum==original:
        print(sum,"Armstrong")
    