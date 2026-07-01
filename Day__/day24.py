class pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class cat(pet):
    def __init__(self, name, age):
        super().__init__(name,age)
def main():

    obj1 = cat('tom',2)
    obj2 = pet('tyson', 4)
    print('is tom cat?: ' +str(isinstance(obj1,cat)))
    print('is tom pet?: ' +str(isinstance(obj1,pet)))
    print('is tyson cat?: ' +str(isinstance(obj2,cat)))
    print('is tyson pet?: ' +str(isinstance(obj2,pet)))

    print(obj1.name)

if __name__ == '__main__':
    main()