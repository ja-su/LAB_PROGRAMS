#WAP THAT COPIES 1ST 10 BYTES OF A FILE INTO ANOTHER.
#OPENING A FILE
WITH OPEN("FILE_1.TXT","RB") AS FILE1:
    WITH OPEN("FILE_2.TXT","WB") AS FILE2:
        BUF=FILE1.READ(10)#READING 10 BYTES
        FILE2.WRITE(BUF)#WRITING ONTO THE FILE

PRINT("FILE COPIED")
