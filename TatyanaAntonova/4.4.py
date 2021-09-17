def main():
    def split_by_index(s, indexes):
        """Splits the s string by indexes specified in [indexes]"""
        indexes.append(len(s))      
        final_lst = []
        pos = 0
        for index in indexes:
            if index <= len(s):
                final_lst.append(s[pos:index])
                pos = index
            else:
                final_lst = [f"{s}"]
                break
        return final_lst

    print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18])) # testing

if __name__ == "__main__":
    main()