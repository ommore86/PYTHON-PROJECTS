# Try Except Block
# try:
#     print(10/2)
# except ZeroDivisionError:
#     print("Dont delete by zero")


# Try Except Block without Error
# try:
#     n = int(input("Enter a number: "))
#     ans = 10/n
# except:
#     print("Please enter integer only...")
# else:
#     print("ans: ", ans)


# Try Except Block with Finally
# try:
#     n = int(input("Enter a number: "))
#     ans = 10/n
#     print(ans)
# except:
#     print("Please enter integer only...")
# finally:
#     print("Code completed. Thank You")


# Raise statement
# try:
#     age = int(input("Enter your age: "))
#     if age<18:
#         raise Exception
#     else:
#         print("You are eligible for election")
# except Exception:
#     print("Sorry, You are not eligible for voting")


# User Defined Exception
class Error(Exception):
    pass

class AgeSmallException(Error):
    pass

try:
    age = int(input("Enter your age: "))
    if age<18:
        raise AgeSmallException
    else:
        print("You are eligible for election")
except AgeSmallException:
    print("Sorry, You are not eligible for voting")
