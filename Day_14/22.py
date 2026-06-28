class MyClass:
    def __init__(self, num, name):
        self.num = num
        self.name = name

def main():
    me = MyClass(1337, "Harssh")
    print(f"{me.name} {me.num}")

if __name__ == "__main__":
    main()
    