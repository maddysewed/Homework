def main():
    def singleton(cls):
        instances = {}
        def getinstance(*args, **kwargs):
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs) # Rewriting instance every time
            return instances[cls]
        return getinstance

    @singleton
    class my_class():
        def method(self):
            ...

    p = my_class() # Testing
    f = my_class()
    print(p.method() is f.method())
    print(p is f)

if __name__ == "__main__":
    main()