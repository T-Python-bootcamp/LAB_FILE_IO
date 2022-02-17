newFile = open("todoList.txt","w",encoding="utf-8")
newFile.write("shopping for new bag \n dinner with my friend \n Movie night")
newFile.close()

file = open("todoList.txt", "r" , encoding="utf-8")
c = file.read()
print(c)




