class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(self.name + " says Woof!")

def main():
    dog1 = Dog("Buddy", "Labrador")

    print("Name:", dog1.name)
    print("Breed:", dog1.breed)

    dog1.bark()

if __name__ == "__main__":
    main()