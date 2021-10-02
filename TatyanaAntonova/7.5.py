class BaseException(Exception):
    pass

class NotNumberError(BaseException):
    pass
    
class MyAttributeError(BaseException):
    pass

def even_and_greater(num):
    """Checks wheather number is even and greater than 2"""
    if not isinstance(num, (int, float)):
         raise NotNumberError
    if num % 2 == 0 and num > 2:
        return True
    else:
        raise MyAttributeError(f"{num} is not even or not greater than 2")

if __name__ == "__main__":
    print(even_and_greater(4))