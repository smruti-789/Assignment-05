n = int(input("Enter number:"))
a = 1
b = 2
for i in range(n):
    print(a, end=" ")
    a,b = b, a*b