n = int(input("Enter n:"))
evencount=0
oddcount=0
while n>0:
    digit=n%10
    n=n//10
    if digit%2==0:
        evencount+=1
    elif digit%2!=0:
        oddcount+=1
print("Even Digits:",evencount)
print("Odd Digits:",oddcount)
