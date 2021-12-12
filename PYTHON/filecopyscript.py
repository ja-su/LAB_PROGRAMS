#wap that copies one python script indo another file in
#such a way that all comment lines are skipped
#and not copied in the destination file.

with open("filcopyfull.py","rb") as file1:
    with open("second_file.py","wb") as file2:
        while True:
            buf=file1.readline()
            if(len(buf)!=0):
                if(buf[0]==35):
                    continue
                else:
                    file2.write(buf)
            else:
                break
