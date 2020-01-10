
# 1.
print(3**4)

# 2.
def to_power(num, pow_num):
    return pow(num, pow_num)

print(to_power(3, 3))

# 3.
def to_power(num, pow_num):
    result = 1
    for index in range(pow_num):
        result *= num
    return result

print(to_power(3, 2))




