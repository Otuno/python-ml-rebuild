# **Reverse list using backward range**
# 
#def reverse_list(lst):
#    reversed_lst = []
#    
#    for i in range(len(lst) - 1, -1, -1):
#        reversed_lst.append(lst[i])
#        
#    return reversed_lst
#
## Example usage:
#numbers = [1, 2, 3, 4, 5]
#print(reverse_list(numbers))

# **Reverse list without backward range**
#
#def reverse_list_insert(lst):
#    reversed_lst = []
#    
#    for item in lst:
#        reversed_lst.insert(0, item)
#        
#    return reversed_lst
#
## Example usage:
#numbers = [1, 2, 3, 4, 5]
#print(reverse_list_insert(numbers))

# **Find the minimum value in a list**
#
#def find_min(lst):
#    if len(lst) == 0:
#        return None   # or raise ValueError("Empty list")
#    
#    minimum = lst[0]   # assume first element is the smallest
#    
#    for item in lst:
#        if item < minimum:
#            minimum = item
#            
#    return minimum
#
## Example usage:
#numbers = [7, 3, 9, 1, 5]
#print(find_min(numbers))

# **Find the second largest value in a list**
#
#def second_largest(lst):
#    if len(lst) < 2:
#        return None   # or raise ValueError("List must contain at least 2 elements")
#    
#    largest = float('-inf')
#    second = float('-inf')
#    
#    for num in lst:
#        if num > largest:
#            second = largest
#            largest = num
#        elif num > second and num != largest:
#            second = num
#            
#    if second == float('-inf'):
#        return None   # means no second distinct largest
#    
#    return second
#
## Example usage:
#numbers = [3, 1, 4, 1, 5, 9]
#print(second_largest(numbers))