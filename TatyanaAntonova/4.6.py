def main():
    def get_longest_word(s):
        """Returns the longest word in the given string"""
        word_lst = s.split()
        buffer_longest = ""
        for word in word_lst:
            if len(word) > len(buffer_longest):
                buffer_longest = word
        return buffer_longest

    print(get_longest_word('Any pythonista like namespaces a lot.')) # testing

if __name__ == "__main__":
    main()