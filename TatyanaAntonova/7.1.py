class File:
    modes = ("r", "w", "x", "a", "t", "b", "+")

    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.opened = open(self.path, self.mode)
        return self.opened

    def __exit__(self, exc_type, exc_value, traceback):
        self.opened.close()
        if exc_value:
            raise

def main():
    with File("1.py", "r") as f: # Testing
        a = f.read()
        print(a)

    
if __name__ == "__main__":
    main()