# **Write a function thatàsums up values from a list of dictionaries**  
#
#def sum_values(dict_list, key):
#    total = 0
#    for d in dict_list:
#        if key in d:
#            total += d[key]
#    return total
#
## Example usage:
#
#data = [
#    {"value": 10, "name": "A"},
#    {"value": 20, "name": "B"},
#    {"value": 15, "name": "C"}
#]
#
#print(sum_values(data, "value"))


# **Wrte a function to find the diètionary with the highest score**
#
def highest_score(dict_list, key):
    if not dict_list:
        return None  # handle empty list
    
    max_dict = dict_list[0]
    
    for d in dict_list:
        if d.get(key, float('-inf')) > max_dict.get(key, float('-inf')):
            max_dict = d
            
    return max_dict
#
## Example usage:
#
data = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 92},
    {"name": "Charlie", "score": 78}
]

print(highest_score(data, "score"))

