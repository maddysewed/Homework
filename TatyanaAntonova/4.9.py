def main():
    import string

    def test_1_1(*strings):
        """Returns characters that appear in all strings"""
        letters = test_1_2(*strings)
        cnt = 0
        final_set = set()
        for i in letters:
            for word_ in strings:
                if i in word_:
                    cnt += 1
            if cnt == 3:
                final_set.add(i)
            cnt = 0              
        return final_set

    def test_1_2(*strings):
        """Returns characters that appear in at least one string"""
        letters = set()
        for word in strings:
            for letter in word:
                    letters.add(letter)
        return letters

    def test_1_3(*strings):
        """Returns characters that appear at least in two strings"""
        letters = test_1_2(*strings)
        cnt = 0
        final_set = set()
        for i in letters:
            for word_ in strings:
                if i in word_:
                    cnt += 1
            if cnt >= 2:
                final_set.add(i)
            cnt = 0              
        return final_set

    def test_1_4(*strings):
        """Returns characters of alphabet, that were not used in any string"""
        final_set = set()
        letters = test_1_2(*strings)
        for i in string.ascii_lowercase:
            if i not in letters:
                final_set.add(i)
        return final_set

    print(test_1_1(*["hello", "world", "python", ]))  # testing
    print(test_1_2(*["hello", "world", "python", ]))
    print(test_1_3(*["hello", "world", "python", ]))
    print(test_1_4(*["hello", "world", "python", ]))

if __name__ == "__main__":
    main()