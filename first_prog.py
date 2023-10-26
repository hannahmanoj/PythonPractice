# inputs a digit from user to be checked as odd or even
number = input("Enter a number: ")

# int function converts the input to an integer
number = int(number)

# prints the number
print("The numbered entered was", number)

# to check if the no is odd or even we use modulus, if remainder is 0 its even and if its anything else it's odd
if (number % 2) == 0 and (number % 10) == 0:
    print("That is an even number")
    print("The number is divisible by 10")

elif (number % 2) == 0 and (number % 10) != 0:
    print("That is an even number")
    print("The number is not divisible by 10")


else:
    print("That is an odd number")
    print("The number is not divisible by 10")