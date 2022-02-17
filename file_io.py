from asyncore import read


writeFile = open("todoList.txt", "w+")
writeFile.write('["Coding in Python", "Learn new thing"]')
writeFile.close()
readFile = open("todoList.txt", "r")
print(readFile.read())
readFile.close()

