'''
///DICTIONARY///
1. Collection of pairs of values(key-value)
2. In the form of {key : value}
3. Non-homogeneous
4. Immutable
5. Key - No Duplicates allowed
   Values - Duplicates allowed
6. Keys are Case Sensitive
'''


# Creating a Dictionary -
# dict = {1:"Government", 2:"Polytechnic", 3:"Thane"}
# print(type(dict))
# print(dict)

# Creating a Mixed Dictionary -
# set1 = set((1,2,"Hello","Guys"))
# dict1 = {"College":"GPT", 1:[1,2,3,4], "tpl":("Java","Python"), "set":set1 ,2:2}
# print(type(dict1))
# print(dict1)

# Creating a dictionary with dict() method - dict()
# Dict = dict({1:"Government", 2:"Polytechnic", 3:"Thane"})
# print(type(Dict))
# print(Dict)

# Creating a Dictionary with each item as a pair -
# Dict = dict([(1,"Government"), (2,"Polytechnic"), (3,"Thane")])
# print(type(Dict))
# print(Dict)

# Nested Dictionary -
# Dict = {1:"Government", 2:"Polytechnic", 3:{"A": "Welcome", "B":"to", "C":"Thane"}}
# print(Dict)

# Adding elements to a Dictionary -
# Dict = {}
# Dict[0] = "Welcome"
# Dict[1] = "to"
# Dict["Programming"] = "Python"
# print(Dict)

# Adding elements as a set to a Dictionary -
# Dict = {}
# Dict[0] = "Welcome"
# Dict[1] = "to"
# Dict["Programming"] = "Python"
# Dict["Set"] = (1,2,"Hi")
# print(Dict)

# Updating elements in a Dictionary -
# Dict = {1:"Government", 2:"Polytechnic", 3:{"A": "Welcome", "B":"to", "C":"Thane"}}
# print(Dict)
# Dict[2] = "College"
# print(Dict)

# Adding nested dictionary as an element in a Dictionary -
# Dict = {1:"Government", 2:"Polytechnic", 3:{"A": "Welcome", "B":"to", "C":"Thane"}}
# print(Dict)
# Dict["Nested"] = {"Language":{"C","C++","Python"}}
# print(Dict)


# Accessing Elements -
# dict1 = {"College":"GPT", 1:[1,2,3,4], "tpl":("Java","Python"),2:2}
# print(dict1["College"])
# print(dict1[1])
# print(dict1.get("tpl"))     # Accessing using get() method
# print(dict1[1][-2])
# print(dict1["tpl"][0])
# print(dict1["tpl"][-1][2:])
# print(dict1["College"][1])


# Deleting items using del() keyword - del()
# dict1 = {"College":"GPT", 1:[1,2,3,4], "tpl":("Java","Python"),2:2}
# print(dict1)
# del(dict1["College"])
# del(dict1[1][-1])
# print(dict1)