def main():
    def foo(lst):
        """Returns a new list where the elements' product plased"""
        product = 1
        for el in lst:
            product *= el
        new_lst = []
        for i in lst:
            new_lst.append(int(product/i))
        return new_lst

    print(foo([1, 2, 3, 4, 5])) # testing

if __name__ == "__main__":
    main()