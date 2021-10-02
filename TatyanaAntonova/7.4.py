import logging

def supressor(func):
    file = "sample.log"
    logging.basicConfig(filename=file, 
                        level=logging.INFO, filemode="a")
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
            with open(file, "r") as f:
                print(f.read())
        except Exception:
            logging.exception("Error!")
        return True
    return wrapper

@supressor
def foo(a, b):
    return a/b

def main():
    foo(2, 1)

if __name__ == "__main__":
    main()