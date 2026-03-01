# **Build a simple menu-driven program: 
# * 1 - Sum list
# * 2 - Find max
# * 3 - Count events
# * 4 - Exit


def sum_list(lst):
    return sum(lst)

def find_max(lst):
    if not lst:
        return None
    maximum = lst[0]
    for num in lst:
        if num > maximum:
            maximum = num
    return maximum

def count_evens(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count

def menu_program():
    lst = []
    # Ask user to enter numbers for the list
    numbers = input("Enter numbers separated by spaces: ").split()
    lst = [int(num) for num in numbers]

    while True:
        print("\nMenu:")
        print("1 - Sum list")
        print("2 - Find max")
        print("3 - Count evens")
        print("4 - Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print("Sum of list:", sum_list(lst))
        elif choice == "2":
            print("Maximum value:", find_max(lst))
        elif choice == "3":
            print("Number of even numbers:", count_evens(lst))
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Try again.")


menu_program()