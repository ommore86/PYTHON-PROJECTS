# 1. WAP to sort a list of integers in ascending order -
# lst = [33,11,7,19,6,10,9]
# lst.sort()
# print(lst)

# 2. WAP to find the greatest value in a list of integers -
# lst = [33,11,7,19,6,10,9]
# lst.sort()
# print(lst[-1])

# 3. WAP to find the average of a list of numbers -
# lst = [33,11,7,19,6,10,9]
# total = sum(lst)
# n = len(lst)
# avg = total/n
# print(round(avg,2))

# 4. WAP to remove all the duplicates from the list -
# lst = [1,2,3,3,4,5,6,5]
# print(type(lst),lst)
# set1 = set(lst)
# lst = list(set1)
# print(type(lst),lst)

# 5. WAP to find the second smallest element in a list -
# lst = [33,45,4,56,45,4,6,76,6]
# set1= set(lst)
# lst = list(set1)
# lst.sort()
# print(lst[1])

# 6. WAP to reverse a list of integers -
# lst = [1, 2, 3, 4, 5, 6]
# lst.reverse()
# print(lst)

# 7. WAP to find the sum of all elements in a list -
# lst = [33,11,7,19,6,10,9]
# total = sum(lst)
# print(total)

# 8. WAP to check if a given list is sorted in ascending order -
# lst = [33,11,7,19,6,10]
# lst = [1,2,3,4,5]
# nlist = lst.copy()
# lst.sort()
# if(nlist == lst):
#     print("The list is sorted in ascending order")
# else:
#     print("The list is not sorted in ascending order")

# 9. WAP to find the length of the longest increasing subsequence in a list of integers


# 10. WAP to find the median of a list of numbers - 
# lst = [33,11,7,19,6,10]
# lst.sort()                             # [6, 7, 10, 11, 19, 33]
# mid = round(len(lst)/2)
# print("Mid =",mid)
# if(mid%2==0):
#     print(lst[mid-1])
# else:
#     print((lst[mid-1] + lst[mid])/2)