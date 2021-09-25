def main():
    with open("C:\\Users\H P\\Desktop\\code\\PYTHON\\EPAM_training\\Session_5\\unsorted_names.txt", "r") as file_from:
        with open("C:\\Users\H P\\Desktop\\code\\PYTHON\\EPAM_training\\Session_5\\sorted_names.txt", "a") as file_to:
            for line in sorted(file_from.readlines()):
                file_to.write(f"{line}")

if __name__ == "__main__":
    main()