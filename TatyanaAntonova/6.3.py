def main():
    from collections import deque
    class Cipher():
        _alphabet = ["a", "b", "c", "d", "e", "f", "g",
                    "h", "i", "j", "k", "l", "m", "n",
                    "o", "p", "q", "r", "s", "t", "u",
                    "v", "w", "x", "y", "z"]
        new_alphabet = deque(_alphabet)

        def __init__(self, keyword) -> None:
            self.keyword = keyword

        def edit_alphabet(self):
            for i in range(len(self.keyword)-1, -1, -1):
                self.new_alphabet.remove(self.keyword[i])
                self.new_alphabet.appendleft(self.keyword[i])
            return self.new_alphabet

        def encode(self, string):
            from string import punctuation
            self.new_alphabet = self.edit_alphabet()
            s = ""
            for letter in string:
                if letter not in punctuation and letter != " ":
                    if letter == letter.upper():
                        s += self.new_alphabet[self._alphabet.index(letter.lower())].upper()
                    else:
                        s += self.new_alphabet[self._alphabet.index(letter.lower())]
                else:
                    s += letter
            return print(s)

        def decode(self, string):
            from string import punctuation
            self.new_alphabet = self.edit_alphabet()
            s = ""
            for letter in string:
                if letter not in punctuation and letter != " ":
                    if letter == letter.upper():
                        s += self._alphabet[self.new_alphabet.index(letter.lower())].upper()
                    else:
                        s += self._alphabet[self.new_alphabet.index(letter.lower())]
                else:
                    s += letter
            return print(s)

    cipher = Cipher("crypto") # Testing
    cipher.encode("Hello world!")
    cipher.decode("Fjedhc dn atidsn!!")

if __name__ == "__main__":
    main()