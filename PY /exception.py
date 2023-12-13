class BaseError(Exception):pass
class HighValueError(Exception):pass
class LowValueError(Exception):pass
value = 29
while(1):
    try:
        n=int(input("Enter number:"))
        if n > value:
            raise HighValueError
        elif n < value:
            raise LowValueError
    except LowValueError:
        print("Very Low Value, Give input again")
        print()
    except HighValueError:
        print("Very High value , give input again")
        print()
    else:
        print("Nice!Correct answer")
        break

# ------------------------------------------------------------------------------------------------------------------------

class CustomException(Exception):
    def __init__(self, message = "WASSUP BUDDY"):
        self.message = message
        super().__init__(self.message)

try:
    a=5
    b=0
    if b==0: raise CustomException("Division by 0")
    result = a/b
except CustomException as ce:
    print(f"This is a custom exception: {ce}")
finally:
    print("oh hi there")