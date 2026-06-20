phone_book = {}



def data():

    name = input("enter the name:")
    phone_num = int(input("enter the phone number:"))
    phone_book['name'] = name
    phone_book['phone_num'] = phone_num


def view_data():
    for name, phone_num in phone_book:
        print(name, phone_num)

print("please select:")
choice = int(input('1. '))