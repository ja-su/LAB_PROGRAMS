#matrix addition -user input
a=[]
n=int(input("Enter the size of the matrix as n: ")) #size of the matrix n x n
print("ENter the values inside the matrix")

for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    a.append(row)
print(a)

#displaying the matrix form

for i in range(n):
    for j in range(n):
        print(a[i][j], end=" ")  #end=" " -takes you to a new line
    print()

b=[]
n=int(input("Enter the size of the matrix as n: ")) #size of the matrix n x n
print("ENter the values inside the matrix")

for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    b.append(row)
print(b)

#displaying the matrix form

for i in range(n):
    for j in range(n):
        print(b[i][j], end=" ")  #end=" " -takes you to a new line
    print()


#sum
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(b)):
        result[i][j]=a[i][j]+b[i][j]

#display sum
for i in range(n):
    for j in range(n):
        print(result[i][j], end=" ")
    print()
