def main():
    def get_digits(num):
        """Returns a tuple of a given integer's digits"""
        num = str(num)
        final_tpl = []
        for i in num:
            final_tpl.append(int(i))
        return tuple(final_tpl)

    print(get_digits(87178291199)) # testing

if __name__ == "__main__":
    main()