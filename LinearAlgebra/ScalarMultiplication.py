num=int(input("Enter the number to create Scalar matrix="))

x=[[1,2,3],
   [5,6,7],
   [4,8,9]]

y=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        
        y[i][j]=num*x[i][j]
        

print("Scalar Multiplication of given Matrix is=")

for r in y:
    print(r)
