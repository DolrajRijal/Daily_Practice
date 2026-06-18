count = 0
def add_task():
    task = input("Enter the task you want to add:")
    with open("To_Do_List.txt", 'a') as f:
        f.write(task + "\n")

def remove_task():
    with open("To_Do_List.txt", "r") as f:
       tasks =  f.readlines()
    for i, task in enumerate (tasks, start =1):
        print(f"{i}.{task.strip()}")
    
    n = int(input("enter which element you want to remove"))
    if 1 <= n <= len(tasks):
        tasks.pop(n-1)
        with open("To_Do_list.txt", "w") as f:
            f.writelines(tasks)
        print("Task removed successfully!")

    else:
        print("Please enter valid number")
        

def view_task():
    try:
        with open("To_Do_List.txt", 'r') as f:
            tasks = f.readlines()
        if not tasks:
            print("List Empty")
        else:
            for i, task in enumerate(tasks, start = 1):
                print(f"{i}. {task}")

    except FileNotFoundError:
        print("No task")

    











print("----------------TO DO LIST--------------------")
print("Please select the number alongside the task to perform that task")
print("\n 1. Add task\n")
print("\n 2. Remove task")
print("\n 3. View tasks" )

choice = int(input("Enter here: "))
if choice == 1:
    add_task()
    print("Task added successfully")

elif choice == 2:
    remove_task()

elif choice == 3:
    view_task()

else:
    print("please input valid choice")