number=[5,3,7,2,1]
print("Original Array=")
print(number)
n=len(number)

for i in range(n):
    
    for j in range(0,n-i-1):
        if(number[j]>number[j+1]):
            number[j],number[j+1]=number[j+1],number[j]

print("sorted Array=") 
print(number)