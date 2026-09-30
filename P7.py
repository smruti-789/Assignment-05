n = int(input("Enter number:"))
if n>2:
    prime = True
for i in range(2,n):
    if n % i == 0:
        prime = False
        break
if prime:
    print("Prime number")
else:
    print("Non Prime Number")
