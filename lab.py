
write_file = open("todoList.txt", 'w', encoding='utf-8')
write_file.write(
    'Eat breakfast. \n Go to python bootcapm. \n Solve problems. \n Back to home')
write_file.close()

read_content = open("todoList.txt", 'r+', encoding='utf-8')
myContent = read_content.read()
read_content.close()
print(myContent)
