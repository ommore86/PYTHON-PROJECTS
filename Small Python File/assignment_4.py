'''
    1.
    WAP to sort a list of tuples using lambda.
    Original list of tuples: [("English", 88), ("Science", 90), ("Maths", 97), ("Social Science", 82)]
    Sorting the list of tuples: [("Social Science", 82), ("English", 88), ("Science", 90), ("Maths", 97)]
'''
# lst = [("English", 88), ("Science", 90), ("Maths", 97), ("Social Science", 82)]
# res = sorted(lst, key=lambda i : i[-1])
# 
# print(res)


'''
    2.
    WAP to count the even and odd numbers in a given array of integers using lambda.
    Original Arrays: [1,2,3,5,7,8,9,10]
    Number of even numbers in the above array: 3
    Number of odd numbers in the above array: 5
'''
# lst = [1,2,3,5,7,8,9,10]
# even_res = len(list(filter(lambda n : n%2==0, lst)))
# odd_res = len(list(filter(lambda n : n%2!=0, lst)))

# print("Number of even numbers in the above array:", even_res)
# print("Number of odd numbers in the above array:", odd_res)


'''
    3.
    Write a Python function to create and print a list,
    where the values are the square of numbers between 1 and 30 (Both included)
'''
# def sqr():
#     lst = []
#     for i in range (1,30+1):
#         lst.append(i*i)
#     print(lst)

# sqr()


'''
    4.
    WAP to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700(both included)
'''
# def func():
#     for n in range (1500, 2700+1):
#         if n%5==0 and n%7==0:
#             print(n,end=" ")
# 
# func()


'''
    5.
    WAP to construct the following pattern, using a nested for loop.
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
'''
# def star():
#     for i in range(5):
#         for j in range(i+1):
#             print("*", end=" ")
#         print()

#     for i in range(5-1,0,-1):
#         for j in range(i):
#             print("*", end=" ")
#         print()

# star()


'''
    6.
    WAP to that takes two digits m(row) and n(column) as input and generates a two-dimensional array.
    The element value in the i-th row and j-th column of the array should be i*j.
    Note : i=0,1.., m-1
           j=0,1.., n-1

    Test Data: Rows=3, Columns = 4
    Expected Result : [(0,0,0,0)],[(0,1,2,3)],[(0,2,4,6)]
'''
def array(m,n):
    arr = []
    for i in range(0,m):
        for j in range(0,n):
            arr.append(i*j)
    print(arr)

m = int(input("Enter no. of rows: "))
n = int(input("Enter no. of columns: "))
array(m,n)