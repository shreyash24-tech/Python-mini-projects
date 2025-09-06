num=int(input("Enter the number="))
rev = 0
num2 = num
print("\n Original Number=", num)

while num > 0:
    
    digit = num % 10
    rev = rev*10 + digit
    num = num // 10

print("\n Reverse Number=", rev)

if num2 == rev :
    print("\n Number is Palindrome")
else :
    print("\n Number is not Palindrom")
