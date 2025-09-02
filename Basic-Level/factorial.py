def factorial(num):
    for i in range(1,num):
        num=num*i
        
    return(num)
num=int(input("Enter the number="))
print("Factorial of given number =" , factorial(num))