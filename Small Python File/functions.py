# # Simple function
# # No arguments, no return
# def show():
#     print("Hi Guys")

# show()

# # Arguments, no return
# def func(str):
#     print(str)

# str="Hello World"
# func(str)

# # No arguments, Return
# def test():
#     a,b = 10,20
#     return a+b, 4.37L

# print(test())

# # Arguments, Return
# def sum(a,b):
#     return a+b

# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# print(sum(a,b))


# Default argument
# def school(fname, lname, std=7, div="D"):
#     print(fname, lname,":" ,std, div)

# school("Om", "More")
# school("Om", "More", 8)
# school("Om", "More", 5, "C")
# school(lname="More", fname="Om", div="C")       # Calling function with keyword arguments


# Keyword argument
# def school(fname, lname, std, div):
#     print(fname, lname,":" ,std, div)

# school(lname="More", fname="Om", div="E", std=9)


# Positional argument (Should be used when we know the position of the arguments)
# def school(fname, lname, std, div):
#     print(fname, lname,":" ,std, div)

# school("Om", "More", 6, "E")


# Arbitary argument
# def func(*args):                    # Variable length non-keyword argument
#     for i in args:
#         print(i)

# func("Welcome", "to", "programming")
# func([1,2,3,4,5],[6,7,8,9])

# def kwfunc(**kwargs):               # Variable length keyword arguments
#     for key, value in kwargs.items():
#         print(key, ":", value)
#     # print(type(kwargs))

# kwfunc(fname="Om", lname="More", std=7, div="D")


# Docstring
# def evenodd(x):
#     '''Program to check whether given no. is even or odd'''
#     if x%2==0:
#         print("Even")
#     else:
#         print("Odd")

# evenodd(9)
# print(evenodd.__doc__)


# Anonymous Functions / Lambda Functions
# str = "HiGuys"
# upperFunc = lambda str : str.upper()
# print(upperFunc(str))

# sqr = lambda n : n*n 
# print(sqr(4))

# evenodd = lambda n : "Even" if n%2==0 else "Odd"
# print(evenodd(7))
# print(evenodd(6))

# max = lambda a,b : a if a>b else b
# print(max(7,33))


# Filter (It takes a function and a list as arguments) :-
# lst = [1,2,3,4,5,6,7,8,9]
# res = list(filter(lambda n:(n%2!=0), lst))
# print(res)

# age = [12,44,76,36,85,17]
# adult = list(filter(lambda n: n>=18, age))
# print(adult)


# Map (It takes a function and a list as arguments and returns the mofified list) -
# lst = [5,7,22,97,54,62,7723,73,61]
# final_lst = list(map(lambda n:(n*2), lst))
# print(final_lst)


# Reduce (It takes a function and a list as arguments and returns reduced result) -
# from functools import reduce
# lst = [5,8,10,20,50,100]
# sum = reduce((lambda x,y : x+y), lst)
# print(sum)