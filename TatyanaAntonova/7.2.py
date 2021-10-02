from contextlib import contextmanager

@contextmanager
def open_file(path, mode): 
    obj = open(path, mode)       
    try:                      
        yield obj
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        obj.close()

def main():
    with open_file("1.py", "r") as f: # Testing
        a = f.read()
        print(a)


if __name__ == "__main__":
    main()