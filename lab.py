# create file
myFile = open("todoList.txt", "x", encoding="utf-8")
myFile.close()

#------------------#

# write in it
myFile = open("todoList.txt", "w", encoding="utf-8")
myFile.writelines(["workout", "\ncode", "\nsleep"])
myFile.close()

#------------------#

# read file & print content
myFile = open("todoList.txt", "r", encoding="utf-8")
content = myFile.read()
myFile.close()
print(content)