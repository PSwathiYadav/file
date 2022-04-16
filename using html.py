
#HTML:
student_name=["sonu","monu","vasu","rasi","nava","madu"]
file=open("student_name.html","w")
for i in student_name:
    file.write(i+"\n")
file.close()