def main():
    a = "I am global variable!"

    def enclosing_funcion():
        a = "I am variable from enclosed function!"

        def inner_function():
            a = "I am local variable!"
            print(a)
        return inner_function()

    enclosing_funcion()


if __name__ == "__main__":
    main()