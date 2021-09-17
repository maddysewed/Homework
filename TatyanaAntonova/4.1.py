def main():
    def symb_replace(string):        
        """Replaces all " symbols with ' and vise versa"""
        new_str = ""
        for i in string:
            if i == "\"":
                new_str += "\'"
            elif i == "\'":
                new_str += "\""
            else:
                new_str += i
        return new_str

    print(symb_replace("Falala\":la\"la\'")) # testing

if __name__ == "__main__":
    main()