a=int(input("Enter a:"))
b=int(input("Enter b:"))
for i in range(a,b+1):
    if i%400==0:
        print(i)
    elif i%100==0:
        continue
    elif i%4==0:
        print(i)