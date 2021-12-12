#wap that creates a new list of words by combining the words
# in two differnt list

list_1=["hello ","world "]
list_2=["python","programming"]

comb=[]

for i in list_1:
    for j in list_2:
        w=i+j
        comb.append(w)
print("combined list",comb)
        
