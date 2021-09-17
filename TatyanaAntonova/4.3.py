def main():    
    def my_split(string, splitter=" "):
        """Works the same as str.split method"""
        splitter = str(splitter)
        string = str(string) + splitter
        final_lst = []
        buffer = ""
        for i in string:
            if i != splitter:
                buffer += i
            else:
                final_lst.append(buffer)
                buffer = ""
        return final_lst

    print(my_split("Falalal a")) # testing

if __name__ == "__main__":
    main()