#wap to reverse a string without the sslice operator
st="welcome to python"
new_st=""

i=len(st)-1
while(i>=0):
    new_st+=st[i]
    i-=1
print(new_st)
