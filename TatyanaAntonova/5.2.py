def main():
    def most_common_words(filepath, number_of_words=10):
        """Searches for most common words in the file"""
        from string import punctuation
        word_dict = {}
        with open(filepath, "r") as file:
            mas_0 = file.read().lower().split()
            mas = []
            for word_0 in mas_0:
                if word_0[len(word_0)-1] in punctuation:
                    word_0 = word_0[:len(word_0)-1]
                mas.append(word_0)
            del mas_0
            for word in mas:
                if (mas.count(word) in word_dict.keys()):
                    word_dict[mas.count(word)].add(word)
                else:
                    word_dict.update({mas.count(word): set([word])})
            final_lst = []
            cnt = 0
            flag = True
            for i in range(max(word_dict.keys()), 0, -1):
                if i in word_dict.keys():
                    for w in word_dict[i]:
                        if flag == True:
                            final_lst.append(w)
                            cnt += 1
                            if cnt == number_of_words:
                                flag = False
            return(final_lst)


    # Testing        
    print(most_common_words("C:\\Users\H P\\Desktop\\code\\PYTHON\\EPAM_training\\Session_5\\lorem_ipsum.txt", 13)) 
    
if __name__ == "__main__":
    main()
