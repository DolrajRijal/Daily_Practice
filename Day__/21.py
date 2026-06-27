# class myclass:
#     num = 1333
#     name = 'sugam'

# me = myclass()
# def main():
#     print(str(me.num) +" " +me.name)

# if __name__ == '__main__':
#     main()

class MyClass:

    def __init__(self,num, name):
        self.num = num 
        self.name = name
def main():
    me = MyClass(123,'ugam')
    print(f'{me.name} {me.num}')

if __name__ == "__main__":
    main()