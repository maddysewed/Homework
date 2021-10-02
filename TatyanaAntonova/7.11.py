def endless_fib_generator():
    i = 0
    j = 1
    while True:
        yield i
        j = i + j
        yield j
        i = i + j
        
def main():
    gen = endless_fib_generator()
    while True:
        print(next(gen))

if __name__ == "__main__":
    main()