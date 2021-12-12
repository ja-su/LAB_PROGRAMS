#wap using functions to check whether two nos are equal,
#greater than or less  than

def check(x,y):
    if(x==y):
        return 0
    if(x>y):
        return 1
    if(x<y):
        return -1

a=30
b=10
result=check(a,b)
if(result==0):
    print("The nos are equal")
if(result==1):
    print("a is greater than b")
if(result==-1):
    print("b is greater than a")
