# Fizz Buzz #2
# Write a function to print all numbers 1 to n, but there are some constraints
# If the number is divisible by 3, print ‘Fizz’ instead of the number
# If the number is divisible 5, print ‘Buzz’ instead of the number
# If the number is divisible by both 3 and 5, print ‘FizzBuzz’ instead of the number
# Otherwise, simply print the number

# n is always positive and n > 1,  and n is whole number
# define a function that takes n as a positive integer > 1
# for loop using range starting with 1, ending with n
# 3 constraints so need possibly 3 conditions
# num % 3 == 0, print "Fizz"
# num % 5 == 0, print "Buzz"
# num % 3 == 0 and num % 5 == 0, print "FizzBuzz"
# else print num

def fizz_buzz(n):

    for i in range(1, n): # will grab all numbers from 1 to n, not including n
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0: # modulo helps us see if a number is divisible by something in this case 3
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

fizz_buzz(16)