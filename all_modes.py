#CREATE A FILE:
# file=open("names.text","x")
# file.close()

#WRITE A FILE:
# file=open("doc.text","w")
# file.write("swathi_gundu\n")
# file.write("gouthami_priyanka\n")
# file.write("hima_bindu\n")
# file.close()


#READ A FILE:
# file=open("doc.text","r")
# for i in file:
#     print(file.read())
# file.close()
    
#APPEND A FILE:
#file=open("demo.text","a")
#file.write("hello")
#file.write("welcome")
#file.close()


#WRITE AND READ:
#file=open("demo.text","w+")
#file.write("hii am swathi i completed my graduation")
#a=file.read()
#print(a)
#file.close()

#READ AND WRITE:
# file=open("demo.text","r+")
# b=file.read()
# file.write("i love india")
# print(b)
# file.close()


#APPEND AND READ:
#file=open("demo.text","a+")
#file.write("bueatifull")
#c=file.read()
#print(c)
#file.close()


#READLINE:
#file=open("doc.text","r")
#a=file.readline()
#print(a)
#file.close()


#READLINES:
# file=open("doc.text","r")
# a=file.readlines()
# print(a)
# file.close()


#WRITE LINES:

# file=open("doc.text","w")
# file.write("hello world")
# file.close()

#WRITELINES:
# file=open("doc.text","w")
# a=["raja\n","rani\n","geetha\n","seetha\n"]
# file.writelines(a)
# file.close()

#READLINES:
# file=open("doc.text","r")
# a=["raja\n","rani\n","geetha\n","seetha\n"]
# file.readlines()
# print(a)
# file.close()
