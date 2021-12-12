with open("data.txt","r") as file1:
    a1=[]
    a2=[]
    a3=[]
    for line in file1:
        row=line.split()
        a1.append(row[0])
        a2.append(row[1])
        a3.append(row[2])
file1.close()
print("Data in coloumn 1:",a1)
print("Data in coloumn 2:",a2)
print("Data in coloumn 3:",a3)
