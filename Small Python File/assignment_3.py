''' 
    1.
    Write a Python function to multiply all the numbers in a list.
    Sample list: [8,2,3,-1,7]
    Expected Output: -336
'''
def mul(lst):
    res=1
    for i in lst:
        res*=i
    print(res)

lst = [8,2,3,-1,7]
mul(lst)


'''
    2.
    WAP to reverse a string.
    Sample string: "1234abcd"
    Expected Output: "dcba4321"
'''
def rev(str):
    print(str[::-1])

str="1234abcd"
rev(str)


'''
    Write a Python function that accepts a string and counts the number of upper and lower case letters.
    Sample string: "The quick Brown Fox"
    Expected Output: No. of Upper case characters: 3 | No. of Lower case characters: 12
'''
def case(str):
    lower=0
    upper=0
    for i in str:
        if(i.islower()):
            lower+=1
        else:
            upper+=1
    print("The number of lowercase characters is: ", lower)
    print("The number of uppercase characters is: ", upper)

str = "ThequickBrownFox"
case(str)


'''
    WAP to print the even numbers from a given list.
    Sample list: [1,2,3,4,5,6,7,8,9]
    Expected Result: [2,4,6,8]
'''
def even(lst):
    for i in lst:
        if i%2==0:
            print(i,end=" ")

lst = [1,2,3,4,5,6,7,8,9]
even(lst)


'''
    Write a Python Function that checks whether a passed string is a palindrome or not.
    Note: A palindrome is a word, phrase or sequence that reads the same backward as forward,
    Eg. madam / nurses run
'''
def palindrome(str):
    rev = str[::-1]
    if str==rev:
        print("\n", str, "is a Palindrome")
    else:
        print("\n", str, "is not a Palindrome")

str = "anna"
palindrome(str)