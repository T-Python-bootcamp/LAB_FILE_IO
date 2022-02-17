 
# myFile = open("todoList.txt", "w", encoding="utf-8")
# myFile.writelines("Complete my tasks with mr.Aqeel.\nLearn flask framework.\nTake some break - it's weekend!")
# myFile.close()

myFile = open("todoList.txt","r",encoding="utf-8")
print(myFile.read())
myFile.close()