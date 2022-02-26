myfile = open('todoList.txt', "w" , encoding='utf-8')
myfile.write("reading,\n coding,\n sports,")
myfile.close()

myfile = open("todoList.txt", "r", encoding="utf-8")
fille =  myfile.readlines()

print(fille)