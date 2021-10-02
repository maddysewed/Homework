class EvenRange:
    def __init__(self, start, end):
        if isinstance(start, int) and isinstance(end, int):
            self.coll = []
            self.even_coll = []
            i = start
            while i <= end:
                self.coll.append(i)
                if i % 2 == 0:
                    self.even_coll.append(i)
                i +=1
            self.idx = 0
        else:
            raise ValueError

    def __str__(self):
        return str(self.coll)

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.even_coll[self.idx]
        except IndexError:
            raise StopIteration("Out of numbers!")
        self.idx += 1
        return item

def main():
    er1 = EvenRange(7,11)
    print(er1)
    for number in er1:
        print(number)
    print(next(er1))

if __name__ == "__main__":
    main()