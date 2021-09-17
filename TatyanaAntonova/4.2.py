def main():
    def is_palindrome(string):
        """Checking whether a string is a palindrome or not"""
        string = str(string)
        if string == string[::-1]:
            return "It's a palindrome"
        return "Not a palindrome"       
           
    print(is_palindrome("12343211")) # testing

if __name__ == "__main__":
    main()