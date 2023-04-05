todos = []

while True:
    user_action = input("Choose to add, show or exit:")

    match user_action:
        case "add":
            todo = input("enter a todo:")
            todos.append(todo)
        case "show":
            print(todos)
        case "exit":
            break
print("byeeee")
