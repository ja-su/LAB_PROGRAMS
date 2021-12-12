string=input("Enter your string: ")
v_count=0
c_count=0
ques_count=0


for i in string:
    if(i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        v_count+=1
    elif(i=="?"):
        ques_count+=1
    elif(i!=" "):
        c_count+=1
words=len(string)

print("The number of vowels: ",v_count)
print("The number of constants: ",c_count)
print("The number of words: ",words)
print("The number of question marks: ",ques_count)
