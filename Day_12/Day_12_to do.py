print("do you want to add or view the list?")
choice = input("if you want to add type A if you want to view type V").lower()
if choice == "a":
    try:
        with open("To_do_list.txt", "a") as f:
            f.write(input("ener the task:" + "\n"))
            print("task added successfully")

    except FileNotFoundError as e:
        print("file not found")        
else:
    try:
        with open("To_do_list.txt", "r") as f:
            print(f.read())

    except FileNotFoundError as e:
        print("Error:", e)



