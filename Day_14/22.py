class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def main():
    student1 = Student("Sugam", 25)

    print("Name:", student1.name)
    print("Age:", student1.age)

if __name__ == "__main__":
    main()