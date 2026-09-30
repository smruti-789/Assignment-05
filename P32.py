n = int(input("Enter n:"))
for i in range(n):
    if i%2==0:
       print(chr(65+i),end=" ")
    else:
        print(chr(97+i),end=" ")