#matrix transpose
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

t_a=[[0,0,0],[0,0,0],[0,0,0]]
print("transpose matrix")
for i in range(len(a)):
    for j in range(len(a[0])):
        t_a[j][i]=a[i][j]

        
for i in range(n):
    for j in range(n):
        print(t_a[i][j], end=" ")  #end=" " -takes you to a new line
    print()