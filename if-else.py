# 1. if ... else basics
is_male = True

if is_male:
    print('#1.You are a male')
else:
    print('#1.You are a female')

# 2. or
is_tall = False

if is_male or is_tall:
    print('#2.You are a male or tall or both')
else:
    print('#2.You are neither male nor tall')

# 3. and

if is_male and is_tall:
    print('#3.You are a male and tall')
else:
    print('#3.You are either a male or tall or both')

# 4. else if

if is_male and is_tall:
    print('#4.You are a tall male')
elif is_male and not(is_tall):
    print('#4.You are a short male')
elif not(is_male) and is_tall:
    print('#4.You are not a male but tall')
else:
    print('#4.You are not a male and not tall')

# def with if

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else:
        return num3


print(max_num(5, 3, 7))

# comparisons: >, <, >=, <=, !=, ==

# How to make a calculator
num1 = float(input('Enter num1: '))
num2 = float(input('Enter num2: '))
op = input('Enter operator: ')

def calc(num1, num2, op):
    if op == '+':
        return float(num1) + float(num2)
    elif op == '-':
        return float(num1) - float(num2)
    elif op == '/':
        return float(num1) / float(num2)
    elif op == '*':
        return float(num1) * float(num2)
    else:
        return 'Invalid operator or number'

print(calc(num1, num2, op))

