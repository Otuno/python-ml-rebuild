# **Rewrite simple FIzzBuzz logic from memory**
#
#def fizzbuzz(n):
#    result = []
#    for i in range(1, n + 1):
#        value = ''
#        if i % 3 == 0:
#            value += 'Fizz'
#        if i % 5 == 0:
#            value += 'Buzz'
#        if value == '':
#            value = i
#        result.append(value)
#    return result

# **Write a generalized version of the FizzBuzz logic**
#
#def fizzbuzz(n, divisor1, divisor2, word1, word2):
#    result = []
#    
#    for i in range(1, n + 1):
#        value = ''
#        if i % divisor1 == 0:
#            value += word1
#        if i % divisor2 == 0:
#            value += word2
#        if value == '':
#            value = i
#        result.append(value)
#        
#    return result