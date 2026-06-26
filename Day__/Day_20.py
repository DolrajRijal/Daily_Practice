class Myclass:  #creating a new class

    #adding class variables

    num = 0
    name = ''
def Main():

    me = Myclass()# defining a object of class my class
    me.num = 1336 #accessing the attributes of a class through object?
    me.name = ' sugar'
    print(me.name + " " + str(me.num))

if __name__ == '__main__':
    Main()


