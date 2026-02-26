# **Basic Syntax Recall**

#print("Day 1 - Python Rebuild")

#x = 3
#y = 4
#z = x + y

#print(z)

#if (z % 2) == 1:
#    print("z is odd")
#else:
#    print("z is even")
    
# **Loop Recall**

#for i in range(1, 21):
#    print(i)
    
#for num in range(20, 0, -1):
#     print(num)   

#for num in range(1, 51, 1):
#    print(num)


# **Function Recall**

#def square(num):
#    return num * num

#def rev_string(string):
#    return string[::-1]

#def is_prime(num):
#    if num < 2:
#        return False
#    for i in range(2, int(num**0.5) + 1):
#        if num % i == 0:
#            return False
#    return True

# **FizzBuzz**
def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)



