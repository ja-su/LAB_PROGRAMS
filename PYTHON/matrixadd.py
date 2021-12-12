#wap that defines two matrices and print its sum

x=[[2,5,4],
   [1,3,9],
   [7,6,2]]

y=[[1,8,5],
   [7,3,6],
   [4,0,9]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j]=x[i][j]+y[i][j]
for r in result:
    print(r)
  
