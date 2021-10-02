class MySquareIterator:
    """Returns squared elements"""
    def __init__(self, iterable):
        if isinstance(iterable, (tuple, list)):
            if all(map(lambda x: isinstance(x, int), iterable)):
                self.iterable = iterable
                self.idx = 0
            else:
                raise ValueError
        else:
            raise TypeError("Iterable objects only!")

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = self.iterable[self.idx]
        except IndexError:
            raise StopIteration()
        self.idx += 1
        return item**2

def main():
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)

if __name__ == "__main__":
    main()