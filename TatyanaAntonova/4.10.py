def main():
    def generate_squares(num):
        """Returns a dictionary with number: square items"""
        final_dict = {}
        for i in range(1, num+1):
            final_dict.update({i: i**2})
        return final_dict

    print(generate_squares(13)) # testing

if __name__ == "__main__":
    main()