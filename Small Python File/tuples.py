'''
///TUPLES///
1. Collection of things
2. Enclosed in ()
3. Ordered
4. Non-homogeneous
5. Immutable
6. Items cant be added nor removed once tuple is created
'''


# Creating single element tuple - 
# tpl1 = ("Python",)
# print(type(tpl1),tpl1)


# Creating tuples using constructor - 
# construct = tuple(("C","C++","Java","Python"))
# print(type(construct))
# print(construct)


tpl = (1,2,("C","Java","Python"),True,[1,5,"Kalyan","Mumbai"],"Hello")
# print(tpl[1])
# print(tpl[-1])
# print(tpl[1:3])
# print(tpl[-3:])
# print(tpl[-2][-2])
# print(tpl[-2][-2][::-1])
# print(tpl[::-1])
# print(tpl[2][::-1])


# Concatenation of Tuples - 
# tpl1 = (1, 2)
# tpl2 = ("Hello", "World")
# print(tpl1 + tpl2)


# Nesting of Tuples - 
# tpl1 = (1, 2)
# tpl2 = ("Hello", "World")
# tpl3 = (tpl1, tpl2)
# print(tpl3)


# Repetition of Python Tuples - 
# tpl = ('Python',)*5
# print(tpl)


# Deleting a tuple in Python -
# del tpl
# print(tpl)


# Length of a Tuple - 
# print(len(tpl))


# Converting String / List to Python - 
# lst = [0,1,2]
# print(tuple(lst))   # Only displaying as tuple
# print(tuple("python"))   # Only displaying as tuple


# Tuples in Loops - 
# tup = ("Hello",)
# n=5
# for i in range(n):
#     tup = (tup,)
#     print(tup)