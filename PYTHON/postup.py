#wap make a new tuple that has only  positive values
#in the list

tup_1=(-10,1,2,-9,3,4,-8,5,6)
new_tup=()
for i in tup_1:
    if(i>0):
        new_tup+=(i,)
print(tup_1)
print(new_tup)
print(tup_1.index(-9))
print(sorted(tup_1))
