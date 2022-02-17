myFile = open("todoList.txt", "w", encoding="utf-8")
myFile.write("☑️ attend class \n ⬛ go out with my sister \n ⬛ eat lunch with my sister \n ⬛ go cycling ")
myFile.close()

myFile = open("todoList.txt", "r", encoding="utf-8")
content = myFile.readlines()
myFile.close()

print(content)