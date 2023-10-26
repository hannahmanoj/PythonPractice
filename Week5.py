#task1

# inputs a digit from user to be checked as odd or even
#number = input("Enter a number: ")
# int function converts the input to an integer
#number = int(number)
# prints the number
#print("The numbered entered was", number)
# to check if the no is odd or even we use modulus, if remainder is 0 its even and if its anything else it's odd
#if (number % 2) == 0 and (number % 10) == 0:
 #   print("That is an even number")
    #print("The number is divisible by 10")

#elif (number % 2) == 0 and (number % 10) != 0:
 #   print("That is an even number")
  #  print("The number is not divisible by 10")


#else:
 #   print("That is an odd number")
  #  print("The number is not divisible by 10")


#task2

#import sys
#count = len(sys.argv)
#total = 0
#while count > 1:
 #    count -= 1
  #   total += float(sys.argv[count])
   #  avg = (total/float(sys.argv[count]))
#if total==0:
 #   print("no arguments were provided")
#else:
    #print("Total is", total)
    #print("The average is", avg)



#task3

#def average(values):
 #   """ Calculates the average of the given list. """
  #  total = 0
   # for n in values: # total the given values
    #    total += float(n)
   #return total/len(values) # return calculated average
# initialisation statement
#print(Welcome, utils module has been imported and initialised!")

#task4

#in new file utils_test.py
#from my_utils import average

#print("average is", average([10,23,30]))
#print("Another average is", average([10.2, 8.8, 2.6]))

#task5
# to directly import average without mentioning

#from my_utils import *

#print("average is", average([10,23,30]))
#print("Another average is", average([10.2, 8.8, 2.6]))

#task6

#import math
#print(dir(math))
#result ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

#task7

from math import *
#print(dir())
#result ['__annotations__', '__builtins__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

#task8

#import sys
#print("The import search path for this program is", sys.path)