def main():
    def get_pairs(lst):
        """Returns a list of tuples containing pairs of elements"""
        if len(lst) == 1:
            return None
        final_lst = []
        i = 0
        while i != len(lst)-1:
            final_lst.append(tuple([lst[i], lst[i+1]]))
            i += 1
        return final_lst

    print(get_pairs([1, 2, 3, 8, 9])) # testing

if __name__ == "__main__":
    main()