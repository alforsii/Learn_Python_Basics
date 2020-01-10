# while loop
print('-------while loop--------------')
i = 0
while i <= 10:
    print(i)
    i += 1

print('Done looping')

# for loop
print('-----------for loop-------------')
print('----------prints 0 to 9------------------')
for i in range(10):
    print(i)

# for loop with arrays
# 1.
print('----------prints all in array------------------')
array = ['apple', 'banana', 'mongo']
for x in array:
     print(x)
# 2.
print('------------prints all elem in numbers array----------------')
numbers = [1, 2, 4, 6, 4]
for n in numbers:
    print(n)
# 3.
print('-----------prints all letters in a str-----------------')
str = 'banana'
for s in str:
    print(s)
# 4.
print('------------prints until gets banana----------------')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
# 5. Game if you enter right word you win else lose!
# print('----------------------------')
# secret_word = 'apple'
# guess = ''
# count_guesses = 0
# while guess != secret_word:
#     guess = input('Enter a secret word: ')
#     count_guesses += 1
#     if count_guesses == 3:
#         print('You lose!')
#         break
#     elif count_guesses < 3 and guess == secret_word:
#         print('You won!')

# 6.
print('---------it will print 5 to 9-------------------')
for i in range(5, 10):
    print(i)

# 7.
print('---------it will print all in ary-------------------')
ary = ['apple', 'banana', 'mango', 'orange']
length_of_ary = len(ary)
for index in range(length_of_ary):
     print(ary[index])

# 8.
# print('---------it will print all in ary-------------------')
# ary = ['apple', 'banana', 'mango', 'orange']
# length_of_ary = len(ary)
# for index in ary:
#      print(ary[index])
# TypeError: list indices must be integers or slices, not str

# 9. it gives a SyntaxWarning: "is" with a literal. Did you mean "=="?
#   if fruit is 'mango':
print('---------it will break when fruit is banana-------------------')
for fruit in ary:
    if fruit == 'mango':
        break
    print(f'current fruit is {fruit}')
