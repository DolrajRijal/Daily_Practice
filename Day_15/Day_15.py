phone_book = {}



def data():

    name = input("enter the name:")
    phone_num = int(input("enter the phone number:"))
    phone_book[name] = name
    phone_book[phone_num] = phone_num


def view_data():
    for name, phone_num in phone_book.items():
        print(name, phone_num)

while True:

    print("please select:")
    print('1. add data \n 2.view data ')


    choice = int(input("Please enter your choice"))

    if choice == 1:
        data()
        print('Data added successfully')

    if choice == 2:
        view_data()
