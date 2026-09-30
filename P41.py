a = int(input("Enter a:"))
b = int(input("Enter b:"))
x=max(a,b)
while True:
    if (x%a==0 and x%b==0):
        print(x)
        break
    x+=1