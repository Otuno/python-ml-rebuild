# **Implementing a linear search function**
#
#def linear_search(lst, target):
#    for index, value in enumerate(lst):
#        if value == target:
#            return index  # return the index of the first occurrence
#    return -1  # return -1 if target not found
#
## Example usage:
#
#numbers = [4, 2, 7, 1, 9]
#print(linear_search(numbers, 7))  # Output: 2
#print(linear_search(numbers, 5))  # Output: -1


# **Check for membership without using 'in'**
#
#def contains(lst, target):
#    for item in lst:
#        if item == target:
#            return True
#    return False
#
## Example usage:
#numbers = [4, 2, 7, 1, 9]

#print(contains(numbers, 7))  
#print(contains(numbers, 5))  


# **Write function to check if list has duplicates. Do not use set()**
#
def has_duplicates(lst):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] == lst[j]:
                return True
    return False

# Example usage:
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [1, 2, 3, 2, 5]

print(has_duplicates(numbers1))  
print(has_duplicates(numbers2)) 




