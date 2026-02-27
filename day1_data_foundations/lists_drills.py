# **Simple list functions**
#
#def even_numbers(lst):
#    # Return a list of even numbers from the input list
#    even_numbers = []
#    
#    for number in lst:
#        if number % 2 == 0:
#            even_numbers.append(number)
#    return even_numbers    

#def reverse_list(lst):
#    # Return a new reversed list from the input list
#    reversed_list = []
#    for i in range(len(lst)-1, -1, -1):
#        reversed_list.append(lst[i])
#    return reversed_list
#
#print(reverse_list([10, 20, 30, 40]))

#def reverse_in_place(lst):
#    #Reverse the input list in place
#    left = 0
#    right = len(lst) -1
#    
#    while left < right:
#        lst[left], lst[right] = lst[right], lst[left]
#        
#        left += 1
#        right -= 1
#        
#lst = [10, 20, 30, 40, 50]
#reverse_in_place(lst)
#print(lst)


#def remove_duplicates(lst):
#    # Return a new list of individual unique elements from the input list
#    unique_elements = []
#    
#    for element in lst:
#        if element not in unique_elements:
#            unique_elements.append(element)
#    return unique_elements
#
#lst = [1, 2, 3, 2, 4, 1, 5]
#unique_list = remove_duplicates(lst)
#print(unique_list)

#def top_three(lst):
#    # Return a new list of te three latrgest vslues from the inpit list
#    if len(lst) < 3:
#        return sorted(lst, reverse=True)
#    sorted_list = sorted(lst, reverse=True)
#    return sorted_list[:3]
#lst = [10, 20, 5, 30, 15]
#top_three_values = top_three(lst)
#print(top_three_values)


#def normalize(lst):
#    # Return a new list of normalized values from the input list
#    if not lst:
#        return []
#    
#    max_value = max(lst)
#    min_value = min(lst)
#    
#    if max_value == min_value:
#        return [0.0] * len(lst)
#    
#    normalized_list = [(x - min_value) / (max_value - min_value) for x in lst]
#    return normalized_list

