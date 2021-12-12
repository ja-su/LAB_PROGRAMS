#creating dictionaries
di={'Roll no' : '54', 'Name' : 'joku', 'branch' : 'IT'}
#print(di)

d1=dict({1:'read', 2:'write', 3:'execute'})
#print(d1)



#accesing values in dictionary
print(di['Roll no'])
print(di['Name'])
print(di['branch'])

#add a new item to a dictionary
di['marks']=100
print(di)

#modifying an element
di['marks']=95
di['branch']='cs'
print(di)

#delete an element
del di['marks']
print(di)

#delete all entries
d1.clear()
print(d1)
del d1
print(d1)

#    di.get('Roll no')
#'54'
#>>> di.pop('Roll no')

