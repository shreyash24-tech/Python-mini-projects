num=int(input("Enter the number="))
n=num
sum=0
while(n>0):
    digit=n%10
    sum=sum+digit
    n=n//10

print("Sum of Digit in Number=",sum)