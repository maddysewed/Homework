class MyNumberCollection:
    """Collecting numbers and working with them"""
    def __init__(self, start, end=None, step=None):            
        if isinstance(start, (list, tuple)):
            if all(map(lambda x: isinstance(x, int), start)):
                self.coll = list(start)
            else:
                raise TypeError(f"{MyNumberCollection.__name__} supports only numbers!")
        else:
            if map(lambda x: isinstance(x, int), (start, end, step)):
                self.coll = [i for i in range(start, end, step)]
                self.coll.append(end)
            else:
                raise TypeError(f"{MyNumberCollection.__name__} supports only numbers!")
        self.idx = 0

    def __str__(self):
        return str(self.coll)

    def append(self, new_item):
        if isinstance(new_item, int):
            self.coll.append(new_item)
        else:
            raise TypeError(f"{MyNumberCollection.__name__} supports only numbers!")

    def __add__(self, new_coll):
        if isinstance(new_coll, MyNumberCollection):
            return self.coll + new_coll.coll
        else:
            raise TypeError(f"{MyNumberCollection.__name__} supports only its own instances!")

    def __getitem__(self, index):
        return self.coll[index]**2

    def __iter__(self):
        return self

    def __next__(self):           
        try:
            item = self.coll[self.idx]
        except IndexError:
            raise StopIteration()
        self.idx += 1
        return item

def main():
    col1 = MyNumberCollection((1,2,3,4,5)) # Testing
    col2 = MyNumberCollection(0, 5, 2)
    print(col1)
    col1.append(10)
    print(col1)
    print(col1 + col2)
    print(col1)
    print(col1[5])
    for item in col1:
        print(item)

if __name__ == "__main__":
    main()