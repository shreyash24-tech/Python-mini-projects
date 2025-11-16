def fact(num):
    # Base case: factorial of 0 or 1 is 1
    if num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

# Take input from user
num = int(input("Enter the number: "))

print("Factorial of given number =", fact(num))
