from time import time

def timer(handler):
    def wrapper(*args, **kwargs):
        t1 = time()
        res = handler(*args, **kwargs)
        t2 = time()
        with open("1.txt", "a") as f:
            f.write(str(round((t2 - t1), 5)) + "\n")
        return res
    return wrapper

@timer
def handle(body):
    print(body)

def main():
    handle("abcdefgh")

if __name__ == "__main__":
    main()