def main():
    def combine_dicts(*args):
        new_dict = {}
        for d in args:
            for key in d.keys():
                if key in new_dict.keys():
                    new_dict[key] += d[key]
                else:
                    new_dict.update({key: d[key]})
        return new_dict

    dict_1 = {'a': 100, 'b': 200} # testing
    dict_2 = {'a': 200, 'c': 300, 'e': 500}
    dict_3 = {'a': 300, 'd': 100}

    print(combine_dicts(dict_1, dict_2))
    print(combine_dicts(dict_1, dict_2, dict_3))

if __name__ == "__main__":
    main()