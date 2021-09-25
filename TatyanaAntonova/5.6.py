def main():
    def call_once(func):
        cached_res = []
        def wrapper(*args):
            if len(cached_res) == 1:
                return cached_res[0]
            else:
                cached_res.append(func(*args))
            return cached_res[0]
        return wrapper

    @call_once
    def sum_of_numbers(a, b):
        return a + b

    print(sum_of_numbers(11, 2)) # Testing
    print(sum_of_numbers(15, 12))

if __name__ == "__main__":
    main()