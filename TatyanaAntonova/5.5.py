def main():
    def remember_result(func):
        buffer = [None, ]
        def wrapper(*args):
            buffer.append(func(*args))
            return f"Last result = '{buffer[len(buffer)-2]}'"
        return wrapper

    @remember_result
    def sum_list(*args):
        if isinstance(args[0], str):
            result = ""
        else:
            result = 0
        for item in args:
            result += item
        print(f"Current result = '{result}'")
        return result

    print(sum_list(1, 2)) # Testing
    print(sum_list(4, 2))
    print(sum_list("bc", "a"))

if __name__ == "__main__":
    main()