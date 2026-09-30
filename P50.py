a = int(input("Enter a:"))
b=int(input("Enter b:"))

for i in range(a,b+1):
    reverse=0
    original=i
    while i>0:
        digit = i%10
        reverse=reverse*10+digit
        i=i//10
    if original==reverse:
        print("Palindrome:",original)
    