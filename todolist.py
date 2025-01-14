# Create Your First Python Program From UST

user = 'input'
data = []

def menu():
    print("Menu:")
    print("1. Add task")
    print("2. Mark As Done")
    print("3. View All Tasks")
    print("4. Exit")

while user != '4':
    menu()
    user = input("Enter your choice: ")
    
    if user == '1':
        item = input("Enter the task: ")
        data.append(item)
        print("Added Iteam: ", item)

    elif user == '2':
        iteam = input("Enter the task to mark as done: ")
        if iteam in data:
            data.remove(iteam)
            print("Removed Iteam: ", iteam)
        else:
            print("Iteam not found")

    elif user == '3':
        print("list of all tasks")
        for iteam in data:
            print(iteam)
        

    elif user == '4':
        print("Goodbye")

    else:
        print("please enter a valid option")
    