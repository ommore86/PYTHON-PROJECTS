'''
///STRINGS///
1. Immutable (Cant update)
2. Enclosed in " "
3. Ordered
4. Slicing
'''

# Creating String-
str = "Welcome to Programming"
# print(type(str))
# print(str)


# Accessing String-
# print(str[8])
# print(str[-1])


# Slicing / SSS - Start,Stop,Step
# print(str[2:12])
# print(str[0:12:2])
# print(str[3:-12])
# print(str[-11::])
# print(str[-11:-3:])
# print(str[-11:-3:2])
# print(str[::-1])      # Reversing a string


# Deleting entire string-
# del str
# print(str)


# Escape Sequences-
# str1 = 'I\'m Om More'
# print(str1)
# str1 = "I live in \"Kalyan\""
# print(str1)
# str1 = r"This is \110\110\456\644\456"      # To escape backslash we have to use r at the beginning
# print(str1)


# Formatting-
# str1 = "My name is {}. I am studing in {}. I live in {}".format("Om","GPT","Kalyan")
# str1 = "My name is {2}. I am studing in {0}. I live in {1}".format("GPT","Kalyan","Om")
# str1 = "My name is {n}. I am studing in {c}. I live in {p}".format(n="Om",c="GPT",p="Kalyan")
# print(str1)


# Getting Size of String-
# print(len(str))