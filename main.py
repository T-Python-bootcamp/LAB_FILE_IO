

# First step is Creating the .txt file
file = open('todoList.txt','x',encoding="utf-8")
file.close()

# Second is Writing to the file from the user 
file = open('todoList.txt','w')
content=[]
while True:
    temp = input("Enter Today's ToDo list: (Q for quitting):")
    if temp.upper()=='Q':
        break
    content.append(f"{len(content)+1}- {temp}\n")
file.writelines(content)
file.close()

# Lastly is reading the file in the terminal
file = open('todoList.txt','r',encoding="utf-8")
content = file.read()
print(content)
file.close()

