#wap which handles the error or exception occurring when
#a file is being opened.

filename=input("Enter the file name: ")
try:
    file=open(filename,"r")

except IOError:
    print("there is no file named as",filename)
