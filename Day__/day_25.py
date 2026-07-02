
class prac:
    def __init__(self,num):
        self.count = 0
        self.num = num

    def __iter__(self):
        return(self)
    def __next__(self):
        if self.count >= self.num:

            raise StopIteration
        self.count += 1
        return self.count
def main():
    count = prac(5)
    for i in count:
        print(i)

if __name__ == '__main__':
    main()

    