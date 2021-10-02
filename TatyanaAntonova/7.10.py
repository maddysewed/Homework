def endless_generator():
    i = 1
    while True:
        yield i
        i += 2

def main():
    gen = endless_generator()
    while True:
        print(next(gen))

if __name__ == "__main__":
    main()