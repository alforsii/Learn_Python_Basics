
# keyword in py for creating function is def
name = 'Ashraf'
def say_hi():
    print('Hello ' + name + '!')

say_hi()
# ===================================
def say_hi2(name):
    print('Hello ' + name + '!')

# say_hi2() # TypeError: say_hi2() missing 1 required positional argument: 'name'
say_hi2('Mike')

# ===================================
def cube(num):
    return num * num * num

print(cube(3))


