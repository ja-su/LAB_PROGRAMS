di={'Roll no' : '54', 'Name' : 'joku', 'branch' : 'IT'}

#check for a key
if 'branch' in di:
    print("key present")
    print(di['branch'])

#sort items based on keys
print(sorted(di.keys()))

