'''
///SETS///
1. Collection of things
2. Enclosed in {}
3. Unordered
4. Non-homogeneous
5. Mutable
6. NO Duplicates
'''


# Creating a set using Set Function -
# set = set("Hello World")
# print(type(set))
# print(set)

# Creating a set function using constructor by passing parameter to it -
# string = "Hi Guys"
# set1 = set(string)
# print(set1)

# Creating a Set using list -
# set1 = set([1,2,"Hello","World"])
# print(set1)

# Creating a Set using Tuple -
# set1 = set((1,2,"Hello","World"))
# print(set1)

# Creating a Set using Dictionary -
# set1 = set({1:"Welcome", 2:"To", 3:"Programming"})
# print(set1)

# Creating set directly -
# my_set = {1,2,3}
# print(my_set)


'''NOTE - Lists cannot be added to a set as elements, because lists are not hashable
          Tuples can be added to a set as elements, because tuples are hashable'''


# Single elements can be added using add function - Add()
# set1 = set()
# set1.add(8)
# set1.add(9)
# set1.add("String")
# set1.add((6,7))
# for i in range(1,6):
#     set1.add(i)
# print(set1)
# print(type(set1))


# Multiple elements can be added using update() function -
# set1 = set([1,2,3,("Hello","world")])
# set1.update([10,11,"String", ("Hi","Guys")])
# print(set1)


# Accessing Sets - 
# set1 = set(["Welcome","to","Programming"])
# print(set1)
# for i in set1:
#     print(i, end=" ")
# print("\n")
# print("to" in set1)     # Checking if the element is present or not


# Removing element from the set(By passing value/element) -
# set1 = set([1,2,3,4,5,6,7,8,9,10,11,12])
# print(set1)
# set1.remove(9)
# set1.remove(7)
# set1.discard(2)
# set1.discard(3)
# for i in range(10,12+1):
#     set1.remove(i)
# print(set1)

# Removing last element from the set -
# set1 = set([1,2,3,4,5,6,7,8,9,10,11,12])
# print(set1)
# set1.pop()
# print(set1)

# To clear all elements - (Clear())
# set1 = set([1,2,3,4,5,6,7,8,9,10,11,12])
# print(set1)
# set1.clear()
# print(set1)


# Typecasting -
# lst = [1,2,3,4,5,6]                             # List to Set
# set1 = set(lst)
# print(type(set1),set1)
# str = "Welcome to Python"                       # String to Set
# set2 = set(str)
# print(type(set2),set2)
# dictionary = {1:"One", 2:"Two", 3:"Three"}      #Dictionary to Set
# set3 = set(dictionary)
# print(type(set3),set3)