class vector2d:
    x = 0.0
    y = 0.0

    def set(self, x, y):
        self.x = x
        self.y = y 
def main():
    vec = vector2d()

    vec.set(5,6)
    print("x: " +str(vec.x) + "\ny: " + str(vec.y))

if __name__ == '__main__':
    main()

