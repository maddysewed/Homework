def main():
    def get_top_performers(file_path, number_of_top_students=7):
        """Returns names of top performer students"""
        import csv
        with open(file_path) as file:
            reader = csv.DictReader(file)
            buffer = {}
            for row in reader:
                if row["average mark"] in buffer.keys():
                    buffer[float(row["average mark"])].add(row["student name"])
                else:
                    buffer.update({float(row["average mark"]): set([row["student name"]])})
            cnt = 0
            flag = True
            final_lst = []
            for i in range(len(buffer)):
                for w in buffer[max(buffer.keys())]:
                        if flag == True:
                                final_lst.append(w)
                                cnt += 1 
                                if cnt == number_of_top_students:
                                    flag = False
                del buffer[max(buffer.keys())]
        return final_lst


    def age_sorted_file(file_path, new_file_path):
        """Writes CSV student information to the new file
        in descending order of age
        """
        import csv
        with open(file_path, newline='') as file:
            reader = csv.DictReader(file)
            sorted_list = sorted(reader, key=lambda row: row["age"], reverse=True)
        with open(new_file_path, "a") as new_file:
            for i in range(len(reader.fieldnames)):
                if i != len(reader.fieldnames) - 1:
                    new_file.write(reader.fieldnames[i] + ",")
                else:
                    new_file.write(reader.fieldnames[i])
            new_file.write("\n")
            for item in sorted_list:
                new_file.write(item["student name"] + "," + item["age"] + \
                    "," + item["average mark"] + "\n")
        return True

    path = "C:\\Users\\H P\\Desktop\\code\\PYTHON\\EPAM_training\\Session_5\\students.csv"
    new_path = "C:\\Users\\H P\\Desktop\\code\\PYTHON\\EPAM_training\\Session_5\\1.txt"
    print(get_top_performers(path)) # Testing
    age_sorted_file(path, new_path)

if __name__ == "__main__":
    main()