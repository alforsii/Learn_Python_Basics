# To handle an error
# sometimes in our program when something goes wrong it will break the code
# and will give us an error
# to prevent that we can use try to catch if any error and not to break our code

# 1.
try:
    number = int(input('Enter a number: '))
    print(number)
except:
    print('Invalid input')
# now if we enter  not a number console will print 'Invalid input'
# so our code will not break, will handle the error and will execute
print('------end #1.----------')

# 2. We can also specify the error that we want to handle
try:
    number = int(input('Enter a number: '))
    value = 10 / number
    print(value)
except ZeroDivisionError:
    print('You cannot divide by zero')
except ValueError:
    print('Invalid input')

print('------end #2.----------')

# 3. It's good practice to catch specific error
try:
    number = int(input('Enter a number: '))
    value = 10 / number
    print(value)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)

