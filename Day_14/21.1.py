class Pet:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

#class cat inheriting from the class pet
class Cat(Pet):
    def __init__(self, name, age):#called the super class function init
            super().__init__(name, age)

def main():
    thepet = Pet("pet", 1)
    jess = Cat("jess", 3)


     #is instance function is used to check wether class is inherited from other class

    print("Is jess the cat?" +str(isinstance(jess, Cat)))

if __name__ == '__main__':
     main()

