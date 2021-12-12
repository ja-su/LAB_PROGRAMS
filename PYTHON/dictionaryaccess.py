student= {101:'aaa', 104:'ttt', 103:'xxx',102:'ccc',105:'yyy'}
print(student)
#acces keys
for key in student:
    print(key, end='\t')
print('\n')
#access values
for val in sorted(student.values()):
    print(val, end='\t')

print('\n')

#accesing items
for key,val in sorted(student.items()):
    print(key,val,end='\t')
